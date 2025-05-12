

from fastapi import FastAPI
#creare un'istanza della classe FASTAPI.
app = FastAPI()
#variabile globale di una lista vuota che utilizzerò nelle funzioni
nome_lista = []
#oggetto app, get è il metodo API, tra virgolette c'è il path.
@app.get("/")
#dichiarazione API
def homepage():
    return "Hello World"
#----------------------------------------------------------------------------------------------------
@app.get("/ciao")
def homepage(nome:str, cognome:str):
    return "ciao" + nome + cognome
#---------------------------------------------------------------------------------------------------
@app.post("/aggiungi-utente")
def user(username:str):    
    #metodo stringa che permette di aggiungere un elemento nella lista
    nome_lista.append(username)
    return "L'utente è stato aggiunto"
@app.get("/cerca-utente")
def cerca_utente(username):
    #controllo, si usa if
    if username in nome_lista:
        return "L'utente è presente nella lista"
    else:
        return "L'utente NON è nella lista"    
@app.get("/totale-utenti")
def conta_utenti():
    #len sta per length e qui si sta tornando la quantità di nomi salvati rispetto al precedente metodo user.
    return len(nome_lista)
@app.delete("/elimina-utente")
def elimina_utente(username):
    nome_lista.remove(username)
    return nome_lista
    
