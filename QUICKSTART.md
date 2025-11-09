# Quick Start Guide - VibeSDK Together AI Integration

This guide will get you up and running with Together AI and VibeSDK in 5 minutes.

## Step 1: Get Your Together AI API Key

1. Go to [Together AI](https://api.together.xyz)
2. Sign up for a free account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy your API key

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Set Up Your Environment

Choose one of these methods:

### Method A: Environment Variable (Recommended)
```bash
export TOGETHER_API_KEY="your-api-key-here"
```

### Method B: In Code
```python
# You'll pass the API key directly in your code
```

## Step 4: Try Your First Request

Create a file called `quick_test.py`:

```python
from vibesdk_together import TogetherAIProvider

# Initialize (uses TOGETHER_API_KEY env var)
provider = TogetherAIProvider()

# Or initialize with API key directly
# provider = TogetherAIProvider(api_key="your-api-key-here")

# Test the connection
result = provider.test_connection()
print(f"Connection: {'✓ Success' if result['success'] else '✗ Failed'}")
print(f"Response time: {result.get('response_time', 0):.2f}ms")
print(f"Models available: {result.get('models_count', 0)}")

# Make your first chat request
response = provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in a friendly way!"}
    ]
)

print("\nResponse:", response['choices'][0]['message']['content'])
```

Run it:
```bash
python quick_test.py
```

## Step 5: Use VibeSDK Configuration

For VibeSDK-compatible configurations:

```python
from vibesdk_together import VibeSDKTogetherConfig, TogetherAIProvider

# Get default agent configuration
config = VibeSDKTogetherConfig.get_default_agent_config()

# Initialize provider
provider = TogetherAIProvider()

# Use for code generation
code_config = config['phaseImplementation']
model_name = code_config['name'].replace('together/', '')

response = provider.chat_completion(
    model=model_name,
    messages=[
        {"role": "system", "content": "You are an expert Python developer."},
        {"role": "user", "content": "Write a function to calculate factorial"}
    ],
    temperature=code_config['temperature'],
    max_tokens=code_config.get('max_tokens', 4096)
)

print(response['choices'][0]['message']['content'])
```

## Common Use Cases

### 1. Code Generation
```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

provider = TogetherAIProvider()

response = provider.chat_completion(
    model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
    messages=[
        {"role": "user", "content": "Create a REST API endpoint for user login"}
    ],
    temperature=0.2,  # Lower temperature for more consistent code
    max_tokens=8192
)
```

### 2. Code Review
```python
code_to_review = """
def calculate(x, y):
    return x/y
"""

response = provider.chat_completion(
    model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT,
    messages=[
        {"role": "system", "content": "You are a code reviewer."},
        {"role": "user", "content": f"Review this code:\n{code_to_review}"}
    ],
    temperature=0.3
)
```

### 3. General Chat
```python
response = provider.chat_completion(
    model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT,
    messages=[
        {"role": "user", "content": "Explain async/await in Python"}
    ]
)
```

## Troubleshooting

### "API key must be provided"
- Make sure you've set the `TOGETHER_API_KEY` environment variable
- Or pass `api_key="your-key"` when creating the provider

### "Connection timeout"
- Check your internet connection
- Increase timeout: `TogetherAIProvider(api_key="...", timeout=120)`

### "API request failed"
- Verify your API key is valid
- Check if you have API credits
- Ensure the model name is correct

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [CONFIGURATION.md](CONFIGURATION.md) for advanced configuration
- Run [examples.py](examples.py) to see more usage patterns
- Run tests with `python -m unittest test_vibesdk_together.py`

## Available Models

Quick reference for popular models:

| Model | Use Case | Speed |
|-------|----------|-------|
| `LLAMA_3_8B_CHAT` | Fast responses, simple tasks | ⚡⚡⚡ |
| `LLAMA_3_70B_CHAT` | High-quality responses, complex tasks | ⚡⚡ |
| `DEEPSEEK_CODER_33B` | Code generation and review | ⚡⚡ |
| `MIXTRAL_8X7B` | Multi-purpose, balanced | ⚡⚡ |
| `QWEN_2_72B` | Multilingual support | ⚡⚡ |

## Getting Help

- Check the [examples.py](examples.py) file for more code samples
- Read the [CONFIGURATION.md](CONFIGURATION.md) for optimization tips
- Visit [Together AI Documentation](https://docs.together.ai/)
- Visit [VibeSDK GitHub](https://github.com/cloudflare/vibesdk)

Happy coding! 🚀
