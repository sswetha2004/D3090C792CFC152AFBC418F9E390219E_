# define the base class player
class Player:
     def play(self):
          print("The player is playing cricket.")

# define the derived class Batsman
class Batsman:
    def play(self):
        print("The batsman is batting.")

# define the derived class Bowler
class Bowler:
       def play(self):
         print("The bowler is bowling.")

batsman=Batsman()
bowler=Bowler()

# call the play () method of each object
batsman.play()
bowler.play()
