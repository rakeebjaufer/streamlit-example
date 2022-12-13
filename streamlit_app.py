import os
import openai
import gradio as gr

#openai.api_key = "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"
#openai.api_key = "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"
openai.api_key ="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"
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def predict(input,initial_prompt, history=[]):

    s = list(sum(history, ()))
    s.append(input)
#     initial_prompt="The following is a conversation with an AI movie recommendation assistant. The assistant is helpful, creative, clever, and very friendly.Along with movie recommendation it also talks about general topics"
#     \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt= initial_prompt + "\n" + str(s), 
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"])
    # tokenize the new input sentence
    response2 = response["choices"][0]["text"]
    history.append((input, response2))

    return history, history
