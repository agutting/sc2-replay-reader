# https://sc2reader.readthedocs.io/en/latest/
import sys
from sc2reader.factories import SC2Factory

path = sys.argv[1]
sc2F = SC2Factory()
replay = sc2F.load_replay(path)

# print('file name: ' + replay.filename)
# print('replay category: ' + replay.category)
# print('replay type: ' + replay.type)
# print('map: ' + replay.map_name)

teamNum = 1
for team in replay.teams:
    print('Team ' + str(teamNum))
    teamNum = teamNum + 1
    for player in team.players:
        print(player.name + ' - ' + player.play_race)
    print('')

input("Press Enter to continue...")