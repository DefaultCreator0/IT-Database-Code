from AI import AIChat

def main():

    Chatbot = AIChat()
    
    DataPacket = []

    DataPacket = Chatbot.SendUserRqst(input())

    #print(getUserInput(DataPacket))
    #print(getAIResponse(DataPacket))

def getAIResponse(DataPacket):
    return DataPacket[1]

def getUserInput(DataPacket):
    return DataPacket[0]


main()