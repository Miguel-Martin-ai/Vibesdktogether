# VibeSDK Together AI Integration - Configuration Guide

## Environment Setup

### 1. API Key Configuration

You can configure your Together AI API key in two ways:

#### Option A: Environment Variable (Recommended)
```bash
export TOGETHER_API_KEY="your-api-key-here"
```

#### Option B: Direct in Code
```python
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key="your-api-key-here")
```

### 2. Model Selection Guide

Different models are optimized for different tasks:

#### Code Generation
- **DeepSeek Coder 33B**: Best for code generation and implementation
- **Llama 3 70B**: Good for general coding tasks

#### Chat and Conversation
- **Llama 3 70B Chat**: Best for conversational interactions
- **Llama 3 8B Chat**: Faster, good for simple queries

#### Multi-purpose
- **Mixtral 8x7B**: Balanced performance for various tasks
- **Qwen 2 72B**: Strong multilingual support

## Integration with VibeSDK

### Full Configuration Example

```python
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

# Initialize provider
provider = TogetherAIProvider()

# Get agent configuration
agent_config = VibeSDKTogetherConfig.get_default_agent_config()

# Use for specific VibeSDK actions
def execute_code_generation(user_request):
    config = agent_config['phaseImplementation']
    model = config['name'].replace('together/', '')
    
    response = provider.chat_completion(
        model=model,
        messages=[
            {"role": "system", "content": "You are an expert code generator."},
            {"role": "user", "content": user_request}
        ],
        temperature=config['temperature'],
        max_tokens=config.get('max_tokens', 4096)
    )
    
    return response['choices'][0]['message']['content']
```

### Custom Agent Configuration

```python
from vibesdk_together import VibeSDKTogetherConfig

# Create custom configuration for specific needs
custom_agent_config = {
    "codeGeneration": VibeSDKTogetherConfig.create_model_config(
        model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
        max_tokens=16384,
        temperature=0.1,  # Lower temperature for more deterministic code
        fallback_model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT
    ),
    "documentation": VibeSDKTogetherConfig.create_model_config(
        model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT,
        max_tokens=4096,
        temperature=0.7,  # Higher temperature for more creative writing
    ),
    "codeReview": VibeSDKTogetherConfig.create_model_config(
        model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT,
        max_tokens=2048,
        temperature=0.3,  # Balanced for analysis
    )
}
```

## Performance Optimization

### 1. Token Management

```python
# For code generation, use higher token limits
provider.chat_completion(
    model="deepseek-ai/deepseek-coder-33b-instruct",
    messages=messages,
    max_tokens=8192  # Large enough for complete code files
)

# For quick responses, use lower limits
provider.chat_completion(
    model="meta-llama/Llama-3-8b-chat-hf",
    messages=messages,
    max_tokens=512  # Quick, focused responses
)
```

### 2. Temperature Settings

```python
# Deterministic code generation
temperature=0.1  # More consistent, less creative

# Creative content generation
temperature=0.8  # More varied, creative outputs

# Balanced general use
temperature=0.7  # Good middle ground
```

### 3. Model Selection Strategy

```python
# Fast responses - use smaller models
fast_model = VibeSDKTogetherConfig.LLAMA_3_8B_CHAT

# High quality - use larger models
quality_model = VibeSDKTogetherConfig.LLAMA_3_70B_CHAT

# Code-specific tasks - use specialized models
code_model = VibeSDKTogetherConfig.DEEPSEEK_CODER_33B
```

## Error Handling Best Practices

```python
from vibesdk_together import TogetherAIProvider

def robust_completion(provider, model, messages, max_retries=3):
    """Execute completion with retry logic"""
    for attempt in range(max_retries):
        try:
            response = provider.chat_completion(
                model=model,
                messages=messages
            )
            return response
        except RuntimeError as e:
            if attempt < max_retries - 1:
                print(f"Attempt {attempt + 1} failed, retrying...")
                continue
            else:
                raise
    
# Usage
provider = TogetherAIProvider()
response = robust_completion(
    provider,
    "meta-llama/Llama-3-8b-chat-hf",
    [{"role": "user", "content": "Hello"}]
)
```

## Rate Limiting

Together AI has rate limits. Implement proper handling:

```python
import time

def rate_limited_request(provider, model, messages, delay=1.0):
    """Make request with rate limiting"""
    response = provider.chat_completion(
        model=model,
        messages=messages
    )
    time.sleep(delay)  # Wait before next request
    return response
```

## Testing Configuration

```python
# Test your connection before use
provider = TogetherAIProvider()
result = provider.test_connection()

if result['success']:
    print(f"✓ Connected successfully")
    print(f"  Response time: {result['response_time']:.2f}ms")
    print(f"  Available models: {result['models_count']}")
else:
    print(f"✗ Connection failed: {result['error']}")
```

## Production Deployment

### 1. Security
- Never commit API keys to version control
- Use environment variables or secret management services
- Rotate API keys regularly

### 2. Monitoring
```python
import time

def monitored_completion(provider, model, messages):
    """Completion with monitoring"""
    start_time = time.time()
    
    try:
        response = provider.chat_completion(model=model, messages=messages)
        duration = time.time() - start_time
        
        # Log metrics
        print(f"Request completed in {duration:.2f}s")
        return response
    except Exception as e:
        duration = time.time() - start_time
        print(f"Request failed after {duration:.2f}s: {e}")
        raise
```

### 3. Caching
```python
import hashlib
import json

cache = {}

def cached_completion(provider, model, messages):
    """Completion with caching"""
    # Create cache key
    cache_key = hashlib.md5(
        json.dumps({"model": model, "messages": messages}).encode()
    ).hexdigest()
    
    if cache_key in cache:
        return cache[cache_key]
    
    response = provider.chat_completion(model=model, messages=messages)
    cache[cache_key] = response
    return response
```

## Troubleshooting

### Common Issues

1. **API Key Not Found**
   ```
   ValueError: API key must be provided or set in TOGETHER_API_KEY environment variable
   ```
   Solution: Set `TOGETHER_API_KEY` environment variable

2. **Connection Timeout**
   ```
   RuntimeError: Together AI API request failed: Connection timeout
   ```
   Solution: Increase timeout or check network connection
   ```python
   provider = TogetherAIProvider(api_key="key", timeout=120)
   ```

3. **Rate Limit Exceeded**
   Solution: Implement exponential backoff and rate limiting

## Additional Resources

- [Together AI Documentation](https://docs.together.ai/)
- [VibeSDK GitHub](https://github.com/cloudflare/vibesdk)
- [Together AI Model List](https://docs.together.ai/docs/models)
