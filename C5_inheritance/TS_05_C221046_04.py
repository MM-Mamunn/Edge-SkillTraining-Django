# Abstraction is like template class that defines what methods or shape the child classes will look like
# ABC and abstractmethod means that all the child of parent(Player) must have the "play" method defined,otherwise its an error
# alternative of this is in the next tast "TS_05.C221046.05.py" (alternative)
from abc import ABC,abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self):
        pass

class CricketPlayer(Player):
    def __init__(self, plays = "Cricket"):
        self.plays = plays 
    def play(self):
        return f"yes"        
cricket_player = CricketPlayer("Cricket")

print(cricket_player.play())  #its an error

