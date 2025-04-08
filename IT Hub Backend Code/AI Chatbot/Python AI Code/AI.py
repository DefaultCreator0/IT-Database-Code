from Libs.google import genai

class AIChat:

    def __init__(self):
        #Instantiating the client with the Gemini API Key
        client = genai.Client(api_key="AIzaSyBS-jAuZwRNLbDsSoxuHtqlmd6kegQ9O5E")
        #Selecting the model of Gemini
        self.chat = client.chats.create(model="gemini-2.0-flash")
        Input = ""
        #Prompting the AI the start the conversation so that the user can notice it's presence
        response = self.chat.send_message_stream("Hello")
        for chunk in response:
            print(chunk.text, end="")

    def SendUserRqst(self,UserInput):
        """This function packages the user input into a List along with the chat record from the AI bot
        """
        Input=[]
        Input.append(UserInput)
        Input.append(self.chat.send_message_stream(Input[0]))
        return self.RecieveBotRqst(Input) 

    def RecieveBotRqst(self,Input):
        """Receives the Initial datapacket from the first step, unpacks the AI response, and the repackages the input and response for later use.
        """
        InputPacket = []    
    
        ans=[]
        for chunk in Input[1]:
            ans.append(chunk.text) 
        String = ''.join(ans)

        InputPacket.append(Input[0])
        InputPacket.append(String)

        return InputPacket


