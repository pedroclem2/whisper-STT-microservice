from pydantic import BaseModel

class TranscriptionResponse(BaseModel):
    text: str
    
#this class defines the structure of the response for the api endpoint, 
#including the original text, its processed/translated version, and the language information.
