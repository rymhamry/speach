import nltk
import speech_recognition as sr
import streamlit as st

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')

# Placeholder chatbot response (you can replace this with a more complex algorithm)
def chatbot_response(user_input):
    # Simple example: Just echo the user's input
    return f"You said: {user_input}"

# Function to transcribe speech to text
def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.write("Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        st.write("Transcribing speech...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        st.write("Sorry, I am having trouble with the speech recognition service.")
        return None

# Streamlit UI
st.title("Speech-Enabled Chatbot")

# Select input mode (Text or Speech)
input_mode = st.radio("Choose input mode", ("Text", "Speech"))

# Handle text input
if input_mode == "Text":
    user_input = st.text_input("Type your message:")
    
    if user_input:
        response = chatbot_response(user_input)
        st.write("Chatbot response:", response)

# Handle speech input
elif input_mode == "Speech":
    if st.button("Click to Speak"):
        user_input = transcribe_speech()
        
        if user_input:
            response = chatbot_response(user_input)
            st.write("Chatbot response:", response)

