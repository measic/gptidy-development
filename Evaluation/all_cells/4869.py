with open("Chatbot_log.pkl", "wb") as file:
    pickle.dump(logs_chatbot, file)
Chatbot.save("Chatbot")