import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
)


history = []
chat_session = model.start_chat(history=history)

print("hello, I am your AI assistant. How can I help you today?")

while True:
    user_input = input("You : ")

    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    # --- Start of Modified Logic for Input Handling ---
    # Strip whitespace from the user input *before* checking if it's empty
    # and before appending to history.
    processed_user_input = user_input.strip()

    if not processed_user_input: # Check if the stripped input is empty
        print("Please enter a valid message.")
        continue

    # Append the PROCESSED user input to history
    history.append({"role": "user", "parts": [processed_user_input]})

    # Send the PROCESSED user input to the model
    response = chat_session.send_message(processed_user_input)
    # --- End of Modified Logic for Input Handling ---

    # --- Safety and Response Handling (from previous debug) ---
    if response.candidates:
        finish_reason = response.candidates[0].finish_reason
        if finish_reason == 2:  # finish_reason 2 usually means SAFETY
            model_response = "I'm sorry, I cannot provide a response to that request. It may fall outside of my safety guidelines."
        elif response.text:
            model_response = response.text
        else:
            model_response = "I encountered an unexpected issue with the model response. Please try again."
    else:
        model_response = "I couldn't generate a response. The API might be experiencing an issue or returned no candidates."
    # --- End of Safety and Response Handling ---

    print("Bot : ", model_response)
    print("--------------------------------------------------")
    
    # Append model response to history (this part was already fine)
    history.append({"role": "model", "parts": [model_response]})