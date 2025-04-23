from Libs.google import genai
import io
import httpx

class AIChat:

    ContentVar = []

    def __init__(self):
        #Instantiating the client with the Gemini API Key
        self.client = genai.Client(api_key="AIzaSyBS-jAuZwRNLbDsSoxuHtqlmd6kegQ9O5E")
        #Selecting the model of Gemini
        self.chat = self.client.chats.create(model="gemini-2.0-flash")
        Input = ""
        
        #doc_url_1 = "https://storage.googleapis.com/defalt_kbs/Kbs/How_to_Create_Your_Account.pdf"
        #doc_url_2 = "https://storage.googleapis.com/defalt_kbs/Kbs/Forgot_My_Password.pdf" 
        #doc_url_3 = "https://storage.googleapis.com/defalt_kbs/Kbs/How_to_Submit_a_Ticket.pdf" 
        #doc_url_4 = "https://storage.googleapis.com/defalt_kbs/Kbs/How_to_Use_Procurement_System.pdf" 
        #doc_url_5 = "https://storage.googleapis.com/defalt_kbs/Kbs/Troubleshooting_Common_Issues.pdf" 
        #doc_url_6 = "https://storage.googleapis.com/defalt_kbs/Kbs/Using_the_AI_Chatbot.pdf" 

        # Retrieve and upload both PDFs using the File API
        #doc_data_1 = io.BytesIO(httpx.get(doc_url_1).content)
        #doc_data_2 = io.BytesIO(httpx.get(doc_url_2).content)
        #doc_data_3 = io.BytesIO(httpx.get(doc_url_3).content)
        #doc_data_4 = io.BytesIO(httpx.get(doc_url_4).content)
        #doc_data_5 = io.BytesIO(httpx.get(doc_url_5).content)
        #doc_data_6 = io.BytesIO(httpx.get(doc_url_6).content)

        #sample_pdf_1 = self.client.files.upload(file=doc_data_1, config=dict(mime_type='application/pdf')) #How to create Acc
        #sample_pdf_2 = self.client.files.upload(file=doc_data_2, config=dict(mime_type='application/pdf')) #Forgot Password
        #sample_pdf_3 = self.client.files.upload(file=doc_data_3, config=dict(mime_type='application/pdf')) #How to submit Ticket
        #sample_pdf_4 = self.client.files.upload(file=doc_data_4, config=dict(mime_type='application/pdf')) #How to use procurement
        #sample_pdf_5 = self.client.files.upload(file=doc_data_5, config=dict(mime_type='application/pdf')) #Common Troubleshooting
        #sample_pdf_6 = self.client.files.upload(file=doc_data_6, config=dict(mime_type='application/pdf')) #Using Chatbot

        
        
        # prompt = "Before prompting the user for anything, ask the user for their name and user ID, once you receive this proceed with any other question"\
        #          "Ask if the user has any issue or would like to review one our KB articles."\
        #          "If the user is having an issue ask them what the issue is in detail and once the data is collected repeat it to them for confirmation"\
        #          "Once the data is confirmed direct them to the ticket creation link"\
        #          "The link for the ticket creation is http://localhost:5000/Ticket."\
        #          "If the user request information on a certain policy, provide them with a link to the corresponding link only once they tell you what article they would like to see"\
        #          "How to create Account : storage.googleapis.com/defalt_kbs/Kbs/How_to_Create_Your_Account.pdf"\
        #          "Forgot Password : storage.googleapis.com/defalt_kbs/Kbs/Forgot_My_Password.pdf"\
        #          "How to Submit Ticket : storage.googleapis.com/defalt_kbs/Kbs/How_to_Submit_a_Ticket.pdf"\
        #          "How to use Procurement Portal : storage.googleapis.com/defalt_kbs/Kbs/How_to_Use_Procurement_System.pdf"\
        #          "Common Troubleshooting : storage.googleapis.com/defalt_kbs/Kbs/Troubleshooting_Common_Issues.pdf"\
        #          "Using the Chatbot : storage.googleapis.com/defalt_kbs/Kbs/Using_the_AI_Chatbot.pdf"

        #self.ContentVar = [sample_pdf_1,sample_pdf_2,sample_pdf_3,sample_pdf_4,sample_pdf_5,sample_pdf_6,prompt]

        #response1 = self.client.models.generate_content(
        #    model="gemini-2.0-flash",
        #    contents=[self.ContentVar, prompt])
        

        # respoText = ""
        # response2 = self.chat.send_message_stream("Hello")
        # for chunk in response2:
        #     respoText += chunk.text
        
        # print(type(respoText))
        # print(respoText)
        # print(response.text) #Test Response

        # #Prompting the AI the start the conversation so that the user can notice it's presence
        # response = self.chat.send_message_stream("Hello")
        # for chunk in response:
        #     print(chunk.text, end="")

    def SendUserRqst(self,UserInput="Hello"):
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


