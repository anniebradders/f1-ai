# circuit.py
import fastf1

class Circuit(object):

    def __init__(self, circuitName, year):
        self.circuitName = circuitName
        self.year = year

    def getCircuitInfo(self):
        session = fastf1.get_event(self.year, self.circuitName)
        return session


