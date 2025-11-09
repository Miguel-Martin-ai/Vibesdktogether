# Guía de Inicio Rápido en Español

## ¿Qué es esto?

Este es un SDK de Python que te permite usar los modelos de IA de Together AI con la configuración de VibeSDK.

## Instalación

```bash
# Instalar dependencias
pip install -r requirements.txt

# O instalar el paquete completo
pip install .
```

## Configuración

### 1. Obtén tu API Key de Together AI

1. Ve a https://api.together.xyz
2. Crea una cuenta (gratis)
3. Genera una API key en la sección de configuración

### 2. Configura la API Key

**Opción A: Variable de entorno (Recomendado)**
```bash
export TOGETHER_API_KEY="tu-api-key-aqui"
```

**Opción B: En el código**
```python
provider = TogetherAIProvider(api_key="tu-api-key-aqui")
```

## Uso Básico

### Ejemplo 1: Chat Simple

```python
from vibesdk_together import TogetherAIProvider

# Inicializar el provider
provider = TogetherAIProvider()

# Hacer una consulta
response = provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {"role": "system", "content": "Eres un asistente útil que habla español."},
        {"role": "user", "content": "¿Qué es la inteligencia artificial?"}
    ]
)

# Mostrar la respuesta
print(response['choices'][0]['message']['content'])
```

### Ejemplo 2: Generar Código

```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

provider = TogetherAIProvider()

# Usar el modelo optimizado para código
response = provider.chat_completion(
    model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
    messages=[
        {"role": "user", "content": "Escribe una función en Python para calcular números primos"}
    ],
    temperature=0.2  # Temperatura baja para código más determinista
)

print(response['choices'][0]['message']['content'])
```

### Ejemplo 3: Usar Configuración de VibeSDK

```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

provider = TogetherAIProvider()

# Obtener la configuración predefinida para VibeSDK
config = VibeSDKTogetherConfig.get_default_agent_config()

# Usar configuración para generación de código
code_config = config['phaseImplementation']
modelo = code_config['name'].replace('together/', '')

response = provider.chat_completion(
    model=modelo,
    messages=[{"role": "user", "content": "Crea una API REST con FastAPI"}],
    temperature=code_config['temperature'],
    max_tokens=code_config['max_tokens']
)

print(response['choices'][0]['message']['content'])
```

## Modelos Disponibles

El SDK incluye acceso a estos modelos de Together AI:

| Modelo | Uso Recomendado | Velocidad |
|--------|----------------|-----------|
| **Llama 3 8B Chat** | Respuestas rápidas, tareas simples | ⚡⚡⚡ |
| **Llama 3 70B Chat** | Alta calidad, tareas complejas | ⚡⚡ |
| **DeepSeek Coder 33B** | Generación y revisión de código | ⚡⚡ |
| **Mixtral 8x7B** | Uso general, balanceado | ⚡⚡ |
| **Qwen 2 72B** | Soporte multilingüe | ⚡⚡ |

### Cómo Usar los Modelos

```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

provider = TogetherAIProvider()

# Opción 1: Usar el identificador del modelo directamente
response = provider.chat_completion(
    model="meta-llama/Llama-3-70b-chat-hf",
    messages=[{"role": "user", "content": "Hola"}]
)

# Opción 2: Usar las constantes predefinidas
response = provider.chat_completion(
    model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT,
    messages=[{"role": "user", "content": "Hola"}]
)
```

## Funciones Disponibles

### TogetherAIProvider

```python
# 1. Chat Completion (Recomendado)
response = provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": "Tu pregunta"}],
    max_tokens=2048,
    temperature=0.7
)

# 2. Text Completion (Para prompts simples)
response = provider.completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    prompt="Completa esta frase: La IA es",
    max_tokens=100
)

# 3. Listar Modelos Disponibles
modelos = provider.list_models()
for modelo in modelos[:5]:
    print(modelo['id'])

# 4. Probar Conexión
resultado = provider.test_connection()
if resultado['success']:
    print(f"✓ Conectado en {resultado['response_time']:.2f}ms")
```

