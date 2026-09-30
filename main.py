import os
import re
import time
from typing import Any, Dict, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Universal Vault Validator",
    description=(
        "Motor de validación modular en Python puro + Puente AI local"
    ),
    version="2.0.0",
)


# Estructuras de datos para las peticiones
class VaultItem(BaseModel):
    content: str
    frontmatter: Optional[Dict[str, Any]] = {}
    path: Optional[str] = ""


class AIRequest(BaseModel):
    content: str
    prompt: Optional[str] = (
        "Realiza una auditoría semántica avanzada y sugiere mejoras para esta nota."
    )
    model: Optional[str] = os.getenv(
        "DEFAULT_AI_MODEL", "qwen-local"
    )  # Dinámico desde variable de entorno


# Configuración mediante variables de entorno (Evita hardcodear URLs o puertos)
LOCAL_LLM_URL = os.getenv(
    "LOCAL_LLM_URL", "http://localhost:11434/api/generate"
)


def detect_note_type(content: str, frontmatter: Dict[str, Any]) -> str:
    """Detecta automáticamente el tipo de nota si no está explícito en el frontmatter."""
    if "type" in frontmatter:
        return frontmatter["type"].lower()

    # Heurísticas en Python puro
    if (
        "```" in content
        or "def " in content
        or "class " in content
        or "import " in content
    ):
        return "code"
    elif (
        "## Referencias" in content
        or "## Fuentes" in content
        or "http" in content
    ):
        return "research"
    elif "## Estado" in content or "status:" in content:
        return "technical"

    return "general"


@app.post("/audit-vault-item")
def audit_vault_item(item: VaultItem):
    """Endpoint universal de validación rápida en Python puro (<50ms).

    Valida estructura Markdown, consistencia de enlaces y metadatos modulares.
    """
    start_time = time.time()
    issues = []

    # 1. Detección de tipo
    note_type = detect_note_type(item.content, item.frontmatter)

    # 2. Validación estructural básica
    if not item.content or not item.content.strip():
        issues.append("La nota está vacía.")

    if not item.content.startswith("#") and "title:" not in item.frontmatter:
        issues.append(
            "Falta un título principal (# Título) o metadatos de título."
        )

    # 3. Extracción y análisis de enlaces internos estilo Obsidian [[Link]]
    internal_links = re.findall(r"\[\[(.*?)\]\]", item.content)

    # 4. Reglas modulares según el tipo detectado
    if note_type == "code":
        if "```" not in item.content:
            issues.append(
                "[Modo Code] La nota está etiquetada como código pero no contiene"
                " bloques Markdown (```)."
            )
    elif note_type == "research":
        if len(internal_links) == 0:
            issues.append(
                "[Modo Research] Se recomienda incluir al menos un enlace interno a"
                " fuentes de la bóveda."
            )
    elif note_type == "technical":
        if (
            not item.frontmatter.get("status")
            and not item.frontmatter.get("estado")
        ):
            issues.append(
                "[Modo Technical] Falta el campo de control 'status' en el"
                " frontmatter."
            )

    execution_time = (time.time() - start_time) * 1000  # Convertir a milisegundos

    return {
        "status": "success",
        "validator": "pure_python_engine",
        "detected_type": note_type,
        "metrics": {
            "internal_links_found": len(internal_links),
            "execution_time_ms": round(execution_time, 2),
        },
        "issues": issues,
    }


@app.post("/audit-vault-ai")
def audit_vault_ai(req: AIRequest):
    """Endpoint de razonamiento profundo.

    Conecta con el servidor de inferencia local para refactorización o auditorías.
    """
    full_prompt = (
        f"{req.prompt}\n\n"
        f"--- CONTENIDO DE LA NOTA ---\n"
        f"{req.content}\n"
        f"-----------------------------"
    )

    payload = {
        "model": req.model,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.1  # Baja temperatura para consistencia técnica
        },
    }

    try:
        import requests

        response = requests.post(LOCAL_LLM_URL, json=payload, timeout=60)
        if response.status_code != 200:
            raise HTTPException(
                status_code=502, detail="Error en el servidor de inferencia local."
            )

        res_data = response.json()
        return {
            "status": "success",
            "model_used": req.model,
            "ai_analysis": res_data.get(
                "response", "No se obtuvo respuesta del modelo."
            ),
        }
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=503,
            detail=f"No se pudo conectar con el motor local: {str(e)}",
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
