from Libs.google import genai


def main():

    #Instantiating the client with the Gemini API Key
    client = genai.Client(api_key="AIzaSyBS-jAuZwRNLbDsSoxuHtqlmd6kegQ9O5E")
    #Selecting the model of Gemini
    chat = client.chats.create(model="gemini-2.0-flash")

    Input = ""
    #Prompting the AI the start the conversation so that the user my notice it's presence
    response = chat.send_message_stream("Hello")
    for chunk in response:
        print(chunk.text, end="")

    #Loop to keep the User and AI in dialogue
    while(Input != "exit"):

        Input = input()
        #Sending the user response and printing the AI answer
        response = chat.send_message_stream(Input)
        for chunk in response:
            print(chunk.text, end="")

main()
