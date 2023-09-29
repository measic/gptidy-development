import openai

def gpt_wrapper(msgs, n=1, stop=None, temperature=0):
    while True:
        try:
            completions = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature = temperature,
                messages= msgs,
                n = n,
                stop = stop
            )
        except Exception as e:
            if 'maximum context length' in str(e):
                print('...Error.. too long...aborting...' + str(e))
                return None
            else:
                print('...Error.. trying again...' + str(e))
        else:
            break
    return completions

def gpt_unpack_simple(completions):
    return completions.choices[0].finish_reason, completions.choices[0].message["content"]