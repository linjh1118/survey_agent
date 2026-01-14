#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from survey_agent.env import *
from openai import OpenAI

def test_llm_api():
    print("=" * 60)
    print("Testing LLM API Connection")
    print("=" * 60)
    
    api_key = os.environ.get("API_KEY")
    base_url = os.environ.get("BASE_URL")
    model = os.environ.get("SURVEY_AGENT_LLM_MODEL", "ep-20250526175303-cv654")
    
    print(f"\n[Config]")
    print(f"  API_KEY: {api_key[:20]}..." if api_key else "  API_KEY: Not set")
    print(f"  BASE_URL: {base_url}")
    print(f"  MODEL: {model}")
    
    if not api_key or not base_url:
        print("\n[ERROR] API_KEY or BASE_URL not set!")
        return False
    
    try:
        print(f"\n[Test] Sending test request to LLM...")
        print(f"  (This may take a few seconds...)")
        
        client = OpenAI(api_key=api_key, base_url=base_url, timeout=30.0)
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! Please respond with 'API test successful' if you receive this message."}
            ],
            max_tokens=50,
            temperature=0.7
        )
        
        result = response.choices[0].message.content
        print(f"\n[Response]")
        print(f"  {result}")
        
        print(f"\n[Success] ✓ LLM API is working correctly!")
        print(f"  Model: {response.model}")
        print(f"  Tokens used: {response.usage.total_tokens}")
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] ✗ LLM API test failed!")
        print(f"  Error type: {type(e).__name__}")
        print(f"  Error message: {str(e)}")
        
        import traceback
        print(f"\n[Debug] Full traceback:")
        traceback.print_exc()
        
        print(f"\n[Troubleshooting Tips]")
        print(f"  1. Check if the API endpoint is accessible")
        print(f"  2. Verify API_KEY is valid and not expired")
        print(f"  3. Check network connectivity (proxy settings if needed)")
        print(f"  4. Verify the model name is correct")
        
        return False

if __name__ == "__main__":
    success = test_llm_api()
    sys.exit(0 if success else 1)
