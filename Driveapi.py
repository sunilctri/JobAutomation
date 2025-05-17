FolderID = "14CLpWbbcbFNCQCKSJk7riYasMIzp6WuA"
# Get Optimise Resume!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload # Corrected import
from google.oauth2 import service_account

def addtodrive(html,company, title):
    FolderID = "14CLpWbbcbFNCQCKSJk7riYasMIzp6WuA"
    SCOPES = [ 
        'https://www.googleapis.com/auth/documents',
        'https://www.googleapis.com/auth/drive'
    ] 

    credentials = service_account.Credentials.from_service_account_file(
        'resumeapi-458801-7777b8f2097a.json',
        scopes=SCOPES 
    )

    drive_service = build('drive', 'v3', credentials=credentials)


    file_metadata = {
        'name': f"{title}_{company}_resume", 
        'mimeType': 'application/vnd.google-apps.document', 
        'parents': [FolderID]
    }

    media = MediaIoBaseUpload(
        io.BytesIO(html.encode('utf-8')), # Source content
        mimetype='text/html',            # Source MIME type
        resumable=True                   # Optional: Use resumable upload
    )


    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        supportsAllDrives=True,
        fields='id'
    ).execute()
    return file.get('id')

#print(f"File created with id: {file.get('id')}")