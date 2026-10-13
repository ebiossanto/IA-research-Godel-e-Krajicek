#!/usr/bin/env python3
"""
GeoGebra Export Integration — Exportação de dados fractais para GeoGebra
Integração com o Terminal-Laboratório
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class GeoGebraExport:
    timestamp_utc: str
    data_source: str
    export_type: str
    filename: str
    format: str
    elements_count: int
    file_size_bytes: int

class GeoGebraExporter:
    """
    Exportador para GeoGebra — Gera arquivos .ggb e XML para importação
    """
    
    def __init__(self):
        self.export_log = []
    
    def create_point(self, x: float, y: float, label: str = "", 
                     color: str = "#0000FF", size: int = 5) -> Dict:
        """Cria elemento ponto GeoGebra"""
        return {
            "type": "point",
            "label": label,
            "coords": {"x": x, "y": y, "z": 0},
            "style": {
                "color": color,
                "size": size,
                "pointStyle": 0
            },
            "showLabel": True,
            "layer": 0
        }
    
    def create_segment(self, point1: str, point2: str,
                       color: str = "#0000FF", thickness: int = 2) -> Dict:
        """Cria segmento entre dois pontos"""
        return {
            "type": "segment",
            "points": [point1, point2],
            "style": {
                "color": color,
                "thickness": thickness,
                "lineStyle": 0
            }
        }
    
    def create_polyline(self, points: List[str], 
                        color: str = "#0000FF", thickness: int = 2,
                        fill: bool = False) -> Dict:
        """Cria polilinha conectando pontos"""
        return {
            "type": "polyline",
            "points": points,
            "style": {
                "color": color,
                "thickness": 2,
                "lineStyle": 0,
                "fill": fill
            }
        }
    
    def create_function(self, expression: str, 
                        xmin: float = -10, xmax: float = 10,
                        color: str = "#FF0000", thickness: int = 2) -> Dict:
        """Cria função matemática"""
        return {
            "type": "function",
            "expression": expression,
            "domain": {"min": xmin, "max": xmax},
            "style": {
                "color": color,
                "thickness": 2
            }
        }
    
    def create_slider(self, name: str, value: float, 
                      min_val: float, max_val: float, step: float = 0.1) -> Dict:
        """Cria slider interativo"""
        return {
            "type": "slider",
            "name": name,
            "value": value,
            "min": min_val,
            "max": max_val,
            "step": step,
            "animation": {
                "speed": 1,
                "repeat": "increasing"
            }
        }
    
    def create_text(self, text: str, x: float, y: float,
                    font_size: int = 12, color: str = "#000000") -> Dict:
        """Cria texto estático"""
        return {
            "type": "text",
            "text": text,
            "position": {"x": x, "y": y},
            "style": {
                "fontSize": font_size,
                "color": color
            }
        }
    
    def generate_ggb_xml(self, elements: List[Dict], 
                         metadata: Dict = None) -> str:
        """Gera XML completo para arquivo .ggb"""
        
        if metadata is None:
            metadata = {
                "title": "Fractal Analysis",
                "author": "Fractal Engine",
                "date": datetime.now(timezone.utc).isoformat()
            }
        
        # Header XML
        xml = '''<?xml version="1.0" encoding="UTF-8"?>
<geogebra format="5.0" version="5.0">
  <kernel>
    <continuous val="true"/>
    <decimals val="2"/>
  </kernel>
  <euclidianView>
    <size width="800" height="600"/>
    <coordSystem xZero="400" yZero="300" scale="50" yscale="50"/>
    <grid type="1" color="#dddddd" distance="50" ydistance="50" xdistance="50"/>
  </euclidianView>
  <construction>
'''
        
        # Adiciona elementos
        for i, element in enumerate(elements):
            element_type = element.get("type", "point")
            
            if element.get("type") == "point":
                coords = element.get("coords", {"x": 0, "y": 0, "z": 0})
                label = element.get("label", f"P{i}")
                color = element.get("style", {}).get("color", "#0000FF")
                size = element.get("style", {}).get("size", 5)
                
                xml += f'''    <element type="point" label="{label}">
      <show object="true" label="true"/>
      <color r="{int(element.get("style", {}).get("color", "#0000FF")[1:3], 16)}" 
             g="{int(element.get("style", {}).get("color", "#0000FF")[3:5], 16)}" 
             b="{int(element.get("style", {}).get("color", "#0000FF")[5:7], 16)}"/>
      <coords x="{element.get("coords", {}).get("x", 0):.6f}" 
               y="{element.get("coords", {}).get("y", 0):.6f}" z="0"/>
      <style pointSize="{element.get("style", {}).get("size", 5)}" 
             color="#{element.get("style", {}).get("color", "#0000FF")[1:]}"/>
      <show object="true" label="true"/>
    </element>
'''
            
            elif element.get("type") == "segment":
                points = element.get("points", [])
                color = element.get("style", {}).get("color", "#0000FF")
                thickness = element.get("style", {}).get("thickness", 2)
                
                xml += f'''    <element type="segment" label="seg">
      <show object="true" label="false"/>
      <color r="{int(element.get("style", {}).get("color", "#0000FF")[1:3], 16)}" 
             g="{int(element.get("style", {}).get("color", "#0000FF")[3:5], 16)}" 
             b="{int(element.get("style", {}).get("color", "#0000FF")[5:7], 16)}"/>
      <points>{" ".join(points)}</points>
      <style thickness="{thickness}" lineStyle="0"/>
    </element>
'''
        
        elif element.get("type") == "polyline":
            points = element.get("points", [])
            color = element.get("style", {}).get("color", "#0000FF")
            thickness = element.get("style", {}).get("thickness", 2)
            fill = element.get("style", {}).get("fill", False)
            
            xml += f'''    <element type="polyline" label="polyline">
      <show object="true" label="false"/>
      <color r="{int(element.get("style", {}).get("color", "#0000FF")[1:3], 16)}" 
             g="{int(element.get("style", {}).get("color", "#0000FF")[3:5], 16)}" 
             b="{int(element.get("style", {}).get("color", "#0000FF")[5:7], 16)}"/>
      <points>{" ".join(points)}</points>
      <style thickness="{thickness}" lineStyle="0" filling="{str(fill).lower()}"/>
    </element>
'''
        
        elif element.get("type") == "function":
            expr = element.get("expression", "x")
            xmin = element.get("domain", {}).get("min", -10)
            xmax = element.get("domain", {}).get("max", 10)
            color = element.get("style", {}).get("color", "#FF0000")
            thickness = element.get("style", {}).get("thickness", 2)
            
            xml += f'''    <element type="function" label="f">
      <show object="true" label="true"/>
      <expression>{expr}</expression>
      <domain min="{xmin}" max="{xmax}"/>
      <color r="{int(element.get("style", {}).get("color", "#FF0000")[1:3], 16)}" 
             g="{int(element.get("style", {}).get("color", "#FF0000")[3:5], 16)}" 
             b="{int(element.get("style", {}).get("color", "#FF0000")[5:7], 16)}"/>
      <style thickness="{thickness}" lineStyle="0"/>
    </element>
'''
        
        elif element.get("type") == "slider":
            name = element.get("name", "a")
            value = element.get("value", 0)
            min_val = element.get("min", -10)
            max_val = element.get("max", 10)
            step = element.get("step", 0.1)
            
            xml += f'''    <element type="slider" label="{name}">
      <show object="true" label="true"/>
      <value val="{value}"/>
      <min val="{min_val}"/>
      <max val="{max_val}"/>
      <step val="{step}"/>
      <animation speed="1" repeat="increasing"/>
    </element>
'''
        
        elif element.get("type") == "text":
            text = element.get("text", "")
            x = element.get("position", {}).get("x", 0)
            y = element.get("position", {}).get("y", 0)
            font_size = element.get("style", {}).get("fontSize", 12)
            color = element.get("style", {}).get("color", "#000000")
            
            xml += f'''    <element type="text" label="text">
      <show object="true" label="true"/>
      <text>{text}</text>
      <position x="{x}" y="{y}"/>
      <fontSize>{font_size}</fontSize>
      <color r="{int(element.get("style", {}).get("color", "#000000")[1:3], 16)}" 
             g="{int(element.get("style", {}).get("color", "#000000")[3:5], 16)}" 
             b="{int(element.get("style", {}).get("color", "#000000")[5:7], 16)}"/>
    </element>
'''
        
        # Fecha XML
        xml += '''  </construction>
</geogebra>
'''
        
        return xml
    
    def export_ggb(self, elements: List[Dict], filename: str,
                   metadata: Dict = None) -> str:
        """Exporta arquivo .ggb (XML compactado)"""
        import zipfile
        import tempfile
        import os
        
        xml_content = self.generate_ggb_xml(elements)
        
        # Cria arquivo temporário
        with tempfile.TemporaryDirectory() as tmpdir:
            # Escreve geogebra.xml
            xml_path = os.path.join(tmpdir, "geogebra.xml")
            with open(xml_path, "w", encoding="utf-8") as f:
                f.write(self.generate_ggb_xml(elements))
            
            # Cria .ggb (zip)
            output_path = filename if filename.endswith(".ggb") else filename + ".ggb"
            
            with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zf:
                zf.write(os.path.join(tmpdir, "geogebra.xml"), "geogebra.xml")
            
            # Log
            file_size = os.path.getsize(filename)
            export_log = GeoGebraExport(
                timestamp_utc=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                data_source="geogebra_export.py",
                export_type="ggb",
                filename=filename,
                format="ggb",
                elements_count=len(elements),
                file_size_bytes=os.path.getsize(filename)
            )
            
            self.export_log.append(asdict(export_log))
            
            return filename
    
    def export_xml(self, elements: List[Dict], filename: str) -> str:
        """Exporta apenas XML (para visualização/debug)"""
        xml_content = self.generate_ggb_xml(elements)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_content)
        
        print(f"[GeoGebra] XML exportado para {filename}")
        return filename
    
    def points_from_data(self, x_data: List[float], y_data: List[float],
                         prefix: str = "P", color: str = "#0000FF",
                         size: int = 5) -> List[Dict]:
        """Converte dados numéricos em pontos GeoGebra"""
        elements = []
        for i, (x, y) in enumerate(zip(x_data, y_data)):
            elements.append({
                "type": "point",
                "label": f"{prefix}{i}",
                "coords": {"x": x, "y": y, "z": 0},
                "style": {
                    "color": color,
                    "size": size,
                    "pointStyle": 0
                }
            })
        return elements
    
    def function_from_data(self, expression: str, x_min: float = -10,
                           x_max: float = 10, color: str = "#FF0000",
                           thickness: int = 2) -> Dict:
        """Cria elemento função"""
        return {
            "type": "function",
            "expression": expression,
            "domain": {"min": x_min, "max": x_max},
            "style": {
                "color": color,
                "thickness": thickness,
                "lineStyle": 0
            }
        }
    
    def create_koch_curve_elements(self, iterations: int = 3,
                                    color: str = "#0000FF") -> List[Dict]:
        """Gera elementos para curva de Koch"""
        # Gera pontos da curva de Koch
        def koch_curve(points, level):
            if level == 0:
                return points
            new_points = []
            for i in range(len(points)-1):
                p1 = points[i]
                p2 = points[i+1]
                dx = p2[0] - p1[0]
                dy = p2[1] - p1[1]
                
                p_a = (p1[0] + dx/3, p1[1] + dy/3)
                p_c = (p1[0] + 2*dx/3, p1[1] + 2*dy/3)
                
                angle = math.atan2(dy, dx) + math.pi/3
                p_b = (p_a[0] + (dx/3)*math.cos(angle) - (dy/3)*math.sin(angle),
                       p_a[1] + (dx/3)*math.sin(angle) + (dy/3)*math.cos(angle))
                
                new_points.extend([p1, p_a, p_b, p_c])
            new_points.append(points[-1])
            return new_points
        
        # Triângulo inicial
        points = [(0, 0), (1, 0), (0.5, math.sqrt(3)/2), (0, 0)]
        
        for i in range(iterations):
            points = koch_curve(points, 1)
        
        # Cria elementos polyline
        elements = []
        points_list = [f"P{i}" for i in range(len(points))]
        
        # Pontos
        for i, (x, y) in enumerate(points):
            elements.append({
                "type": "point",
                "label": f"K{i}",
                "coords": {"x": x, "y": y, "z": 0},
                "style": {"color": color, "size": 3}
            })
        
        # Polilinha
        elements.append({
            "type": "polyline",
            "points": [f"K{i}" for i in range(len(points))],
            "style": {"color": color, "thickness": 2, "fill": False}
        })
        
        return elements

def main():
    print("=" * 70)
    print("GEOGEBRA EXPORT — Exportação para GeoGebra")
    print("=" * 70)
    
    exporter = GeoGebraExporter()
    
    # Exemplo 1: Pontos de dados
    print("\n--- Exemplo 1: Pontos de dados ---")
    x_data = np.linspace(0, 10, 20)
    y_data = np.sin(x_data) * np.exp(-x_data/5)
    
    elements = exporter.points_from_data(x_data, y_data, prefix="D", 
                                          color="#0000FF", size=4)
    
    # Adiciona função teórica
    elements.append(exporter.function_from_data(
        "sin(x)*exp(-x/5)", x_min=0, x_max=10,
        color="#FF0000", thickness=2))
    
    # Exporta
    filename = "damped_oscillation.ggb"
    exporter.export_ggb(elements, filename)
    
    # Exemplo 2: Curva de Koch
    print("\n--- Exemplo 2: Curva de Koch ---")
    koch_elements = exporter.create_koch_curve_elements(3, "#0066CC")
    exporter.export_ggb(koch_elements, "koch_curve.ggb")
    
    # Exemplo 3: Exporta XML apenas
    print("\n--- Exemplo 3: Exporta XML ---")
    xml_content = exporter.generate_ggb_xml(elements)
    with open("damped_oscillation.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
    print("XML exportado para damped_oscillation.xml")
    
    print("\n" + "=" * 70)
    print("EXPORTAÇÃO CONCLUÍDA")
    print("=" * 70)

if __name__ == "__main__":
    main()