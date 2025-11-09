"""
VibeSDK Together AI Integration

A Python SDK adapter for integrating Together AI models with VibeSDK.
"""

from vibesdk_together import (
    TogetherAIProvider,
    VibeSDKTogetherConfig,
    create_together_provider
)

__version__ = "1.0.0"
__author__ = "Miguel Martin"
__all__ = [
    "TogetherAIProvider",
    "VibeSDKTogetherConfig", 
    "create_together_provider"
]
