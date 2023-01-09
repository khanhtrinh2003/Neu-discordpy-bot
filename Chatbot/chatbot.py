import openai
import discord
import requests
import io

openai.api_key = ""


def AI_BOT(tin_nhan):        
    if tin_nhan.startswith("!image"):
        prompt = tin_nhan[7:]
        api_url = "https://api.openai.com/v1/images/generations"
        api_key = {"Authorization": f"Bearer {openai.api_key}"}
        data = {"model": "image-alpha-001", "prompt": prompt, "num_images": 1, "size": "512x512", "response_format": "url"}
        response = requests.post(api_url, headers=api_key, json=data).json()
        if 'error' in response:
            error_message = response['error']['message']
            return (f"An error occurred: {error_message}")
        else:
            image_url = response['data'][0]['url']
            return image_url

    else:
        prompt = tin_nhan
        response_lines = generate_response(prompt, 0.5)
        if isinstance(response_lines, str):
            return (response_lines)
        else:
            for line in response_lines:
                return (line)
        

def generate_response(prompt, temperature):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000, # 4000 is the maximum number of tokens for the davinci 003 GPT3 model
        n=1,
        stop=None,
        temperature=temperature,
    )

    if 'error' in completions:
        return completions['error']['message']
    else:
        message = completions.choices[0].text

    if '!image' in prompt:
        return message
    else:
        return message
