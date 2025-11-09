"""
Tests for VibeSDK Together AI integration
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
import json
from vibesdk_together import TogetherAIProvider, VibeSDKTogetherConfig


class TestTogetherAIProvider(unittest.TestCase):
    """Test cases for TogetherAIProvider class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.api_key = "test-api-key"
        self.provider = TogetherAIProvider(api_key=self.api_key)
    
    def test_initialization_with_api_key(self):
        """Test provider initialization with API key"""
        provider = TogetherAIProvider(api_key="test-key")
        self.assertEqual(provider.api_key, "test-key")
        self.assertEqual(provider.base_url, "https://api.together.xyz/v1")
    
    def test_initialization_with_custom_base_url(self):
        """Test provider initialization with custom base URL"""
        custom_url = "https://custom.api.together.xyz/v1"
        provider = TogetherAIProvider(api_key="test-key", base_url=custom_url)
        self.assertEqual(provider.base_url, custom_url)
    
    def test_initialization_without_api_key_raises_error(self):
        """Test that initialization without API key raises ValueError"""
        with patch.dict('os.environ', {}, clear=True):
            with self.assertRaises(ValueError):
                TogetherAIProvider()
    
    def test_initialization_with_env_var(self):
        """Test provider initialization using environment variable"""
        with patch.dict('os.environ', {'TOGETHER_API_KEY': 'env-api-key'}):
            provider = TogetherAIProvider()
            self.assertEqual(provider.api_key, "env-api-key")
    
    @patch('requests.request')
    def test_chat_completion_success(self, mock_request):
        """Test successful chat completion"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "Hello! How can I help you?"
                    }
                }
            ]
        }
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        messages = [{"role": "user", "content": "Hello"}]
        response = self.provider.chat_completion(
            model="meta-llama/Llama-3-8b-chat-hf",
            messages=messages
        )
        
        self.assertIn("choices", response)
        self.assertEqual(
            response["choices"][0]["message"]["content"],
            "Hello! How can I help you?"
        )
    
    @patch('requests.request')
    def test_chat_completion_with_parameters(self, mock_request):
        """Test chat completion with custom parameters"""
        mock_response = Mock()
        mock_response.json.return_value = {"choices": []}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        messages = [{"role": "user", "content": "Test"}]
        self.provider.chat_completion(
            model="test-model",
            messages=messages,
            max_tokens=512,
            temperature=0.5,
            top_p=0.8
        )
        
        # Verify the request was made with correct parameters
        call_args = mock_request.call_args
        self.assertEqual(call_args[1]['json']['max_tokens'], 512)
        self.assertEqual(call_args[1]['json']['temperature'], 0.5)
        self.assertEqual(call_args[1]['json']['top_p'], 0.8)
    
    @patch('requests.request')
    def test_completion_success(self, mock_request):
        """Test successful text completion"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"text": "Generated text"}]
        }
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        response = self.provider.completion(
            model="test-model",
            prompt="Test prompt"
        )
        
        self.assertIn("choices", response)
        self.assertEqual(response["choices"][0]["text"], "Generated text")
    
    @patch('requests.request')
    def test_list_models_success(self, mock_request):
        """Test listing models"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "data": [
                {"id": "model-1", "name": "Model 1"},
                {"id": "model-2", "name": "Model 2"}
            ]
        }
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        models = self.provider.list_models()
        
        self.assertEqual(len(models), 2)
        self.assertEqual(models[0]["id"], "model-1")
    
    @patch('vibesdk_together.requests.request')
    def test_api_request_failure(self, mock_request):
        """Test handling of API request failure"""
        mock_request.side_effect = Exception("API Error")
        
        with self.assertRaises(RuntimeError):
            self.provider.chat_completion(
                model="test-model",
                messages=[{"role": "user", "content": "test"}]
            )
    
    @patch('requests.request')
    def test_test_connection_success(self, mock_request):
        """Test successful connection test"""
        mock_response = Mock()
        mock_response.json.return_value = {"data": [{"id": "model-1"}]}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        result = self.provider.test_connection()
        
        self.assertTrue(result["success"])
        self.assertIn("response_time", result)
        self.assertEqual(result["models_count"], 1)
    
    @patch('requests.request')
    def test_test_connection_failure(self, mock_request):
        """Test connection test failure"""
        mock_request.side_effect = Exception("Connection failed")
        
        result = self.provider.test_connection()
        
        self.assertFalse(result["success"])
        self.assertIn("error", result)


class TestVibeSDKTogetherConfig(unittest.TestCase):
    """Test cases for VibeSDKTogetherConfig class"""
    
    def test_create_model_config_basic(self):
        """Test creating basic model configuration"""
        config = VibeSDKTogetherConfig.create_model_config(
            model="test-model",
            temperature=0.5
        )
        
        self.assertEqual(config["name"], "together/test-model")
        self.assertEqual(config["temperature"], 0.5)
    
    def test_create_model_config_with_max_tokens(self):
        """Test creating model configuration with max_tokens"""
        config = VibeSDKTogetherConfig.create_model_config(
            model="test-model",
            max_tokens=2048
        )
        
        self.assertEqual(config["max_tokens"], 2048)
    
    def test_create_model_config_with_fallback(self):
        """Test creating model configuration with fallback"""
        config = VibeSDKTogetherConfig.create_model_config(
            model="test-model",
            fallback_model="fallback-model"
        )
        
        self.assertEqual(config["fallbackModel"], "together/fallback-model")
    
    def test_get_default_agent_config(self):
        """Test getting default agent configuration"""
        config = VibeSDKTogetherConfig.get_default_agent_config()
        
        # Check that all expected keys are present
        expected_keys = [
            "templateSelection", "blueprint", "projectSetup",
            "phaseGeneration", "phaseImplementation", "firstPhaseImplementation",
            "codeReview", "fileRegeneration", "screenshotAnalysis",
            "realtimeCodeFixer", "fastCodeFixer", "conversationalResponse",
            "deepDebugger"
        ]
        
        for key in expected_keys:
            self.assertIn(key, config)
            self.assertIn("name", config[key])
            self.assertIn("temperature", config[key])
    
    def test_default_agent_config_uses_together_prefix(self):
        """Test that default config uses 'together/' prefix"""
        config = VibeSDKTogetherConfig.get_default_agent_config()
        
        for action_config in config.values():
            self.assertTrue(action_config["name"].startswith("together/"))
    
    def test_model_constants(self):
        """Test that model constants are defined"""
        self.assertTrue(hasattr(VibeSDKTogetherConfig, 'LLAMA_3_70B_CHAT'))
        self.assertTrue(hasattr(VibeSDKTogetherConfig, 'LLAMA_3_8B_CHAT'))
        self.assertTrue(hasattr(VibeSDKTogetherConfig, 'MIXTRAL_8X7B'))
        self.assertTrue(hasattr(VibeSDKTogetherConfig, 'QWEN_2_72B'))
        self.assertTrue(hasattr(VibeSDKTogetherConfig, 'DEEPSEEK_CODER_33B'))


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    @patch('requests.request')
    def test_end_to_end_chat_workflow(self, mock_request):
        """Test end-to-end chat workflow"""
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)"
                    }
                }
            ]
        }
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response
        
        # Create provider
        provider = TogetherAIProvider(api_key="test-key")
        
        # Get config
        config = VibeSDKTogetherConfig.get_default_agent_config()
        code_config = config["phaseImplementation"]
        
        # Extract model name (remove 'together/' prefix)
        model_name = code_config["name"].replace("together/", "")
        
        # Make request
        response = provider.chat_completion(
            model=model_name,
            messages=[
                {"role": "user", "content": "Write a fibonacci function"}
            ],
            temperature=code_config["temperature"],
            max_tokens=code_config.get("max_tokens")
        )
        
        # Verify response
        self.assertIn("choices", response)
        self.assertIn("fibonacci", response["choices"][0]["message"]["content"])


if __name__ == "__main__":
    unittest.main()
