import requests

text = input("Please write your prompt here:")
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': text,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'},
    timeout= 30.0
)
print(r.json())