import time

def addEvent(collection, eventType):
    collection.insert_one({"Event-type": eventType, "Time": time.asctime()})