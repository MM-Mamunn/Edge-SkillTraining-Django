# Polymorphism - for extensibility,code can be extended without modifying the orginal structure

# Base class representing a generic Player
class Player:
    def play(self):
        # Abstract method to be implemented by subclasses
        pass

# Class representing a Cricket Player, inheriting from Player
class CricketPlayer(Player):
    def __init__(self, plays):
        self.plays = plays  # Type of game the player plays

    def play(self):
        # Override the play method to provide specific implementation
        return f"Cricket Player plays {self.plays}"

# Class representing a Football Player, inheriting from Player
class FootballPlayer(Player):
    def __init__(self, plays):
        self.plays = plays  # Type of game the player plays

    def play(self):
        # Override the play method to provide specific implementation
        return f"Football Player plays {self.plays}"
    
# Creating instances of CricketPlayer and FootballPlayer
cricket = CricketPlayer("Cricket")  # A cricket player
football = FootballPlayer("Football")  # A football player

# Calling the play method for both players
print(cricket.play())  # Output: Cricket Player plays Cricket
print(football.play())  # Output: Football Player plays Football



# # Alternative
# # Polymorphism - for extensibility,code can be extended without modifying the orginal structure

# # Base class representing a generic Player
# class Player:
#     def play(self):
#         # Abstract method to be implemented by subclasses
#         pass

# # Class representing a Cricket Player, inheriting from Player
# class CricketPlayer(Player):
#     def play(self):
#         # Override the play method to provide specific implementation
#         return f"Cricket Player plays Cricket"

# # Class representing a Football Player, inheriting from Player
# class FootballPlayer(Player):
#     def play(self):
#         # Override the play method to provide specific implementation
#         return f"Football Player plays Football"
    
# # Creating instances of CricketPlayer and FootballPlayer
# cricket = CricketPlayer()  # A cricket player
# football = FootballPlayer()  # A football player

# # Calling the play method for both players
# print(cricket.play())  # Output: Cricket Player plays Cricket
# print(football.play())  # Output: Football Player plays Football
