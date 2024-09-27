# Abstraction is like template class that defines what methods or shape the child classes will look like1
from abc import ABC,abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self):
        pass

class CricketPlayer(Player):
    def __init__(self, plays = "Cricket"):
        self.plays = plays 
        
cricket_player = CricketPlayer("Cricket")

print(cricket_player.play())  #its an error

