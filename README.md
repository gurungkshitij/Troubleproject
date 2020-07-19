# **Trouble Project**
## Kshitij Gurung, 4/16/2020

In the game Trouble, the goal is to move a bunch of markers from a starting point all the way to
the ending point. Ignoring some subtleties of the game, the basic move is very simple:
- You roll a standard 6-sided die.
- You move your marker the number of spaces equal to the value on the die.
- If you rolled a six, you roll and move again. You keep doing this as a long as you roll sixes.

For example, if you roll a 3, then you move 3 spaces. If you roll a 6 followed by a 3, then you move
6 + 3 = 9 spaces. If you roll a 6, another 6, and then a 3, then you move 6 + 6 + 3 = 15 spaces.

***My investigation:*** 
1) What is the average **length** of a move?
2) How does the average length of a move depend on the roll-again value? That is, if you change the rules so that you roll again after rolling a 1, what is the average length of a move? 
Do this for all six possible roll-again values.
3) Suppose you are playing a head-to-head game with another person. You use the “roll again on 1” rule, the other person uses the “roll again on 6” rule.
You both roll your die to complete a move. The winner is who ever has a the larger move. (If there is a tie, repeat until there is a winner.) Is this a fair game, in the sense that
both players have an equal probability of winning? 
If not, who has the advantage? How can you explain this, given what you found **for** question 2? 
4) What is the distribution of move lengths for each roll again value? Make a histogram of move lengths
for at least 1000 simulations of each roll-again value. How does this help you understand what you found for question 3?
5) Conclusion, Limitation, and Future work.
