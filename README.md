# Sereni Chat

Using Google Generative AI model, this Streamlit app implements a Mental Support Chatbot. 
The chatbot provides a listening ear and support for mental well-being, responding to user inputs with empathy and understanding.

## Getting Started

   Don't forget to add a .env file to your project and add your Google generative AI API
   Your .env file contents should look something like this 

   ```
   GENAI_API_KEY=YOUR API KEY GOES HERE
   ```
   For instancees where you are launching your project on different platforms like streamlit.io or any other ,
   Go to the app advanced settings and include your API key in TOML format 
   ```
   GENAI_API_KEY = "YOUR API KEY GOES HERE"

   ```

1. Install dependencies:
   In your command prompt, 
   write cd then add your location/directory
   Then Run
   ```
   pip install -r requirements.txt
    ```
   If you have not initiated a virtual environment for your project/ directory and you don't want to , use
   ```
   python -m pip install -r requirements.txt
   ```


3. Run the Streamlit app:

    ```
    streamlit run main.py
    ```

## Usage

A login and signup page is provided is provided.
An Internet connection is required for the chatbot to run

After login /Signup, 

1. Enter your messages in the text input field.

2. Click the "Send" button to interact with the chatbot.

3. The chatbot will respond with supportive messages related to mental health.

## Conversation History

The conversation history is loaded from the `conversation_history.json` file. You can customize the conversation or extend it as needed.
