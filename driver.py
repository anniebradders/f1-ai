# driver.py
# circuit.py
import fastf1

class Driver(object):

    def __init__(self, driverName):
        self.driverName = driverName

    def getDriverInfo(self, session):
        session = session.get_race()
        session.load(telemetry=False, laps=False, weather=False)

        driverAb = self.driverName[:3]

        driverInfo = session.get_driver(driverAb.upper())
        return driverInfo
