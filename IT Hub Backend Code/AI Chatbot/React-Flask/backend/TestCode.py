import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("AIzaSyBS-jAuZwRNLbDsSoxuHtqlmd6kegQ9O5E"),
    )

    files = [
        # Please ensure that the file is available in local system working direrctory or change the file path.
        client.files.upload(file="Forgot My Password.pdf"),
    ]
    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""The user wants me to transcribe the text from the provided image.

1.  **Identify the main sections:** The image has a title, an overview, a list of steps, tips, and related articles.
2.  **Transcribe the title:** \"6. Forgot My Password\"
3.  **Transcribe the Overview section:** \"Overview: If you've forgotten your password, follow these steps to reset it and regain access to your account.\"
4.  **Transcribe the Steps section:**
    *   Identify the heading: \"Steps:\"
    *   Transcribe each numbered step:
        *   \"1. Navigate to the Help Desk login page.\"
        *   \"2. Click the \"Forgot Password?\" link located below the password field.\"
        *   \"3. Enter your registered email address in the provided field and click \"Submit.\"\"
        *   \"4. Check your email inbox for a password reset link. If you don't see it, check your spam or junk folder.\"
        *   \"5. Click the link in the email and follow the instructions to create a new password.\"
        *   \"6. Once your password is updated, return to the login page and enter your new credentials to access your account.\"
5.  **Transcribe the Tips section:**
    *   Identify the heading: \"Tips:\"
    *   Transcribe each bullet point:
        *   \"• Choose a strong password that includes a mix of uppercase letters, lowercase letters, numbers, and special characters.\"
        *   \"• Avoid using the same password for multiple accounts to enhance security.\"
6.  **Transcribe the Related Articles section:**
    *   Identify the heading: \"Related Articles:\"
    *   Transcribe each bullet point:
        *   \"• Troubleshooting Login Issues\"
        *   \"• How to Create and Manage Your Account\"
7.  **Review and format:** Ensure the transcription matches the original image, maintaining the structure (headings, numbered lists, bullet points). Check for any OCR errors. The transcription seems accurate and well-formatted."""),
                types.Part.from_text(text="""```text
6. Forgot My Password

Overview: If you've forgotten your password, follow these steps to reset it and regain access to your account.

Steps:
1. Navigate to the Help Desk login page.
2. Click the \"Forgot Password?\" link located below the password field.
3. Enter your registered email address in the provided field and click \"Submit.\"
4. Check your email inbox for a password reset link. If you don't see it, check your spam or junk folder.
5. Click the link in the email and follow the instructions to create a new password.
6. Once your password is updated, return to the login page and enter your new credentials to access your account.

Tips:
*   Choose a strong password that includes a mix of uppercase letters, lowercase letters, numbers, and special characters.
*   Avoid using the same password for multiple accounts to enhance security.

Related Articles:
*   Troubleshooting Login Issues
*   How to Create and Manage Your Account
```"""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
