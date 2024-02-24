import openai
from openai import OpenAI
import os
os.environ['OPENAI_API_KEY'] = "YOUR_API_HERE"
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
  insert_prompt = 'Four different prompts for DALL-E for'+input()
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
  imaging(inputs)
prompting()