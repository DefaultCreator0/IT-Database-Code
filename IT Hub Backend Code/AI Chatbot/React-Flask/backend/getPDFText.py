from docx import Document
import os

def extract_text_from_docx(docx_path):
    """
    Extracts text content from a local DOCX file.

    Args:
        docx_path (str): The full path to the local DOCX file.

    Returns:
        str: The extracted text content, or None if an error occurs.
    """
    try:
        document = Document(docx_path)
        text = ""
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"  # Add newline to separate paragraphs
        return text
    except FileNotFoundError:
        print(f"Error: File not found at {docx_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the DOCX file: {e}")
        return None

# Specify the path to your local DOCX file
local_docx_path = r"F:\AI Chatbot\Python_AI_Code\KBs\Using_the_AI_Chatbot.docx"

def getDocx():
    docx_content = extract_text_from_docx(local_docx_path)
    return docx_content


# Read the content of the DOCX
getDocx()

