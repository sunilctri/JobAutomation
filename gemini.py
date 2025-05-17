import google.generativeai as genai
import markdown
import os
import pandas as pd



def openmarkdownfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
        
systempromt= openmarkdownfile("systems.md")
#desc_md = openmarkdownfile("description.md")
resume_md = openmarkdownfile("resume.md")

def gemini(description):
    from google import genai
    # Hide the API key
    client = genai.Client(api_key="GEMINI KEY")

    response = client.models.generate_content(
    model="gemini-2.5-flash-preview-04-17",
    contents=f"Given are the  job description {description} and resume{resume_md}. Output should be markdown format with same layout",
    config={
        "temperature": 0,
        "system_instruction": systempromt
    }
)
    return response.text
