from fastapi import FastAPI, File, UploadFile, HTTPException
from application import parse_invoice_pdf
app = FastAPI()

@app.get("/processfile")
def processfile(filepath:str):
    return parse_invoice_pdf(filepath)