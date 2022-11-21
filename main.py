def data(test):
    if "0000" in test:
        if "0004" in test:
            print("Doppelter Fehler")
            print("0000 und 0004")
        print("Alarm")
        print("0000 Fehlermeldung")
    elif "0004" in test:
        print("Alarm haha")
        print("0004 Fehler")