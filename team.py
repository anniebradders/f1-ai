# team.py

class Team(object):

    def __init__(self, teamName):
        self.teamName = teamName

    def getTeamInfo(self, session):
        session = session.get_race()
        session.load(telemetry=False, laps=False, weather=False)
        team = []
        for drv in session.drivers:
            drvs = session.get_driver(drv)
            if drvs['TeamName'] == self.teamName:
                team.append(drvs)
        return team
