import ollama


response = ollama.list()
# print(response)

# *** Chat example ***

res = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Can you explain common API usage?"},
    ],
)
# print(res["message"]["content"])

# ** Chat example streaming **
res = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What common syntax problems are there in an API?",


        },
    ],
    stream=True,
)
for chunk in res:
    print(chunk["message"]["content"], end="", flush=True)
