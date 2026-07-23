from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from groq import Groq
from sentiment_analysis import predict_sentiment
import os
import json
load_dotenv()




conversation = [{"role":"system", "content":'You are a customer care service bot.'}]

class LLMProvider:
    def __init__(self, model_name):
        self.model_name = model_name

    def send_message(self):
        pass


class Phi4Provider(LLMProvider):
    def __init__(self, model_name):
        self.model_name = model_name
        self.api_key = os.getenv('AZURE_API_KEY')
        if self.api_key == None:
            raise MissingAPIKeyError("Girllll your API KEY is missing!!!!")
        self.endpoint = 'https://models.github.ai/inference'
        self.client = ChatCompletionsClient(
            endpoint=self.endpoint, 
            credential=AzureKeyCredential(self.api_key))

    def send_message(self):
        response = self.client.complete (messages= conversation,
                                        temperature= 1,
                                        model= self.model_name,
                                        max_tokens=100)

        ai_reply = (response.choices[0].message.content)
        
        return ai_reply
            

class GroqProvider(LLMProvider):
    def __init__(self,model_name):
        self.model = model_name
        self.api_key = os.getenv("GROQ_API_KEY")
        if self.api_key == None:
            raise MissingAPIKeyError("Girllll your API KEY is missing!!!!")
        self.base_url = "https://api.groq.com/openai/v1"
        self.client = Groq(api_key= self.api_key)
        

    def send_message(self):
        chat_completion = self.client.chat.completions.create(
            messages = conversation,
            model = self.model
        )
        ai_reply = chat_completion.choices[0].message.content
        return ai_reply


class MissingAPIKeyError(Exception):
    pass



try:
    with open ("C:\\Users\\USER\\Documents\\LLM Projects\\conversation.json", "r") as f:
        data = json.load(f)
        conversation = data
except:
    print(" Welcome to our first chat")
    

finally:
    while True:
        option = input("Press C to continue and E to exit: ")
        if option.lower() == "c":
            print("Avaliabe Models are \n 1. microsoft/Phi-4 \n 2. openai/gpt-oss-120b")
            ai_choice = input("What model would you like to use \n Enter 1 or 2 ")
            if ai_choice == '1':
                model_name = 'microsoft/Phi-4'
                active_model = Phi4Provider(model_name)
            elif ai_choice == '2':
                model_name = 'openai/gpt-oss-120b'
                active_model = GroqProvider(model_name)
            else:
                print("select an existing model")
                continue
            
                
            user_input = input("Enter your message: ")
            sentiment = predict_sentiment(user_input)
            conversation[0]["content"] = (
                f"You are a customer care service bot. "
                f"The customer's sentiment is {sentiment}. "
                "If the sentiment is negative, respond with empathy and apologize for the inconvenience. "
                "If the sentiment is positive, respond warmly and appreciatively. "
                "If the sentiment is neutral, respond normally and helpfully."
            )


            user_dict = {"role":"user", "content": user_input}
            conversation.append(user_dict)

            
            ai_response = active_model.send_message()
            print(ai_response)
            ai_dict = {"role":"assistant", "content":ai_response}
            conversation.append(ai_dict)

            with open ("C:\\Users\\USER\\Documents\\Multi-Provider LLM Chat\\conversation.json", "w") as f:
                data = json.dump(conversation, f)
    

        elif option.lower() == "e":
            print("Okay Bye")
            break

        else:
            print("Please input a valid number")
                            
    
    

    

