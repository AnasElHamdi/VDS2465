from vds import VDSpackage
from vds import VDS
from vds import VDS
import time
from fastapi import FastAPI
import uvicorn
import datetime
from pprint import pprint

vds = VDS()

app = FastAPI()
dt = datetime.datetime.now()
dt = dt.replace(microsecond=0) # Returns a copy
dt

@app.on_event("startup")
async def startup_event():
    print("Server gestartet")


@app.get("/{alarm}/{test}/2000")
async def alarm(test):
    print("Was ist das?")
    alarmid = int(test)
    vds.byteid = alarmid.to_bytes(2,'big')
    vds.queue.append(vds.byteid)

    #dringend aufräumen
    #Neue Liste wird Überprüft ob voll ist wenn ja dann erstelle neu Uhrzeit und verwende es als Angekommene Zeit
    if vds.Warte != 0:
        bt = datetime.datetime.now()
        bt = bt.replace(microsecond=0)  # Returns a copy
        bt
        pprint(dt,bt,vds.Warte)
        return ("die Abgeschickte AlarmID beträgt:",alarmid,"Die Sendezeit beträgt:",dt,"Der Alarm ist um:",bt,"angekommen",)



@app.get("/{alarm}/{id}")
async def alarm(id):
    print("Alarm eingetreten")
    #Konventieren der ID in int/bytes
    vds.Carsten.append(id)
    intid = int(id)

    print(type(intid))
    vds.byteid = intid.to_bytes(2, 'big')
    print(type(vds.byteid))
    vds.queue.append(vds.byteid)


    return ("Alarm entgegengenommen",)


@app.get("/warteschlange/welche/nr")
async def warteschlange():
    return "Vor ihnen sind:", (len(vds.queue)),"Alarme","Diese alarme wurden bereits Bearbeitet:",         vds.Carsten

    # Objekt printen mit den Infos (Von wo komme ich, wann bin ich gekommen, und dann wurde ich versendet)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
print("Goodbye")

# while True:
# print(".")
