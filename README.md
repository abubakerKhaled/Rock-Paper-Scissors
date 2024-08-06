# Rock, Paper, Scissors Game

This is a simple implementation of the classic game Rock, Paper, Scissors. The player chooses between rock, paper, or scissors, and the computer randomly selects one of the three as well. The winner is determined based on the standard rules: rock beats scissors, scissors beats paper, and paper beats rock.

## How to Play

1. Run the program.
2. Enter your choice when prompted: 'r' for rock, 'p' for paper, or 's' for scissors.
3. The computer will randomly select its choice.
4. The program will determine the winner and display the result.

## Code Implementation

### Main Game Logic

The `play` function contains the main logic for the game. It prompts the user for their choice, randomly selects the computer's choice, and determines the winner.

```python
import random

def play():
    user = input("What's your choice?\n'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You win!"
    
    return "You lost!"
    
    
def is_win(user, computer):
    # return true if user is win
    # r>s , s>p, p>r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    
    
print(play())
```

### Function Explanation

- `play()`: Prompts the user for their choice and randomly selects the computer's choice. It then determines the winner based on the rules.
- `is_win(user, computer)`: Checks if the user's choice beats the computer's choice and returns `True` if the user wins.

## Areas for Improvement

1. **Input Validation**: Ensure that the user's input is valid ('r', 'p', or 's'). If the input is invalid, prompt the user to enter a valid choice.
2. **Extending Game Logic**: Add functionality to play multiple rounds and keep track of the score.
3. **Enhancing User Experience**: Improve the user interface by adding more descriptive messages and handling edge cases.

## Conclusion

This Rock, Paper, Scissors game provides a simple and fun way to play the classic game against the computer. The code can be further improved by adding input validation, extending game logic to multiple rounds, and enhancing the user experience.