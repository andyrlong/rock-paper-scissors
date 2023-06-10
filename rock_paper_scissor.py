import random

def play():
   user = input("Rock, Paper, or Scissor? 'R' for rock, 'P' for paper, 'S' for scissors: ")
   computer = random.choice(['R', 'P', 'S'])
   
   if user == computer:
        return 'It\'s a tie!'
   if is_win(user, computer):
        return 'You win!'
   return 'You lose!'

def is_win(player, opponent):
   # Return true if player wins  
   if (player == 'R' and opponent == 'P') or (player == 'P' and opponent == 'R') \
       or (player == 'S' and opponent == 'P'):
       return True
   
print(play())

