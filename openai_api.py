import openai
my_key = "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"
han = "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"
openai.api_key = my_key
import testing

def prompt():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages= testing.summarize
    )
    if completion.choices[0].finish_reason != "stop":
        raise Exception("OpenAI API did not return a valid response")
    return completion.choices[0].message

print(prompt()["content"])