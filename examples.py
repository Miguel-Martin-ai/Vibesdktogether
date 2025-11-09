"""
Example usage of VibeSDK Together AI integration
"""

from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig

# Example 1: Basic chat completion
def example_chat():
    """Example of using Together AI for chat completion"""
    print("=== Example 1: Chat Completion ===")
    
    # Initialize the provider
    provider = TogetherAIProvider(api_key="your-api-key-here")
    
    # Create a chat completion
    response = provider.chat_completion(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": "Write a Python function to calculate fibonacci numbers."}
        ],
        max_tokens=512,
        temperature=0.7
    )
    
    print(f"Response: {response['choices'][0]['message']['content']}")
    print()


# Example 2: Text completion
def example_completion():
    """Example of using Together AI for text completion"""
    print("=== Example 2: Text Completion ===")
    
    provider = TogetherAIProvider(api_key="your-api-key-here")
    
    response = provider.completion(
        model="meta-llama/Llama-3-8b-chat-hf",
        prompt="The best programming language for web development is",
        max_tokens=100,
        temperature=0.7
    )
    
    print(f"Response: {response['choices'][0]['text']}")
    print()


# Example 3: List available models
def example_list_models():
    """Example of listing available Together AI models"""
    print("=== Example 3: List Models ===")
    
    provider = TogetherAIProvider(api_key="your-api-key-here")
    
    models = provider.list_models()
    print(f"Found {len(models)} models")
    print("First 5 models:")
    for model in models[:5]:
        print(f"  - {model.get('id', 'Unknown')}")
    print()


# Example 4: Test connection
def example_test_connection():
    """Example of testing the connection to Together AI"""
    print("=== Example 4: Test Connection ===")
    
    provider = TogetherAIProvider(api_key="your-api-key-here")
    
    result = provider.test_connection()
    if result["success"]:
        print(f"✓ Connection successful!")
        print(f"  Response time: {result['response_time']:.2f}ms")
        print(f"  Models available: {result['models_count']}")
    else:
        print(f"✗ Connection failed: {result.get('error', 'Unknown error')}")
    print()


# Example 5: Using VibeSDK-compatible configuration
def example_vibesdk_config():
    """Example of using VibeSDK-compatible configuration"""
    print("=== Example 5: VibeSDK Configuration ===")
    
    # Get default agent configuration
    config = VibeSDKTogetherConfig.get_default_agent_config()
    
    print("Agent configuration for Together AI models:")
    for action, model_config in config.items():
        print(f"  {action}:")
        print(f"    Model: {model_config['name']}")
        print(f"    Temperature: {model_config.get('temperature', 'default')}")
        if 'max_tokens' in model_config:
            print(f"    Max tokens: {model_config['max_tokens']}")
    print()


# Example 6: Custom model configuration
def example_custom_config():
    """Example of creating custom model configuration"""
    print("=== Example 6: Custom Configuration ===")
    
    # Create a custom configuration for code generation
    code_gen_config = VibeSDKTogetherConfig.create_model_config(
        model=VibeSDKTogetherConfig.DEEPSEEK_CODER_33B,
        max_tokens=8192,
        temperature=0.2,
        fallback_model=VibeSDKTogetherConfig.LLAMA_3_70B_CHAT
    )
    
    print("Custom code generation config:")
    print(f"  Model: {code_gen_config['name']}")
    print(f"  Temperature: {code_gen_config['temperature']}")
    print(f"  Max tokens: {code_gen_config['max_tokens']}")
    print(f"  Fallback: {code_gen_config['fallbackModel']}")
    print()


# Example 7: Using environment variable for API key
def example_env_var():
    """Example of using environment variable for API key"""
    print("=== Example 7: Environment Variable ===")
    
    # This will automatically use TOGETHER_API_KEY environment variable
    # export TOGETHER_API_KEY="your-api-key-here"
    try:
        provider = TogetherAIProvider()  # No api_key parameter
        print("✓ Provider initialized using TOGETHER_API_KEY environment variable")
    except ValueError as e:
        print(f"✗ Error: {e}")
        print("  Please set TOGETHER_API_KEY environment variable")
    print()


if __name__ == "__main__":
    print("VibeSDK Together AI Integration - Examples\n")
    
    # Note: These examples require a valid Together AI API key
    # Replace "your-api-key-here" with your actual API key
    # or set the TOGETHER_API_KEY environment variable
    
    print("To run these examples, you need to:")
    print("1. Get a Together AI API key from https://api.together.xyz")
    print("2. Replace 'your-api-key-here' with your actual key")
    print("3. Or set TOGETHER_API_KEY environment variable")
    print()
    
    # Uncomment the examples you want to run:
    # example_chat()
    # example_completion()
    # example_list_models()
    # example_test_connection()
    example_vibesdk_config()
    example_custom_config()
    example_env_var()
