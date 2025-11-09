#!/usr/bin/env node

/**
 * Example: Using vibesdk-together from Node.js
 * 
 * This demonstrates how to use the Python package from a Node.js application.
 * 
 * Prerequisites:
 * 1. Run: npm run install:python
 * 2. Set: export TOGETHER_API_KEY="your-api-key"
 * 3. Run: node example-nodejs.js
 */

import { TogetherAIProvider, getVibeSDKConfig, Models } from './index.js';

async function main() {
  console.log('╔══════════════════════════════════════════════════════════════════╗');
  console.log('║  VibeSDK Together AI - Node.js Example                          ║');
  console.log('╚══════════════════════════════════════════════════════════════════╝\n');

  // Check if API key is set
  if (!process.env.TOGETHER_API_KEY) {
    console.error('❌ Error: TOGETHER_API_KEY environment variable not set');
    console.log('\nPlease set your API key:');
    console.log('  export TOGETHER_API_KEY="your-api-key-here"\n');
    process.exit(1);
  }

  try {
    // Initialize provider
    console.log('1️⃣  Initializing TogetherAI Provider...');
    const provider = new TogetherAIProvider();
    console.log('   ✅ Provider initialized\n');

    // Test connection
    console.log('2️⃣  Testing connection...');
    const connectionTest = await provider.testConnection();
    if (connectionTest.success) {
      console.log(`   ✅ Connected successfully`);
      console.log(`   ⏱️  Response time: ${connectionTest.response_time.toFixed(2)}ms`);
      console.log(`   📊 Models available: ${connectionTest.models_count}\n`);
    } else {
      console.log(`   ❌ Connection failed: ${connectionTest.error}\n`);
      return;
    }

    // Example 1: Simple chat
    console.log('3️⃣  Example: Simple Chat Completion');
    console.log('   Model: Llama 3 8B Chat');
    console.log('   Prompt: "Say hello in Spanish"\n');
    
    const chatResponse = await provider.chatCompletion({
      model: Models.LLAMA_3_8B_CHAT,
      messages: [
        { role: 'system', content: 'You are a helpful assistant.' },
        { role: 'user', content: 'Say hello in Spanish' }
      ],
      maxTokens: 100
    });

    console.log('   Response:');
    console.log('   ' + chatResponse.choices[0].message.content + '\n');

    // Example 2: Get VibeSDK config
    console.log('4️⃣  Example: Get VibeSDK Configuration');
    const config = await getVibeSDKConfig();
    console.log(`   ✅ Retrieved ${Object.keys(config).length} agent configurations`);
    console.log(`   📝 Code generation model: ${config.phaseImplementation.name}`);
    console.log(`   🔍 Code review model: ${config.codeReview.name}\n`);

    // Example 3: List available models
    console.log('5️⃣  Example: List Available Models');
    const models = await provider.listModels();
    console.log(`   ✅ Found ${models.length} models`);
    console.log('   First 3 models:');
    models.slice(0, 3).forEach((model, i) => {
      console.log(`      ${i + 1}. ${model.id || model.name || 'Unknown'}`);
    });
    console.log('');

    console.log('╔══════════════════════════════════════════════════════════════════╗');
    console.log('║  ✅ All examples completed successfully!                        ║');
    console.log('╚══════════════════════════════════════════════════════════════════╝\n');

  } catch (error) {
    console.error('❌ Error:', error.message);
    console.error('\nMake sure you have:');
    console.error('  1. Installed Python dependencies: npm run install:python');
    console.error('  2. Set TOGETHER_API_KEY environment variable');
    console.error('  3. Python 3.7+ installed and in PATH\n');
    process.exit(1);
  }
}

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(console.error);
}

export default main;
