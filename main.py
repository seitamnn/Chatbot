import openai

openai.api_key = "API_KEY"

def chat_with_gbt(prompt):
    response = openai.chatCompletion.create(
        model="gbt-3.5-turbo",
        messages=[{"role": "user", "content": "prompt"}]
    )

    return response.choises[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

    response = chat_with_gbt(user_input)
    print("Chatbot: ", response)