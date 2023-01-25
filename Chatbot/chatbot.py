import openai
import requests

openai.api_key = ""

def generate_response(tin_nhan, temperature):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=tin_nhan,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=temperature,
    )
    message = completions.choices[0].text
    return message

def Chat(tin_nhan): 
    message = generate_response(tin_nhan, 0.5)
    return message

def AI_BOT(tin_nhan):        
    if tin_nhan.startswith("#"):
        pass 
    else:
        message = generate_response(tin_nhan, 0.5)
        return message
    
def Code(tin_nhan):
    completions = openai.Completion.create(
        engine="code-davinci-002",
        prompt=tin_nhan,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return f"```{message}```"


def Image(tin_nhan):
    api_url = "https://api.openai.com/v1/images/generations"
    api_key = {"Authorization": f"Bearer {openai.api_key}"}
    data = {"model": "image-alpha-001", "prompt": tin_nhan, "num_images": 1, "size": "1024x1024", "response_format": "url"}
    response = requests.post(api_url, headers=api_key, json=data).json()
    if 'error' in response:
        error_message = response['error']['message']
        return (f"An error occurred: {error_message}")
    else:
        image_url = response['data'][0]['url']
        return image_url
