import fastf1
from circuit import Circuit
from team import Team
from driver import Driver

trackName = input("Please enter a track name: ")
year = int(input("Please enter year: "))

track = Circuit(trackName, year)
track = Circuit.getCircuitInfo(track)

option = int(input("1) Get Team Details \n 2) Get Driver Details"))

if option == 1:
    teamName = input("Please enter team name: ")

    team = Team(teamName)
    team = Team.getTeamInfo(team, track)

    print(team)
else:
    driverName = input("Please enter driver name: ")

    driver = Driver(driverName)
    driver = Driver.getDriverInfo(driver, track)
    print(driver)







