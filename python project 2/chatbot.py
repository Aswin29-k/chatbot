import nltk
from nltk.chat.util import Chat, reflections
import streamlit as st

# Define chatbot responses using pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm doing well, thank you!", "I'm just a bot, but I'm good!"]],
    [r"what is your name", ["I'm a chatbot!", "You can call me ChatBot."]],
    [r"what can you do", ["I can chat with you, answer simple questions, and keep you company!"]],
    [r"who created you", ["I was created by a developer using Python and Streamlit!"]],
    [r"tell me a joke", ["Why don’t scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]],
    [r"what is the capital of France", ["The capital of France is Paris."]],
    [r"who is the president of the USA", ["I'm not sure, but you can check the latest news to find out!"]],
    [r"what is 2 \+ 2", ["2 + 2 is 4!"]],
    [r"what is the meaning of life", ["The meaning of life is subjective, but many say it's 42!"]],
    [r"what's your favorite color", ["I like blue, but I don't actually see colors!"]],
    [r"can you help me", ["Of course! What do you need help with?"]],
    [r"do you like music", ["I don't listen to music, but I can talk about it!"]],
    [r"tell me a fun fact", ["Did you know honey never spoils? Archaeologists found 3000-year-old honey in Egyptian tombs!"]],
    [r"do you believe in aliens", ["I think the universe is big enough for possibilities!"]],
    [r"how old are you", ["I exist beyond time, but I was created recently!"]],
    [r"what's the weather like", ["I can't check the weather, but you can use a weather website!"]],
    [r"recommend a book", ["I suggest '1984' by George Orwell or 'To Kill a Mockingbird' by Harper Lee!"]],
    [r"recommend a movie", ["Try watching 'Inception' if you like mind-bending stories!"]],
    [r"who is your favorite scientist", ["I admire many scientists, but Albert Einstein and Isaac Newton are legendary!"]],
    [r"what is the speed of light", ["The speed of light is approximately 299,792,458 meters per second!"]],
    [r"who won the last world cup", ["You might need to check the latest sports news for that!"]],
    [r"tell me a riddle", ["What has to be broken before you can use it? An egg!"]],
    [r"can you do math", ["I can do basic math. Try asking me a simple addition or multiplication question!"]],
    [r"do you know any quotes", ["Sure! 'The only way to do great work is to love what you do.' - Steve Jobs"]],
    [r"who is the richest person in the world", ["It changes frequently! You might want to check the latest billionaire rankings."]],
    [r"what languages do you speak", ["I understand English, but I can be trained for other languages too!"]],
    [r"how do airplanes fly", ["Airplanes fly using the principles of lift, thrust, drag, and weight!"]],
    [r"what is the tallest mountain", ["Mount Everest is the tallest mountain above sea level at 8,848 meters!"]],
    [r"how do I cook pasta", ["Boil water, add salt, drop the pasta in, and cook until tender. Then drain and enjoy!"]],
    [r"quit", ["Goodbye!", "See you later!"]],
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Streamlit UI
st.title("Basic Chatbot")
st.write("Start chatting with the bot below:")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

user_input = st.text_input("You:", "")
if user_input:
    response = chatbot.respond(user_input)
    st.session_state["messages"].append(("You", user_input))
    st.session_state["messages"].append(("Bot", response))

for sender, message in st.session_state["messages"]:
    st.write(f"**{sender}:** {message}")


