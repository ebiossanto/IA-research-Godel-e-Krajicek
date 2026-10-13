#!/usr/bin/env python3
"""
Fractal Visualization Engine — Visualização e exportação para GeoGebra/TikZ
Para o Terminal-Laboratório
"""

import json
import math
import numpy as np
from typing import List, Dict, Tuple, Optional, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from itertools import product

@dataclass
class VisualizationData:
    timestamp_utc: str
    data_source: str
    metric_type: str
    plot_type: str
    tikz_code: str
    geogebra_xml: str
    png_base64: Optional[str]

class FractalVisualizationEngine:
    """
    Motor de visualização e exportação para GeoGebra/TikZ
    Para visualização de dados fractais no Terminal-Laboratório
    """
    
    def __init__(self):
        self.telemetry_log = []
    
    def generate_tikz_2d_plot(self, x_data: List[float], y_data: List[float],
                               title: str = "Fractal Plot",
                               xlabel: str = "x", ylabel: str = "y",
                               color: str = "blue", mark: str = "*") -> str:
        """
        Gera código TikZ para gráfico 2D
        """
        if len(x_data) != len(y_data):
            raise ValueError("x_data and y_data must have same length")
        
        # Normaliza para coordenadas TikZ (0-10, 0-7)
        x_min, x_max = min(x_data), max(x_data)
        y_min, y_max = min(y_data), max(y_data)
        
        def norm_x(x):
            return 1 + 8 * (x - min(x_data)) / (max(x_data) - min(x_data) + 1e-9)
        def norm_y(y):
            return 1 + 5 * (y - min(y_data)) / (max(y_data) - min(y_data) + 1e-9)
        
        coordinates = " ".join(f"({norm_x(x):.3f},{norm_y(y):.3f})" 
                               for x, y in zip(x_data, y_data))
        
        tikz = f"""
\\begin{{tikzpicture}}[scale=1]
\\begin{{axis}}[
    title={{{title}}},
    xlabel={{{xlabel}}},
    ylabel={{{ylabel}}},
    xmin=0, xmax=10,
    ymin=0, ymax=6,
    grid=major,
    width=12cm,
    height=8cm,
]
\\addplot[{color}, mark={mark}, only marks, mark size=1.5pt] coordinates {{
{coordinates}
}};
\\end{{axis}}
\\end{{tikzpicture}}
"""
        return tikz
    
    def generate_tikz_3d_plot(self, x_data: List[float], y_data: List[float], 
                               z_data: List[float],
                               title: str = "3D Fractal Plot") -> str:
        """Gera código TikZ para gráfico 3D"""
        if not (len(x_data) == len(y_data) == len(z_data)):
            raise ValueError("All data arrays must have same length")
        
        # Normaliza para coordenadas TikZ 3D
        x_min, x_max = min(x_data), max(x_data)
        y_min, y_max = min(y_data), max(y_data)
        z_min, z_max = min(z_data), max(z_data)
        
        def norm_x(x): return 1 + 8 * (x - min(x_data)) / (max(x_data) - min(x_data) + 1e-9)
        def norm_y(y): return 1 + 8 * (y - min(y_data)) / (max(y_data) - min(y_data) + 1e-9)
        def norm_z(z): return 1 + 4 * (z - min(z_data)) / (max(z_data) - min(z_data) + 1e-9)
        
        coordinates = " ".join(f"({norm_x(x):.3f},{norm_y(y):.3f},{norm_z(z):.3f})" 
                               for x, y, z in zip(x_data, y_data, z_data))
        
        tikz = f"""
\\begin{{tikzpicture}}[scale=1]
\\begin{{axis}}[
    title={{{title}}},
    xlabel={{x}}, ylabel={{y}}, zlabel={{z}},
    view={{60}}{{30}},
    width=12cm, height=10cm,
]
\\addplot3[blue, only marks, mark=*, mark size=1pt] coordinates {{
{coordinates}
}};
\\end{{axis}}
\\end{{tikzpicture}}
"""
        return tikz
    
    def generate_tikz_fractal_curve(self, iterations: int = 5, 
                                     angle: float = math.pi/3,
                                     length: float = 1.0) -> str:
        """
        Gera curva fractal (Koch snowflake style) em TikZ
        """
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
                
                # Pontos intermediários
                p_a = (p1[0] + dx/3, p1[1] + dy/3)
                p_c = (p1[0] + 2*dx/3, p1[1] + 2*dy/3)
                
                # Pico do triângulo
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
        
        # Normaliza para TikZ
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        x_min, x_max = min(x_coords), max(x_coords)
        y_min, y_max = min(y_coords), max(y_coords)
        
        def norm_x(x): return 1 + 8 * (x - x_min) / (x_max - x_min + 1e-9)
        def norm_y(y): return 1 + 5 * (y - min(y_coords)) / (max(y_coords) - min(y_coords) + 1e-9)
        
        coords = " ".join(f"({norm_x(x):.3f},{norm_y(y):.3f})" for x, y in zip(x_coords, y_coords))
        
        tikz = f"""
\\begin{{tikzpicture}}[scale=1]
\\begin{{axis}}[
    title={{Curva de Koch - Iteração {iterations}}},
    xlabel={{x}}, ylabel={{y}},
    axis equal,
    width=12cm, height=10cm,
]
\\addplot[blue, thick] coordinates {{
{coords}
}};
\\end{{axis}}
\\end{{tikzpicture}}
"""
        return tikz
    
    def generate_geogebra_xml(self, x_data: List[float], y_data: List[float],
                               name: str = "FractalData") -> str:
        """
        Gera XML para importação no GeoGebra
        """
        # GeoGebra XML format (simplified)
        xml = f"""<?xml version="1.0" encoding="UTF-8"?>
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
"""
        
        # Adiciona pontos
        for i, (x, y) in enumerate(zip(x_data, y_data)):
            xml += f'    <element type="point" label="P{i}">\n'
            xml += f'      <show object="true" label="true"/>\n'
            xml += f'      <coords x="{x:.6f}" y="{y:.6f}" z="0"/>\n'
            xml += f'    </element>\n'
        
        # Adiciona polilinha conectando pontos
        if len(x_data) > 1:
            points_str = " ".join(f"P{i}" for i in range(len(x_data)))
            xml += f'    <element type="polyline" label="curve">\n'
            xml += f'      <show object="true"/>\n'
            xml += f'      <points>{points_str}</points>\n'
            xml += f'    </element>\n'
        
        xml += """  </construction>
</geogebra>
"""
        return xml
    
    def export_tikz_file(self, tikz_code: str, filename: str):
        """Salva código TikZ em arquivo"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(tikz_code)
        print(f"[Visualization] TikZ salvo em {filename}")
    
    def export_geogebra_file(self, xml_code: str, filename: str):
        """Salva XML GeoGebra em arquivo"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_code)
        print(f"[Visualization] GeoGebra XML salvo em {filename}")

