"""
VibeSDK Together AI Integration
================================

A lightweight Python SDK adapter for integrating Together AI models with VibeSDK.
This module provides a simple interface for using Together AI's API with VibeSDK-like
configuration patterns.

Example usage:
    from vibesdk_together import TogetherAIProvider
    
    provider = TogetherAIProvider(api_key="your-api-key")
    response = provider.chat_completion(
        model="meta-llama/Llama-3-70b-chat-hf",
        messages=[{"role": "user", "content": "Hello!"}]
    )
"""

import os
from typing import Dict, List, Optional, Any, Union
import requests
import json


class TogetherAIProvider:
    """
    Together AI provider for VibeSDK integration.
    
    This class provides an interface to Together AI's API compatible with
    VibeSDK's model provider pattern.
    """
    
    DEFAULT_BASE_URL = "https://api.together.xyz/v1"
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = 60
    ):
        """
        Initialize Together AI provider.
        
        Args:
            api_key: Together AI API key. If not provided, will look for TOGETHER_API_KEY env var.
            base_url: Base URL for Together AI API. Defaults to https://api.together.xyz/v1
            timeout: Request timeout in seconds. Defaults to 60.
        """
        self.api_key = api_key or os.getenv("TOGETHER_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided or set in TOGETHER_API_KEY environment variable")
        
        self.base_url = (base_url or self.DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout
    
    def _make_request(
        self,
        endpoint: str,
        method: str = "POST",
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a request to the Together AI API.
        
        Args:
            endpoint: API endpoint (without base URL)
            method: HTTP method (GET, POST, etc.)
            data: Request body data
            params: URL parameters
            
        Returns:
            API response as a dictionary
            
        Raises:
            RuntimeError: If the API request fails
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                json=data,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Together AI API request failed: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"Together AI API request failed: {str(e)}")
    
    def chat_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        top_p: float = 0.9,
        stream: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a chat completion using Together AI.
        
        Args:
            model: Model identifier (e.g., "meta-llama/Llama-3-70b-chat-hf")
            messages: List of message dicts with 'role' and 'content' keys
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0-1)
            top_p: Nucleus sampling parameter
            stream: Whether to stream the response
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            API response containing the completion
        """
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "top_p": top_p,
            "stream": stream,
            **kwargs
        }
        
        if max_tokens is not None:
            data["max_tokens"] = max_tokens
        
        return self._make_request("chat/completions", data=data)
    
    def completion(
        self,
        model: str,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        top_p: float = 0.9,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Create a text completion using Together AI.
        
        Args:
            model: Model identifier
            prompt: Input prompt text
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0-1)
            top_p: Nucleus sampling parameter
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            API response containing the completion
        """
        data = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
            "top_p": top_p,
            **kwargs
        }
        
        if max_tokens is not None:
            data["max_tokens"] = max_tokens
        
        return self._make_request("completions", data=data)
    
    def list_models(self) -> List[Dict[str, Any]]:
        """
        List available models from Together AI.
        
        Returns:
            List of available models
        """
        response = self._make_request("models", method="GET")
        return response.get("data", [])
    
    def test_connection(self) -> Dict[str, Any]:
        """
        Test the connection to Together AI API.
        
        Returns:
            Dictionary with success status and response time
        """
        import time
        start_time = time.time()
        
        try:
            models = self.list_models()
            response_time = (time.time() - start_time) * 1000  # Convert to ms
            return {
                "success": True,
                "response_time": response_time,
                "models_count": len(models)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


class VibeSDKTogetherConfig:
    """
    Configuration class for Together AI models in VibeSDK-compatible format.
    
    This class provides model configurations compatible with VibeSDK's agent
    configuration pattern.
    """
    
    # Popular Together AI models
    LLAMA_3_70B_CHAT = "meta-llama/Llama-3-70b-chat-hf"
    LLAMA_3_8B_CHAT = "meta-llama/Llama-3-8b-chat-hf"
    MIXTRAL_8X7B = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    QWEN_2_72B = "Qwen/Qwen2-72B-Instruct"
    DEEPSEEK_CODER_33B = "deepseek-ai/deepseek-coder-33b-instruct"
    
    @staticmethod
    def create_model_config(
        model: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        fallback_model: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a VibeSDK-compatible model configuration.
        
        Args:
            model: Together AI model identifier
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            fallback_model: Optional fallback model
            
        Returns:
            Model configuration dictionary
        """
        config = {
            "name": f"together/{model}",
            "temperature": temperature
        }
        
        if max_tokens is not None:
            config["max_tokens"] = max_tokens
        
        if fallback_model is not None:
            config["fallbackModel"] = f"together/{fallback_model}"
        
        return config
    
    @classmethod
    def get_default_agent_config(cls) -> Dict[str, Dict[str, Any]]:
        """
        Get default agent configuration using Together AI models.
        
        Returns:
            Complete agent configuration for VibeSDK
        """
        return {
            "templateSelection": cls.create_model_config(
                cls.LLAMA_3_8B_CHAT,
                max_tokens=2048
            ),
            "blueprint": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=4096
            ),
            "projectSetup": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=4096
            ),
            "phaseGeneration": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=8192
            ),
            "phaseImplementation": cls.create_model_config(
                cls.DEEPSEEK_CODER_33B,
                max_tokens=8192,
                temperature=0.3
            ),
            "firstPhaseImplementation": cls.create_model_config(
                cls.DEEPSEEK_CODER_33B,
                max_tokens=8192,
                temperature=0.3
            ),
            "codeReview": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=4096,
                temperature=0.2
            ),
            "fileRegeneration": cls.create_model_config(
                cls.DEEPSEEK_CODER_33B,
                max_tokens=8192,
                temperature=0.3
            ),
            "screenshotAnalysis": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=4096
            ),
            "realtimeCodeFixer": cls.create_model_config(
                cls.LLAMA_3_8B_CHAT,
                max_tokens=2048,
                temperature=0.2
            ),
            "fastCodeFixer": cls.create_model_config(
                cls.LLAMA_3_8B_CHAT,
                max_tokens=2048,
                temperature=0.2
            ),
            "conversationalResponse": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=2048
            ),
            "deepDebugger": cls.create_model_config(
                cls.LLAMA_3_70B_CHAT,
                max_tokens=4096,
                temperature=0.3
            )
        }


def create_together_provider(
    api_key: Optional[str] = None,
    base_url: Optional[str] = None
) -> TogetherAIProvider:
    """
    Factory function to create a Together AI provider instance.
    
    Args:
        api_key: Together AI API key
        base_url: Custom base URL (optional)
        
    Returns:
        Configured TogetherAIProvider instance
    """
    return TogetherAIProvider(api_key=api_key, base_url=base_url)
