# Game-of-Hog

1. Introduction

  This is the course project from UCB CS 61A: Structure and Interpretation of Computer Programs, which is the Game of Hog. 
  
  In this project, simulators and the rules of the dice game Hog were designed, and the corresponding Graphical User Interface
  was created for users to play a fully interactive version of Hog!

  Higher ordered functions and control statements were the main techniques in designing and employing game strategies and rules.
  Feel free to check them out in the code.

2. Rules

To spice up the game, we will play with some special rules:

  Pig Out. If any of the dice outcomes is a 1, the current player's score for the turn is 1.

    Example 1: The current player rolls 7 dice, 5 of which are 1's. They score 1 point for the turn.
    
    Example 2: The current player rolls 4 dice, all of which are 3's. Since Pig Out did not occur, 
    they score 12 points for the turn.

  Free Bacon. A player who chooses to roll zero dice scores the one more than the last digit of the product of the digits
  in the opponent's score.

    Example 1: The opponent has 46 points, and the current player chooses to roll zero dice. 4 * 6 = 24; 
    the last digit is a 4, so the current player gains 4 + 1 = 5 points.
    
    Example 2: The opponent has 28 points, and the current player chooses to roll zero dice. 2 * 8 = 16;
    the last digit is a 6, so the current player gains 6 + 1 = 7 points.
    
    Example 3: The opponent has 5 points, and the current player chooses to roll zero dice. 0 * 5 = 0;
    the last digit is a 0, so the current player gains 0 + 1 = 1 point.
  
  Swine Swap. After points for the turn are added to the current player's score, if the ones digit of the current player's score
  is the same as the tens digit of the opponent's score, the two scores are swapped.

    Example 1: The current player has a total score of 41 and the opponent has 92.
    The current player rolls two dice that total 8. The player's new score is 49,
    and the opponent's score is 92. The ones and tens digits are the same (49 and 92), 
    so the scores are swapped! The current player now has 92 points and the opponent has 49. The turn ends.
    
    Example 2: The current player has a total score of 34 and the opponent has 5.
    The current player rolls three dice that total 6.
    The player's new score is 40, and the ones digit is the same as the opponent's tens digit (40 and 05),
    so the scores are swapped. The current player now has 5 points and the opponent has 40.
    
    Example 3: The current player has a total score of 91 and the opponent has 12.
    The current player rolls five dice that total 20.
    The player's new score is 111, and the ones digit is the same as the opponent's tens digit (111 and 12),
    so the scores are swapped. The opponent ends the turn with 111 points and wins the game.

3. Files

  Files in the project:

    hog.py: A starter implementation of Hog
    
    dice.py: Functions for rolling dice
    
    hog_gui.py: A graphical user interface for Hog
    
    ucb.py: Utility functions for CS 61A
    
    images: A directory of images used by hog_gui.py

