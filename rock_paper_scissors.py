import random

def play():
    user = input("What's your choice?\n'r' for rock, 'p' paper, and 's' scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a tie"
    
    # r>s , s>p, p>r

    if is_win(user, computer):
        return "You win!"
    
    return "You lost!"
    
    
def is_win(user, computer):
    # return true if user is win
    # r>s , s>p, p>r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    
    
print(play())