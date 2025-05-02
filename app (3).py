import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Set Streamlit page configuration
st.set_page_config(page_title="Depression Detection", page_icon=":no_entry:")

# Header
st.header("Depression Detection")

# Initialize session state if not already present
if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = [
        SystemMessage(content="You are a depression detection system. Classify the following text as 'depressed' or 'not depressed'.")
    ]

# Function to classify text
def detect_hate_speech(text):
    st.session_state.sessionMessages.append(HumanMessage(content=text))  # User input

    # Send the message to OpenAI
    assistant_answer = chat(st.session_state.sessionMessages)

    # Store assistant response
    st.session_state.sessionMessages.append(AIMessage(content=assistant_answer.content))

    return assistant_answer.content

# Function to get user input
def get_text():
    input_text = st.text_input("Enter text for depression classification:")
    return input_text

# Initialize ChatOpenAI with temperature 0 for deterministic output
chat = ChatOpenAI(temperature=0)

# Get user input
user_input = get_text()
submit = st.button('Classify')  # Submit button for user input

# If button is pressed, classify the text
if submit:
    if user_input:
        response = detect_hate_speech(user_input)
        st.subheader("Classification:")
        st.write(response)
    else:
        st.write("Please enter some text to classify.")