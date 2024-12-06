import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
GPT_MODEL = "gpt-4"  # or "gpt-3.5-turbo" if using GPT-3.5

# Example prompt messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
]

def chat_with_ai(messages):
    try:
        # Use the client object to call the correct endpoint
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=0.7,  # Adjust the creativity/temperature of the model
            max_tokens=150  # Adjust token limit as per your requirement
        )

        # Extract the AI's response using the correct attribute
        response_message = response.choices[0].message.content.strip()
        
        return response_message
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Welcome to the AI Chat Assistant!")
    print("Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        # Prepare messages with user input
        user_message = {"role": "user", "content": user_input}
        messages.append(user_message)
        
        reply = chat_with_ai(messages)
        print(f"AI: {reply}")
