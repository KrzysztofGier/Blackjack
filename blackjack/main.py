from game import Game
from exceptions import  GameOverCroupierException, GameOverUserException

try:
    game= Game()
    game.play()
except GameOverCroupierException:
    print('WYgrywa gracz')
except GameOverUserException:
    print('Wygral krupier')
    