# https://sc2reader.readthedocs.io/en/latest/
import sys
import sc2reader
import datetime
from sc2reader.engine.plugins import SelectionTracker, APMTracker
sc2reader.engine.register_plugin(SelectionTracker())
sc2reader.engine.register_plugin(APMTracker())

path = sys.argv[1]
sc2F = sc2reader.factories.SC2Factory()
replay = sc2F.load_replay(path)

class SC2ReplayData:
    def __init__(self, rawReplayData):
        self.gameType = rawReplayData.type
        # self.playerData
        self.winningTeam = rawReplayData.winner.number
        self.mapName = rawReplayData.map_name
        self.timePlayed = datetime.datetime.utcfromtimestamp(rawReplayData.unix_timestamp)
        self.timePlayedPretty = self.timePlayed.strftime('%Y-%m-%d %H:%M:%S')

# print('file name: ' + replay.filename)
# print('replay category: ' + replay.category)
# print('replay type: ' + replay.type)
# print('map: ' + replay.map_name)

# teamNum = 1
# for team in replay.teams:
#     print('Team ' + str(teamNum))
#     teamNum = teamNum + 1
#     for player in team.players:
#         print(player.name + ' - ' + player.play_race)
#     print('')

# add each action to appropriate player's total actions
# for i in range(0, len(replay.game_events)):
#     playerName = replay.game_events[i].player.name
#     if playerName in playersAPM:
#         playersAPM[playerName] += 1

for player in replay.players:
    print("Name: " + player.name)
    print("APM: " + str(player.avg_apm))
    print("Race: " + player.pick_race)

print(replay.date)

# for property, value in vars(replay.winner).items():
#     print(property)