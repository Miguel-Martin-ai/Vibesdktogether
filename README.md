# VibeSDK Together AI Integration

> **⚠️ IMPORTANT**: This is a **Python package**, not a Node.js/TypeScript project. If you're looking for the original Cloudflare VibeSDK (TypeScript), visit https://github.com/cloudflare/vibesdk

A Python SDK adapter that integrates Together AI models with VibeSDK-compatible configuration patterns. This library provides a simple interface for using Together AI's powerful open-source language models in VibeSDK applications.

## Language & Requirements

- **Language**: Python 3.7+
- **Package Manager**: pip (not npm/bun/yarn)
- **Build System**: setuptools/wheel (not vite/webpack)
- **Optional**: Node.js 14+ (for Node.js wrapper)

## Dual Usage Support

This package can be used in **two ways**:

### Option 1: Python (Recommended)
```bash
pip install -r requirements.txt
pip install .
```

### Option 2: Node.js Wrapper
```bash
npm run install:python  # Installs Python package
node example-nodejs.js   # Uses Python via Node.js wrapper
```

See [USO_DUAL.md](USO_DUAL.md) for complete dual-usage documentation.

## Features

- 🚀 Simple Python interface for Together AI API
- 🔧 VibeSDK-compatible configuration patterns
- 🤖 Support for multiple Together AI models (Llama, Mixtral, Qwen, DeepSeek, etc.)
- ⚡ Chat completions and text completions
- 🔍 Model listing and connection testing
- 🎯 Pre-configured agent settings for different tasks
- 🔐 Environment variable support for API keys

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Basic Usage

```python
from vibesdk_together import TogetherAIProvider

# Initialize the provider
provider = TogetherAIProvider(api_key="your-api-key")

# Chat completion
response = provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response['choices'][0]['message']['content'])
```

### Using Environment Variables

```bash
export TOGETHER_API_KEY="your-api-key-here"
```

```python
from vibesdk_together import TogetherAIProvider

# Provider will automatically use TOGETHER_API_KEY
provider = TogetherAIProvider()
```

### VibeSDK-Compatible Configuration

```python
from vibesdk_together import VibeSDKTogetherConfig

# Get default agent configuration
config = VibeSDKTogetherConfig.get_default_agent_config()

# Use specific configurations for different tasks
print(config['phaseImplementation'])  # Code generation config
print(config['codeReview'])           # Code review config
print(config['conversationalResponse']) # Chat config
```

### Custom Model Configuration

```python
from vibesdk_together import VibeSDKTogetherConfig

# Create custom configuration
custom_config = VibeSDKTogetherConfig.create_model_config(
    model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
    max_tokens=8192,
    temperature=0.2,
    fallback_model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT
)
```

## Available Models

The SDK provides easy access to popular Together AI models:

- **Llama 3**: `LLAMA_3_70B_CHAT`, `LLAMA_3_8B_CHAT`
- **Mixtral**: `MIXTRAL_8X7B`
- **Qwen**: `QWEN_2_72B`
- **DeepSeek Coder**: `DEEPSEEK_CODER_33B`

## API Reference

### TogetherAIProvider

Main class for interacting with Together AI API.

#### Methods

- `chat_completion(model, messages, max_tokens=None, temperature=0.7, top_p=0.9, **kwargs)`
  - Create a chat completion
  
- `completion(model, prompt, max_tokens=None, temperature=0.7, top_p=0.9, **kwargs)`
  - Create a text completion
  
- `list_models()`
  - List available models
  
- `test_connection()`
  - Test API connection and get response time

### VibeSDKTogetherConfig

Configuration helper for VibeSDK-compatible settings.

#### Methods

- `create_model_config(model, max_tokens=None, temperature=0.7, fallback_model=None)`
  - Create a model configuration
  
- `get_default_agent_config()`
  - Get complete agent configuration for all VibeSDK actions

## Agent Configuration

The default agent configuration includes optimized settings for:

- **Template Selection**: Fast model selection for templates
- **Blueprint**: Project planning and architecture
- **Project Setup**: Initial project configuration
- **Phase Generation**: Breaking down tasks into phases
- **Phase Implementation**: Code generation and implementation
- **Code Review**: Reviewing and improving code
- **File Regeneration**: Regenerating specific files
- **Screenshot Analysis**: Analyzing UI screenshots
- **Real-time Code Fixer**: Quick code fixes
- **Fast Code Fixer**: Rapid error correction
- **Conversational Response**: Natural language responses
- **Deep Debugger**: In-depth debugging analysis

## Examples

See the `examples.py` file for comprehensive usage examples:

```bash
python examples.py
```

## Testing

Run the test suite:

```bash
python -m unittest test_vibesdk_together.py
```

Or with verbose output:

```bash
python -m unittest test_vibesdk_together.py -v
```

## Requirements

- Python 3.7+
- requests >= 2.31.0

## Getting a Together AI API Key

1. Visit [Together AI](https://api.together.xyz)
2. Sign up for an account
3. Navigate to API Keys section
4. Create a new API key
5. Set it as an environment variable or pass it to the provider

## Configuration Options

### Provider Settings

```python
provider = TogetherAIProvider(
    api_key="your-api-key",      # API key (or use TOGETHER_API_KEY env var)
    base_url="custom-url",        # Custom base URL (optional)
    timeout=60                    # Request timeout in seconds
)
```

### Model Parameters

```python
response = provider.chat_completion(
    model="model-name",           # Together AI model identifier
    messages=[...],               # Chat messages
    max_tokens=2048,              # Maximum tokens to generate
    temperature=0.7,              # Sampling temperature (0-1)
    top_p=0.9,                    # Nucleus sampling parameter
    stream=False                  # Enable streaming (optional)
)
```

## Error Handling

```python
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key="your-api-key")

try:
    response = provider.chat_completion(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": "Hello"}]
    )
except RuntimeError as e:
    print(f"API request failed: {e}")
except ValueError as e:
    print(f"Configuration error: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built for integration with [Cloudflare VibeSDK](https://github.com/cloudflare/vibesdk)
- Powered by [Together AI](https://www.together.ai/)

## Support

For issues and questions:
- Create an issue in this repository
- Check the [Together AI documentation](https://docs.together.ai/)
- Review the [VibeSDK documentation](https://github.com/cloudflare/vibesdk)
