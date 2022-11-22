from vds import  VDSpackage
from vds import VDS
from vds import VDS
import time
from fastapi import FastAPI






vds = VDS()

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    print("Server gestartet")

@app.get("/alarm")
async def alarm():
    print("Alarm eingetretten")

print("Hallo")



#while True:
   # print(".")
