from ..model.model_1 import get_responses

def main_1():
    print("chatbot : hi how i can help you! ")
    while True:
        user_input = input("User :  ").lower()
        responses= get_responses(user_input)
        print("chatbot",responses)
        if user_input=="goodbye":
         break