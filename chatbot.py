import requests

def chatbot_interaction(user_input):
    url = "https://models3.p.rapidapi.com/"
    querystring = {"model_id": "27", "prompt": user_input}
    payload = {"key1": "value", "key2": "value"}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "YOUR_API",
        "X-RapidAPI-Host": "models3.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    return response.json()

def main():
    while True:
        user_input = input("You: ")
        if user_input == "!quit":
            print("Goodbye!")
            break
        else:
            response = chatbot_interaction(user_input)
            print("Chatbot:", response['content'])

if __name__ == "__main__":
    main()
