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

@app.get("/alarm/{id}")
async def alarm(id):
    print("Alarm eingetretten")
    print(id)
    vds.queue.append(id)
    return("Alarm entgegengenommen")
@app.get("/warteschlange")
async def warteschlange():
    return(vds.queue)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
print("Goodbye")



#while True:
   # print(".")
