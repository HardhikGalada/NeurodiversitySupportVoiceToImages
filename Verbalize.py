# !pip install openai

import openai
from openai import OpenAI
import os
os.environ['OPENAI_API_KEY'] = "YOUR_APIKEY_HERE"
client = OpenAI()
def imaging(list):
  for input_prompt in list:
    try:
      response = client.images.generate(
        model="dall-e-3",
        prompt=input_prompt,
        size="1024x1024",
        quality="standard",
        n=1,
      )
      image_url = response.data[0].url
      print(image_url)
    except openai.BadRequestError:
      continue

def prompting():
  insert_prompt = 'You are a person and you have to answer a question. Give Four different answers which will then be used as prompts for DALL-E for the following question:'+input()
  response = client.chat.completions.create(
    model="gpt-4",
    messages=[
    {"role": "user", "content": insert_prompt}],
    stream=True
  )
  texts=""
  for chunk in response:
    if chunk.choices[0].delta.content is not None:
      texts+=(chunk.choices[0].delta.content)
  inputs = texts.split("\n")
  print(inputs)
  imaging(inputs)

prompting()
