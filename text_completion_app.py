import cohere
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
co = cohere.ClientV2(API_KEY)

def get_response(prompt, temp):
    try:
        response = co.chat(
            model='command-a-03-2025',
            messages=[{"role":"user", "content":prompt}],
            max_tokens=500,
            temperature=temp
        )
        return response.message.content[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"


# print(response)
print("##################################################")
print("\tWelcome to the text completion app")
print("####################################################")
print("Type 'exit' to exit the program")

while True:
    print("\nWould yould like to set the creativity of the text?")
    res = input("Y/N: ")
    if res.upper() == "Y":
        creativity = float(input("To set creativity enter a float between 0 and 1: "))
        if creativity > 0 and creativity < 1:
            prompt = input("Enter a prompt: ")
            response = get_response(prompt, creativity)
            print("AI Response: ", response)

        else:
            print("Please enter a number between 0 and 1")
        # continue
    elif res.upper() == "N":
        creativity = 0.7
        prompt = input("Enter a prompt: ")
        if prompt == 'exit':
            print("GoodBye!")
            exit()
        if not prompt:
            print("Please enter a valid prompt!")
        response = get_response(prompt, creativity)
        print("AI Response: ", response)

# text_completion_app.py