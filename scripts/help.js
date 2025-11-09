#!/usr/bin/env node

console.log(`
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║              VibeSDK Together AI Integration - Help                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝

This is a PYTHON package with optional Node.js wrapper support.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 INSTALLATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Option 1: Python Only (Recommended)
   npm run install:python
   # or
   pip install -r requirements.txt
   pip install -e .

Option 2: Use from Node.js
   npm run install:python  # Install Python package first
   # Then use the Node.js wrapper (see examples below)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 USAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Python (Direct):
   from vibesdk_together import TogetherAIProvider
   
   provider = TogetherAIProvider(api_key="your-key")
   response = provider.chat_completion(
       model="meta-llama/Llama-3-8b-chat-hf",
       messages=[{"role": "user", "content": "Hello!"}]
   )

Node.js (Wrapper):
   import { TogetherAIProvider, Models } from './index.js';
   
   const provider = new TogetherAIProvider('your-api-key');
   const response = await provider.chatCompletion({
       model: Models.LLAMA_3_8B_CHAT,
       messages: [{ role: 'user', content: 'Hello!' }]
   });

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 NPM SCRIPTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   npm run install:python   Install Python dependencies
   npm run build            Build Python package
   npm run test             Run tests
   npm run demo             Run demo
   npm run check            Verify installation
   npm run clean            Clean build artifacts
   npm run help             Show this help

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 API KEY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Get API key from: https://api.together.xyz
2. Set environment variable:
   export TOGETHER_API_KEY="your-api-key"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 DOCUMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   README.md              Main documentation
   QUICKSTART.md          Quick start guide (English)
   INICIO_RAPIDO_ES.md    Quick start guide (Spanish)
   CONFIGURATION.md       Configuration guide
   DEPLOYMENT.md          Deployment guide

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For more information, visit:
https://github.com/Miguel-Martin-ai/Vibesdktogether

`);
