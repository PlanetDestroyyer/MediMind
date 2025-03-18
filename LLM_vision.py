from ollama import chat


# path = input('Please enter the path to the image: ')

response = chat(
  model='erwan2/DeepSeek-Janus-Pro-7B-Vision-Encoder:latest',
  messages=[
    {
      'role': 'user',
      'content': 'What is in this image? Be concise.',
      'images': ['image.jpg'],
    }
  ],
)

print(response.message.content)