import requests

OLLAMA_URL = 'http://localhost:11434/api/chat'

def send_message_to_ollama(message, model="mistral"):
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "messages": [
            {"role": "user", "content": message}
        ]
    })
    if response.status_code == 200:
        return response.json()['message']['content']
    else:
        return f"❌ Error: {response.text}"

def chat_loop():
    print("🤖 Локальний чат-бот на базі Ollama. Напиши 'вихід' для завершення.")
    while True:
        user_input = input("🧑 Ти: ")
        if user_input.lower() in ["bye"]:
            print("👋 До побачення!")
            break

        response = send_message_to_ollama(user_input)
        print("🤖 Бот:", response)

if __name__ == '__main__':
    chat_loop()
