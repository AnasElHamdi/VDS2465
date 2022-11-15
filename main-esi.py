from vds import VDS
from collections import deque
from vds import VDSpackage
import time

class Que():
    def Warteschlange(self,):
#definieren einer Liste
        q = deque
        q.append = ('0000')

#versuch Object chars zu übergeben als test
       # q.append = object.ID_chars

        print(q)

#Que leeren nachdem sie benutz wurde damit sie wieder befüllt werden kann
        (q.popleft())
        print(q)
#Starten der vds 
vds = VDS()


while True:
    print(".")
    time.sleep(5)
