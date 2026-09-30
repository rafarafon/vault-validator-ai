# ⚡ Universal Vault Validator & Local AI Bridge

Motor de validación modular en Python puro y FastAPI con integración a modelos de lenguaje locales (Ollama/Qwen). Diseñado para auditar notas Markdown, comprobar metadatos y realizar análisis semánticos profundos.

---

## 🚀 Características

- **Validación estática ultra rápida (<50ms):** Comprueba sintaxis, estructura y enlaces estilo Obsidian (`[[Link]]`) en Python puro sin sobrecargar la GPU.
- **Detección heurística de contenido:** Clasifica automáticamente las notas según su estructura en tres modos: `code`, `research` o `technical`.
- **Puente con IA local:** Endpoint dedicado para auditorías semánticas avanzadas con modelos locales ejecutados en Ollama, vLLM o LM Studio.
- **Configuración mediante entorno:** URLs y modelos dinámicos controlados por variables de entorno.

---

## 📦 Requisitos Previos

- **Python 3.9+** instalado en el sistema.
- Un servidor de inferencia local activo (por ejemplo, **Ollama** corriendo en `http://localhost:11434`).

---

## 🛠️ Instalación paso a paso

### 1. Clonar el repositorio
Abre tu terminal y ejecuta:

```bash
git clone [https://github.com/rafarafons/vault-validator-ai.git](https://github.com/rafarafons/vault-validator-ai.git)
cd vault-validator-ai