### VibeSDKTogetherConfig

```python
# Obtener configuración completa de VibeSDK
config = VibeSDKTogetherConfig.get_default_agent_config()

# Acciones disponibles:
# - templateSelection: Selección de plantillas
# - blueprint: Planificación de proyecto
# - projectSetup: Configuración inicial
# - phaseGeneration: Generación de fases
# - phaseImplementation: Implementación de código
# - codeReview: Revisión de código
# - conversationalResponse: Respuestas conversacionales
# ... y más

# Crear configuración personalizada
custom_config = VibeSDKTogetherConfig.create_model_config(
    model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
    max_tokens=8192,
    temperature=0.1,
    fallback_model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT
)
```

## Parámetros Importantes

### Temperature (Temperatura)
- **0.1-0.3**: Respuestas más consistentes y deterministas (ideal para código)
- **0.5-0.7**: Balanceado (uso general)
- **0.8-1.0**: Más creativo y variado (ideal para contenido creativo)

### Max Tokens
- Número máximo de tokens a generar
- 1 token ≈ 0.75 palabras en español
- Ejemplos:
  - 512 tokens ≈ 380 palabras
  - 2048 tokens ≈ 1500 palabras
  - 8192 tokens ≈ 6000 palabras

## Ejemplos Prácticos

### Asistente de Programación

```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

provider = TogetherAIProvider()

def asistente_codigo(pregunta):
    response = provider.chat_completion(
        model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
        messages=[
            {"role": "system", "content": "Eres un experto programador que ayuda con código Python."},
            {"role": "user", "content": pregunta}
        ],
        temperature=0.2,
        max_tokens=4096
    )
    return response['choices'][0]['message']['content']

# Usar
codigo = asistente_codigo("Crea una función para validar emails")
print(codigo)
```

### Chat Interactivo

```python
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider()
conversacion = []

def chat(mensaje_usuario):
    conversacion.append({"role": "user", "content": mensaje_usuario})
    
    response = provider.chat_completion(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[
            {"role": "system", "content": "Eres un asistente amigable."},
            *conversacion
        ]
    )
    
    respuesta = response['choices'][0]['message']['content']
    conversacion.append({"role": "assistant", "content": respuesta})
    
    return respuesta

# Usar
print(chat("Hola, ¿cómo estás?"))
print(chat("¿Qué sabes sobre Python?"))
```

## Solución de Problemas

### Error: "API key must be provided"
**Solución**: Configura la variable de entorno:
```bash
export TOGETHER_API_KEY="tu-api-key"
```

### Error: "Connection timeout"
**Solución**: Aumenta el timeout:
```python
provider = TogetherAIProvider(api_key="tu-key", timeout=120)
```

### Error: "Rate limit exceeded"
**Solución**: Espera unos segundos entre requests o implementa delays:
```python
import time
time.sleep(1)  # Esperar 1 segundo entre requests
```

## Ejecutar los Ejemplos

```bash
# Ver todos los ejemplos disponibles
python examples.py

# Ejecutar el demo completo
python demo_together_integration.py

# Ejecutar los tests
python -m unittest test_vibesdk_together.py -v
```

## Recursos Adicionales

- **Documentación completa**: Ver `README.md`
- **Guía de configuración**: Ver `CONFIGURATION.md`
- **Guía de despliegue**: Ver `DEPLOYMENT.md`
- **Together AI**: https://api.together.xyz
- **VibeSDK**: https://github.com/cloudflare/vibesdk

## Soporte

Para preguntas o problemas:
1. Revisa la documentación en los archivos `.md`
2. Ejecuta `python demo_together_integration.py` para verificar la configuración
3. Revisa los ejemplos en `examples.py`
4. Crea un issue en el repositorio de GitHub

---

**¡Todo está listo para usar! 🚀**

Simplemente obtén tu API key de Together AI y empieza a usar los modelos de IA más avanzados con este SDK.
