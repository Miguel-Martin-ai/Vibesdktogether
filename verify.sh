#!/bin/bash

echo "╔══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                          ║"
echo "║         VibeSDK Together AI - Verificación de Instalación               ║"
echo "║                                                                          ║"
echo "╚══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check Python
echo "🔍 Verificando Python..."
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1)
    echo "   ✅ $PYTHON_VERSION"
else
    echo "   ❌ Python no encontrado"
    exit 1
fi

# Check pip
echo ""
echo "🔍 Verificando pip..."
if command -v pip &> /dev/null; then
    PIP_VERSION=$(pip --version 2>&1 | head -1)
    echo "   ✅ $PIP_VERSION"
else
    echo "   ❌ pip no encontrado"
    exit 1
fi

# Check if package is installed
echo ""
echo "🔍 Verificando paquete vibesdk-together..."
if python -c "import vibesdk_together" 2>/dev/null; then
    echo "   ✅ Paquete instalado correctamente"
    
    # Test import
    python -c "from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig; print('   ✅ Todas las importaciones funcionan')"
else
    echo "   ⚠️  Paquete no instalado"
    echo "   💡 Ejecuta: pip install -e ."
fi

# Check Node.js (optional)
echo ""
echo "🔍 Verificando Node.js (opcional)..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version 2>&1)
    echo "   ✅ Node.js $NODE_VERSION"
    echo "   ✅ Wrapper de Node.js disponible"
else
    echo "   ⚠️  Node.js no encontrado (opcional, solo para wrapper)"
fi

# Check API key
echo ""
echo "🔍 Verificando API key..."
if [ -n "$TOGETHER_API_KEY" ]; then
    echo "   ✅ TOGETHER_API_KEY configurada"
else
    echo "   ⚠️  TOGETHER_API_KEY no configurada"
    echo "   💡 Configura con: export TOGETHER_API_KEY='tu-api-key'"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📚 Siguiente paso:"
echo "   • Para usar en Python: python examples.py"
echo "   • Para usar en Node.js: node example-nodejs.js"
echo "   • Para ver ayuda: npm run help"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
