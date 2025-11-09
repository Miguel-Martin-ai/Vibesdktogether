# 🚀 Inicio Rápido - 2 Minutos

## Para Python

```bash
# 1. Instalar
pip install -r requirements.txt
pip install .

# 2. Configurar API key
export TOGETHER_API_KEY="tu-api-key"

# 3. Usar
python -c "
from vibesdk_together import TogetherAIProvider
provider = TogetherAIProvider()
print(provider.test_connection())
"
```

## Para Node.js

```bash
# 1. Instalar
npm run install:python

# 2. Configurar API key
export TOGETHER_API_KEY="tu-api-key"

# 3. Ejecutar ejemplo
node example-nodejs.js
```

## Verificar Instalación

```bash
npm run verify
# o
bash verify.sh
```

## Obtener Ayuda

```bash
npm run help
```

## Más Información

- Python: Ver `INICIO_RAPIDO_ES.md`
- Node.js: Ver `USO_DUAL.md`
- Completo: Ver `README.md`
