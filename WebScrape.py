from bs4 import BeautifulSoup
from urllib.request import urlopen

page = urlopen("https://www.cnet.com/pictures/video-games-mario-zelda-nintendo-switch/")

soup = BeautifulSoup(page)

games = soup.findAll('h2')
captions = soup.findAll('p')

top_games = {}
games2 = []
url = 'https://www.cnet.com/pictures/video-games-mario-zelda-nintendo-switch/'

for game in games:
  game_name = game.getText().strip()
  games2.append(game_name)

games2.remove(games2[len(games2)-1])
for i in range(len(games2)-1):
  top_games[games2[i]] = (url + str(i+1))

num_games = 0
for game in top_games:
  num_games += 1
  print(str(game) + ": " + str(top_games[game]))
  print('')

print('')
print(num_games)