⚡ Universal Vault Validator & Local AI Bridge
Motor de validación modular en Python puro y FastAPI con integración a modelos de lenguaje locales (Ollama/Qwen). Diseñado para auditar notas Markdown, comprobar metadatos y realizar análisis semánticos profundos.
🚀 Características
 * Validación estática ultra rápida (<50ms): Comprueba sintaxis, estructura y enlaces estilo Obsidian ([[Link]]) en Python puro sin sobrecargar la GPU.
 * Detección heurística de contenido: Clasifica automáticamente las notas según su estructura en tres modos: code, research o technical.
 * Puente con IA local: Endpoint dedicado para auditorías semánticas avanzadas con modelos locales ejecutados en Ollama, vLLM o LM Studio.
 * Configuración mediante entorno: URLs y modelos dinámicos controlados por variables de entorno.
📦 Requisitos Previos
 * Python 3.9+ instalado en el sistema.
 * Un servidor de inferencia local activo (por ejemplo, Ollama corriendo en http://localhost:11434).
🛠️ Instalación paso a paso
1. Clonar el repositorio
Abre tu terminal y ejecuta:
git clone [https://github.com/rafarafons/vault-validator-ai.git](https://github.com/rafarafons/vault-validator-ai.git)
cd vault-validator-ai
2. Crear y activar un entorno virtual (Recomendado)
 * Linux / macOS:
   python3 -m venv venv
   source venv/bin/activate
 * Windows:
   python -m venv venv
   venv\Scripts\activate
3. Instalar las dependencias
Instala los paquetes requeridos con pip:
pip install fastapi uvicorn pydantic requests
⚙ Configuración (Variables de Entorno)
El motor funciona con valores por defecto orientados a Ollama, pero puedes personalizar la URL del motor LLM y el modelo objetivo definiendo las siguientes variables en tu sistema o archivo .env:
| Variable | Valor por defecto | Descripción |
|---|---|---|
| LOCAL_LLM_URL | http://localhost:11434/api/generate | Endpoint del motor de inferencia local. |
| DEFAULT_AI_MODEL | qwen-local | Modelo utilizado por defecto en el endpoint /audit-vault-ai. |
Ejemplo de exportación en Linux/macOS:
export LOCAL_LLM_URL="http://localhost:11434/api/generate"
export DEFAULT_AI_MODEL="qwen2.5-coder"
Ejemplo de exportación en Windows (PowerShell):
$env:LOCAL_LLM_URL="http://localhost:11434/api/generate"
$env:DEFAULT_AI_MODEL="qwen2.5-coder"
🚀 Ejecución del Servidor
Inicia la API con Uvicorn ejecutando directamente:
python main.py
O si prefieres invocar Uvicorn de forma explícita:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
El servidor quedará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).
📖 Documentación interactiva (Swagger UI)
Una vez iniciado el servidor, puedes probar los endpoints navegando a:
 * [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
📌 Ejemplos de Uso de Endpoints
1. /audit-vault-item (POST)
Validación rápida estática en Python puro (<50ms).
Cuerpo del Payload (JSON):
{"content": "# Ejemplo Nota\n\n```python\ndef test():\n    pass\n```", "frontmatter": {"type": "code"}, "path": "proyectos/ejemplo.md"}
2. /audit-vault-ai (POST)
Análisis y razonamiento profundo mediante el modelo local.
Cuerpo del Payload (JSON):
{"content": "Contenido de la nota o documento a analizar...", "prompt": "Realiza una auditoría semántica avanzada y sugiere mejoras.", "model": "qwen-local"}
📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
 sistema.
 * Un servidor de inferencia local activo (por ejemplo, Ollama corriendo en http://localhost:11434).
🛠️ Instalación paso a paso
1. Clonar el repositorio
Abre tu terminal y ejecuta:
git clone https://github.com/rafarafons/vault-validator-ai.git
cd vault-validator-ai

2. Crear y activar un entorno virtual (Recomendado)
 * Linux / macOS:
   python3 -m venv venv
source venv/bin/activate

 * Windows:
   python -m venv venv
venv\Scripts\activate

3. Instalar las dependencias
Instala los paquetes requeridos con pip:
pip install fastapi uvicorn pydantic requests

⚙️️ Configuración (Variables de Entorno)
El motor funciona con valores por defecto orientados a Ollama, pero puedes personalizar la URL del motor LLM y el modelo objetivo definiendo las siguientes variables en tu sistema o archivo .env:
| Variable | Valor por defecto | Descripción |
|---|---|---|
| LOCAL_LLM_URL | http://localhost:11434/api/generate | Endpoint del motor de inferencia local. |
| DEFAULT_AI_MODEL | qwen-local | Modelo utilizado por defecto en el endpoint /audit-vault-ai. |
Ejemplo de exportación en Linux/macOS:
export LOCAL_LLM_URL="http://localhost:11434/api/generate"
export DEFAULT_AI_MODEL="qwen2.5-coder"

Ejemplo de exportación en Windows (PowerShell):
$env:LOCAL_LLM_URL="http://localhost:11434/api/generate"
$env:DEFAULT_AI_MODEL="qwen2.5-coder"

🚀 Ejecución del Servidor
Inicia la API con Uvicorn ejecutando directamente:
python main.py

O si prefieres invocar Uvicorn de forma explícita:
uvicorn main:app --host 127.0.0.1 --port 8000 --reload

El servidor quedará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).
📖 Documentación interactiva (Swagger UI)
Una vez iniciado el servidor, puedes probar los endpoints navegando a:
 * [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
📌 Ejemplos de Uso de Endpoints
1. /audit-vault-item (POST)
Validación rápida estática en Python puro (<50ms).
Cuerpo del Payload (JSON):
{
  "content": "# Ejemplo Nota\n\n```python\ndef test():\n    pass\n```",
  "frontmatter": {
    "type": "code"
  },
  "path": "proyectos/ejemplo.md"
}

2. /audit-vault-ai (POST)
Análisis y razonamiento profundo mediante el modelo local.
Cuerpo del Payload (JSON):
{
  "content": "Contenido de la nota o documento a analizar...",
  "prompt": "Realiza una auditoría semántica avanzada y sugiere mejoras.",
  "model": "qwen-local"
}

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
