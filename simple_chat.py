import ollama
from typing import List, Dict
import json
from datetime import datetime

def chat_with_model(
    model: str = 'gemma2:2b',
    messages: List[Dict[str, str]] = None,
    print_full_response: bool = False
) -> Dict:
    if messages is None:
        messages = [{
            'role': 'user',
            'content': 'Hi'
        }]
    
    try:
        # Make the API call
        response = ollama.chat(
            model=model,
            messages=messages
        )
        
        # Print just the message content
        print("\nModel's response:")
        print(response['message']['content'])
        
        # Optionally print the full response details
        if print_full_response:
            print("\nFull response details:")
            print(json.dumps(response, indent=2))
            
        return response
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Example usage
    messages = [
        {
            'role': 'user',
            'content': 'What is the fastest animal on the planet?'
        },
    ]
    
    chat_with_model(
        model='gemma2:2b',
        messages=messages,
        print_full_response=True
    )