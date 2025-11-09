# Uso Dual: Python y Node.js

Este paquete se puede usar de **dos maneras**:

## Opción 1: Uso Directo en Python (Recomendado)

### Instalación
```bash
pip install -r requirements.txt
pip install .
```

### Uso
```python
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key="your-key")
response = provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[{"role": "user", "content": "¡Hola!"}]
)
```

## Opción 2: Uso desde Node.js (Wrapper)

### Instalación
```bash
# Instalar dependencias de Python
npm run install:python

# O manualmente
pip install -r requirements.txt
pip install -e .
```

### Uso
```javascript
import { TogetherAIProvider, Models } from './index.js';

const provider = new TogetherAIProvider('your-api-key');
const response = await provider.chatCompletion({
    model: Models.LLAMA_3_8B_CHAT,
    messages: [{ role: 'user', content: '¡Hola!' }]
});

console.log(response.choices[0].message.content);
```

## Scripts NPM Disponibles

```bash
npm run install:python   # Instalar dependencias Python
npm run build            # Construir paquete Python
npm run test             # Ejecutar tests
npm run demo             # Ejecutar demo Python
npm run check            # Verificar instalación
npm run clean            # Limpiar archivos generados
npm run help             # Mostrar ayuda
```

## Ejemplos

### Python
```bash
python examples.py
python demo_together_integration.py
```

### Node.js
```bash
node example-nodejs.js
```

## Requisitos

- **Python**: 3.7 o superior
- **Node.js**: 14.0 o superior (solo si usas el wrapper)
- **API Key**: Obtener de https://api.together.xyz

## Configuración

```bash
export TOGETHER_API_KEY="your-api-key-here"
```

## Documentación

- `README.md` - Documentación principal
- `QUICKSTART.md` - Inicio rápido (inglés)
- `INICIO_RAPIDO_ES.md` - Inicio rápido (español)
- `CONFIGURATION.md` - Configuración avanzada
- `DEPLOYMENT.md` - Guía de despliegue

## Notas Importantes

1. **El paquete base es Python**: El wrapper de Node.js ejecuta Python internamente
2. **Performance**: Para mejor rendimiento, usa Python directamente
3. **Compatibilidad**: El wrapper funciona en cualquier sistema con Python y Node.js
