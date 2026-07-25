from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("Choose AI personality and start chatting...")
print("Choose your AI Mode:")
print("1. 😡 Angry")
print("2. 😂 Funny")
print("3. 😢 Sad")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

messages = [
    SystemMessage(content=mode)
]

print("***************** You can start chatting now! Type '0' to stop. ********************")

while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == '0':
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ", response.content)

print("Messages: ", messages)
print("***************** Chat Ended ********************")