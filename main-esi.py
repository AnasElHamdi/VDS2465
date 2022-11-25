from vds import  VDSpackage
from vds import VDS
from vds import VDS
import time
from fastapi import FastAPI
import uvicorn






vds = VDS()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Server gestartet")

@app.get ("/{Postleitzahl}")
async def Postleitzahl():
    print("Test")
    vds.queue.append(Postleitzahl)
    return("Okayö")

@app.get("/{alarm}")
async def alarm():
    print("Was ist das?")
    print(alarm)
    vds.queue.append(alarm)
    return("Was auch immer das ist!")

@app.get("/{alarm}/{id}")
async def alarm(id):
    print("Alarm eingetretten")

#   Konventieren der ID in int/bytes
    intid = int(id)
    vds.byteid = intid.to_bytes(2,'big')
    vds.queue.append(vds.byteid)
    return("Alarm entgegengenommen")

@app.get("/warteschlange/welche/nr")
async def warteschlange():
    return ("Vor ihnen sind:"),(len(vds.queue)),("Alarme")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
print("Goodbye")
#while True:
   #print(".")
