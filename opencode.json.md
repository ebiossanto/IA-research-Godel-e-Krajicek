{  
  "\$schema": "https\://opencode.ai/config.json",  
  "model": "opencode-go/deepseek-v4.1-flash",  
  "instructions": \["AGENTS.md"\],  
  "agent": {  
    "plan": {  
      "description": "Arquiteto Matemático e Lógico (Gödel, Krajíček, Lean 4 e Sistemas Dinâmicos)",  
      "mode": "primary",  
      "model": "opencode-go/deepseek-v4-pro",  
      "tools": {  
        "write": false,  
        "edit": false,  
        "bash": false  
      }  
    },  
    "build": {  
      "description": "Executor Científico (Julia, Python/Z3, Lean 4 e organização de dados)",  
      "mode": "primary",  
      "model": "opencode-go/deepseek-v4.1-flash",  
      "tools": {  
        "write": true,  
        "edit": true,  
        "bash": true  
      }  
    },  
    "referee": {  
      "description": "Auditor implacável (Referee Hostile) que verifica provas, quantificadores e logs sem alterar arquivos",  
      "mode": "subagent",  
      "model": "opencode-go/kimi-k3.1-pro",  
      "prompt": "Você é o Referee Hostile do projeto IA-research-Godel-e-Krajicek. Sua única função é auditar provas matemáticas, códigos em Lean 4 e experimentos numéricos em busca de falhas de quantificadores, confusão entre modelos padrão e não-padrão (Log(M)), hipóteses ocultas ou uso de resultados retraídos (D1-D6). Nunca edite código; apenas aponte falhas críticas e gere o parecer técnico.",  
      "tools": {  
        "write": false,  
        "edit": false,  
        "bash": false  
      }  
    }  
  }  
}

