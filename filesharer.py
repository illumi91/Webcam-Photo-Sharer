from filestack import Client
import os
from dotenv import load_dotenv

load_dotenv()


class FileSharer:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = os.getenv("FILESTACK_API_KEY")
        
    def share(self):
        client = Client(self.api_key)
        
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url