def main():
    print("=" * 70)
    print("FRACTAL VISUALIZATION ENGINE — GeoGebra/TikZ Export")
    print("=" * 70)
    
    viz = FractalVisualizationEngine()
    
    # Teste 1: Gráfico 2D
    print("\n--- Teste 1: Gráfico 2D (TikZ) ---")
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.exp(-x/5)
    tikz_2d = viz.generate_tikz_2d_plot(x.tolist(), y.tolist(), 
                                         title="Damped Oscillation",
                                         xlabel="Time", ylabel="Amplitude")
    print("TikZ 2D gerado (primeiras 500 chars):")
    print(tikz_2d[:500] + "...")
    
    # Teste 2: Gráfico 3D
    print("\n--- Teste 2: Gráfico 3D (TikZ) ---")
    x = np.random.rand(50) * 10
    y = np.random.rand(50) * 10
    z = np.random.rand(50) * 5
    tikz_3d = viz.generate_tikz_3d_plot(x.tolist(), y.tolist(), z.tolist(),
                                         title="Random 3D Points")
    print("TikZ 3D gerado (primeiras 500 chars):")
    print(tikz_3d[:500] + "...")
    
    # Teste 3: Curva de Koch
    print("\n--- Teste 3: Curva de Koch (TikZ) ---")
    tikz_koch = viz.generate_tikz_fractal_curve(iterations=3)
    print("Koch curve TikZ gerado (primeiras 500 chars):")
    print(tikz_koch[:500] + "...")
    
    # Teste 4: Exportação GeoGebra
    print("\n--- Teste 4: Exportação GeoGebra ---")
    x_data = np.linspace(0, 10, 20).tolist()
    y_data = (np.sin(np.array(x_data)) * np.exp(-np.array(x_data)/5)).tolist()
    geogebra_xml = viz.generate_geogebra_xml(x_data, y_data, "DampedSine")
    print("GeoGebra XML gerado (primeiras 500 chars):")
    print(geogebra_xml[:500] + "...")
    
    # Salva arquivos de exemplo
    viz.export_tikz_file(tikz_2d, "example_2d_plot.tex")
    viz.export_tikz_file(tikz_koch, "koch_curve.tex")
    viz.export_geogebra_file(geogebra_xml, "damped_sine.ggb")
    
    print("\n[Visualization] Arquivos de exemplo salvos:")
    print("  - example_2d_plot.tex")
    print("  - koch_curve.tex")
    print("  - damped_sine.ggb")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()