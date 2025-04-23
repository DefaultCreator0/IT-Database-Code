        try:
            # 3. Specify the path to your local file
            file_path = "F:\\AI Chatbot\\Python_AI_Code\\KBs\\Forgot_My_Password.pdf"  # Replace with the actual path
            
            # 4. Upload the file using the Files API
            uploaded_file = genai.upload_file(file_path)
            
            # 5. Get the URI of the uploaded file
            file_uri = uploaded_file.uri
            print(f"Successfully uploaded file. URI: {file_uri}")

            # 6. You can now use this URI in your prompts
            model = genai.GenerativeModel(model_name="gemini-2.0-flash") # Or a model that supports file input
            response = model.generate_content([file_uri, "Summarize the main points of this document."])
            print(response.text)
        except Exception as e:
            print(f"An error occurred: {e}")