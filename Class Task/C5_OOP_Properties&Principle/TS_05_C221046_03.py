# Encapsulation - for public private


# Base class representing a generic Player
class Player:
    def play(self):
        # Abstract method to be implemented by subclasses
        pass

# Class representing a Cricket Player, inheriting from Player
class CricketPlayer(Player):
    def __init__(self, plays = "Cricket"):
        # "__" defines for private variable
        self.__plays = plays  # Type of game the player plays

    def play(self):
        # Override the play method to provide specific implementation
        return f"Cricket Player plays {self.__plays}"

# Class representing a Football Player, inheriting from Player
class FootballPlayer(Player):
    def __init__(self, plays = "Football"):
        # "__" defines for private variable
        self.__plays = plays  # Type of game the player plays

    def play(self):
        # Override the play method to provide specific implementation
        return f"Football Player plays {self.__plays}"
    
# Creating instances of CricketPlayer and FootballPlayer
cricket_player = CricketPlayer("Cricket")  # A cricket player
football_player = FootballPlayer("Football")  # A football player

# Calling the play method for both players
print(cricket_player.play())  # Output: Cricket Player plays Cricket
print(football_player.play())  # Output: Football Player plays Football

print(cricket_player.__plays) #Not accessable