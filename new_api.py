from fastapi import FastAPI
from langdetect import detect
from textblob import TextBlob

app = FastAPI()

testo = ""

@app.get("/input")

def user(testo):
    lingua = detect(testo)
    return f"La lingua rilevata è: {lingua}"

@app.get("/input1")
def user(testo):
    blob = TextBlob(testo)
    sentiment = blob.sentiment.polarity
    return sentiment

