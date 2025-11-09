#!/usr/bin/env node

/**
 * Node.js wrapper for vibesdk-together Python package
 * 
 * This allows you to use the Python package from Node.js applications
 * by spawning Python processes.
 */

import { spawn } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

class TogetherAIProvider {
  constructor(apiKey = null) {
    this.apiKey = apiKey || process.env.TOGETHER_API_KEY;
    if (!this.apiKey) {
      throw new Error('API key must be provided or set in TOGETHER_API_KEY environment variable');
    }
  }

  /**
   * Execute Python script and return result
   */
  async _executePython(script) {
    return new Promise((resolve, reject) => {
      const python = spawn('python', ['-c', script], {
        env: { ...process.env, TOGETHER_API_KEY: this.apiKey }
      });

      let stdout = '';
      let stderr = '';

      python.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      python.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      python.on('close', (code) => {
        if (code !== 0) {
          reject(new Error(`Python execution failed: ${stderr}`));
        } else {
          try {
            resolve(JSON.parse(stdout));
          } catch (e) {
            resolve(stdout);
          }
        }
      });
    });
  }

  /**
   * Chat completion using Together AI
   */
  async chatCompletion(options) {
    const { model, messages, maxTokens = null, temperature = 0.7, topP = 0.9 } = options;
    
    const script = `
import json
import os
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key=os.getenv('TOGETHER_API_KEY'))
response = provider.chat_completion(
    model="${model}",
    messages=${JSON.stringify(messages)},
    ${maxTokens ? `max_tokens=${maxTokens},` : ''}
    temperature=${temperature},
    top_p=${topP}
)
print(json.dumps(response))
`;

    return await this._executePython(script);
  }

  /**
   * Text completion using Together AI
   */
  async completion(options) {
    const { model, prompt, maxTokens = null, temperature = 0.7 } = options;
    
    // Properly escape the prompt for Python
    const escapedPrompt = JSON.stringify(prompt);
    
    const script = `
import json
import os
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key=os.getenv('TOGETHER_API_KEY'))
response = provider.completion(
    model="${model}",
    prompt=${escapedPrompt},
    ${maxTokens ? `max_tokens=${maxTokens},` : ''}
    temperature=${temperature}
)
print(json.dumps(response))
`;

    return await this._executePython(script);
  }

  /**
   * List available models
   */
  async listModels() {
    const script = `
import json
import os
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key=os.getenv('TOGETHER_API_KEY'))
models = provider.list_models()
print(json.dumps(models))
`;

    return await this._executePython(script);
  }

  /**
   * Test connection to Together AI
   */
  async testConnection() {
    const script = `
import json
import os
from vibesdk_together import TogetherAIProvider

provider = TogetherAIProvider(api_key=os.getenv('TOGETHER_API_KEY'))
result = provider.test_connection()
print(json.dumps(result))
`;

    return await this._executePython(script);
  }
}

/**
 * Get VibeSDK configuration
 */
async function getVibeSDKConfig() {
  const script = `
import json
from vibesdk_together import VibeSDKTogetherConfig

config = VibeSDKTogetherConfig.get_default_agent_config()
print(json.dumps(config))
`;

  return new Promise((resolve, reject) => {
    const python = spawn('python', ['-c', script]);
    let stdout = '';
    let stderr = '';

    python.stdout.on('data', (data) => {
      stdout += data.toString();
    });

    python.stderr.on('data', (data) => {
      stderr += data.toString();
    });

    python.on('close', (code) => {
      if (code !== 0) {
        reject(new Error(`Python execution failed: ${stderr}`));
      } else {
        try {
          resolve(JSON.parse(stdout));
        } catch (e) {
          reject(new Error(`Failed to parse JSON: ${e.message}`));
        }
      }
    });
  });
}

// Model constants
const Models = {
  LLAMA_3_70B_CHAT: 'meta-llama/Llama-3-70b-chat-hf',
  LLAMA_3_8B_CHAT: 'meta-llama/Llama-3-8b-chat-hf',
  DEEPSEEK_CODER_33B: 'deepseek-ai/deepseek-coder-33b-instruct',
  MIXTRAL_8X7B: 'mistralai/Mixtral-8x7B-Instruct-v0.1',
  QWEN_2_72B: 'Qwen/Qwen2-72B-Instruct'
};

export {
  TogetherAIProvider,
  getVibeSDKConfig,
  Models
};

export default TogetherAIProvider;
