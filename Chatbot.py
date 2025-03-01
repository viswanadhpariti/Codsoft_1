from datetime import datetime

def chatbot(user_input):
    if "hello"in user_input.lower():
        return "Hello! How can I help you today?"
    elif "weather" in user_input.lower():
        return "I can check the weather for you. Where are you located?"
    elif "time" in user_input.lower():
        return "Currently, I'm in India Standard Time. Do you want to know the exact time?"
    elif "yes" in user_input.lower():
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"current time :{current_time}"
    elif "what is the date" in user_input.lower() or "date" in user_input.lower():
        current_date = datetime.today().strftime("%d-%B-%Y")
        return f"current date is {current_date}"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"

print("Welcome to the simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot:", chatbot(user_input))