from AI import AIChat

def main():

    Chatbot = AIChat()
    
    DataPacket = []

    DataPacket = Chatbot.SendUserRqst("Hello")

    # print(DataPacket[1])

    # print(getUserInput("User Input {DataPacket}"))
    # print(getAIResponse(DataPacket))

def getAIResponse(DataPacket):
    return DataPacket[1]

def getUserInput(DataPacket):
    return DataPacket[0]

def ComplieToJson(DataPacket):
    return {
        "User" : DataPacket[0],
        "AI" : DataPacket[1]
    }



main()