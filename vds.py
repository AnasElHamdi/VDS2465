import socket
import threading
from concurrent.futures.thread import _worker
import os
from datetime import datetime
from main import

HOST = "proof.hopto.org"  # The server's hostname or IP address
PORT = 1100  # The port used by the server
data = s.recv(1024)
class Debug():
    debugflag = os.environ.get("ESI_DEBUG_MODE","1")
    def print(self, msg):
        if self.debugflag == "1":
            now = datetime.now()
            nowstr = now.strftime("%d.%m.%Y %H:%M:%S")
            print(f"{nowstr}: {msg}")
        return True

d = Debug()


class VDSpackage():

    def __init__(self, data):
                self.ID_chars = data[0:4]
                self.CE_chars = data[8:10]
                self.ik_chars= data [14]
                self.pk_chars = data [15:16]
                self.LN_chars = data [16:17]
                self.KN_chars = bytearray(b'\x01')
                self.counterreceive_chars = data[4:8]
                self.countersend_chars = data[10:14]


    def inc_receive(self):
        d.print("increase receive")
        self.counterreceive_chars = bytearray(self.counterreceive_chars)
        self.counterreceive_chars[3]
        return [self.counterreceive_chars[3]]

    def inc_send(self):
        d.print("increase send")
        self.countersend_chars = bytearray(self.countersend_chars)
        self.countersend_chars[3] += 1
        return [self.countersend_chars[3]]

class VDS():
    def __init__(self):
                   # Initialisierung von VDS
        #self.vds = VDSpackage()
        self.thread = threading.Thread(target=self.worker) # Worker Thread starten.
        self.thread.start()
        d.print("Worker started")


    def worker(self):  # Async thread zur Kommunikation mit Empfänger
        d.print("Connect to Server")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            while True:
                #Client hört zu
                data = s.recv(1024)

                object = VDSpackage(data)

                Counter = 0


#hochzählen des Counters
                valuesreceive = object.inc_receive()
                valuessend = object.inc_send()

#Erstellen des Syncresponse
                if object.ik_chars == 0x1:
                    Counter += 1
                    object.CE_chars = bytes(2)
                    object.ik_chars = bytes(b'\x02')
                    SyncResponse = (object.ID_chars + object.countersend_chars + object.CE_chars + object.counterreceive_chars + object.ik_chars + object.pk_chars + object.LN_chars + object.KN_chars)
                    print('Sync Request incoming : ', SyncResponse, valuesreceive)
                    s.sendall(SyncResponse)

#Erstellen des Payload
                elif object.ik_chars == 0x4:
                    Counter += 1
                    object.LN_chars = (b'\x08')
                    object.CE_chars = bytes(2)
                    random = bytes(3)
                    object.ik_chars = bytes(b'\x04')
                    object.ID_charspay = object.ID_chars[3]
                    object.ID_charspay = bytes(b'\037')
                    object.ID_kennung = bytes(b'\x90') + (b'\x99') + (b'\x99')
                    object.Payload_Ack = bytes(b'\x06') + (b'\x56') + (b'\x00') + (b'\x00') + (b'\x00')
                    Payload =(object.ID_chars + object.countersend_chars + object.CE_chars + object.counterreceive_chars + object.ik_chars +object.pk_chars+ object.LN_chars + object.Payload_Ack + object.ID_kennung)
                    print('Payload incoming : ',Payload)
                    s.sendall(Payload)

#Data Request
                elif object.ik_chars == 0x3:
                    Counter += 1
                    print(Counter)
                    object.ik_chars = bytes(b'\x03')
                    DataRequest = (object.ID_chars + object.countersend_chars + object.CE_chars + object.counterreceive_chars + object.ik_chars + object.pk_chars + object.LN_chars)
                    print('Data request incoming : ', DataRequest, valuessend,valuesreceive)
                    s.sendall(DataRequest)
                    Counter += 1
#wenn etwas in der warteschlange steckt dann schicke den alarm ab 
#fehler bei der übergabe der warteschlange
                
                if len(q) != 0:
                    ID_chars = data[0:3]
                    ID_Alarmstufe = bytes(b'\x44')
                    LN_chars = bytes(b'\x37')
                    ik_chars = bytes(b'\x04')
                    alarm_linie = bytes (b'\x05') + (b'\x02') + (b'\x00') + (b'\x02') + (b'\x00') + (b'\x01') + (b'\x00') + (b'\x07') + (b'\x50') + (b'\x50') + (b'\x14') + (b'\x04') + (b'\x10') + (b'\x00') + (b'\x17')
                    alarm_code = bytes(b'\x36')
                    Alarm = (ID_chars + ID_Alarmstufe + countersend_chars + CE_chars + counterreceive_chars + ik_chars + pk_chars + LN_chars + alarm_linie + alarm_code)
                    print('Alarm:', ID_kennung , valuesreceive,valuessend)
                    s.sendall(Alarm)
                    print('erfolgreich')
                else:
                    s.sendall(DataRequest)

