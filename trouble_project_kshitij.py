# -*- coding: utf-8 -*-
"""Trouble Project- Kshitij.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3Ci88d4lAgKYkQkMnCPmG5vmCNs2Z3h

# **Trouble Project**
## Kshitij Gurung, 4/16/2020

In the game Trouble the goal is to move a bunch of markers from a starting point all the way to
the ending point. Ignoring some subtleties of the game, the basic move is very simple:
- You roll a standard 6-sided die.
- You move your marker the number of spaces equal to the value on the die.
- If you rolled a six, you roll and move again. You keep doing this as a long as you roll sixes.

For example, if you roll a 3, then you move 3 spaces. If you roll a 6 followed by a 3, then you move
6 + 3 = 9 spaces. If you roll a 6, another 6, and then a 3, then you move 6 + 6 + 3 = 15 spaces.
"""

import matplotlib.pyplot as plt
import random
import numpy

"""### A Move function

This is a move function with a roll-again value of 6, which returns the move length after a dice is rolled.
"""

def move_6():
  roll = 6
  total = 0
  while (roll== 6):
    roll = random.randint(1,6)
    total = total + roll
  return total

"""# Your Task
### 1) What is the average **length** of a move?

We are going to run move_6() funciton in a for loop for 10000 times and take the average move length.
"""

move_list = [move_6() for i in range(10000)];
numpy.mean(move_list)

"""- Based on 10,000 iterations, the average length seems to be around 4.20

### 2. How does the average length of a move depend on the roll-again value? That is, if you change the rules so that you roll again after rolling a 1, what is the average length of a move? Do this for all six possible roll-again values.

We created a new function with similar idea as before. Here, the roll-again value is set at 1.
"""

def move_1():
  roll = 1
  total = 0
  while (roll== 1):
    roll = random.randint(1,6)
    total = total + roll
  return total

move_list = [move_1() for i in range(10000)];
numpy.mean(move_list)

"""- Suprisingly, the average length seems to be around 4.19, which is close to previous value for roll-again 6.

- Let's try to find the average move length for all six roll-gain values. The function move_r()  accepts roll-again value and returns the move length.
"""

def move_r(r):
  roll = r
  total = 0
  while (roll== r):
    roll = random.randint(1,6)
    total = total + roll
  return total

"""- Lets run a loop for all six roll-again values."""

for i in range(1,7):
  move_list = [move_r(i) for j in range(5000000)];
  print(numpy.mean(move_list))

"""- Turns out, the average move length seem to be similar across all six-roll again values, averaging around 4.2. This is very interesting becasue I initially thought that the roll-again value of 6 would have the biggest average length.

### 3. Suppose you are playing a head-to-head game with another person. You use the “roll again on 1” rule, the other person uses the “roll again on 6” rule. You both roll your die to complete a move. The winner is who ever has a the larger move. (If there is a tie, repeat until there is a winner.) Is this a fair game, in the sense that both players have an equal probability of winning? If not, who has the advantage? How can you explain this, given what you found **for** question 2?

-  Based on the conclusion found on question 2, I think this is a fair game. No matter what roll again values we choose between 1 to 6, the average move length is going to be the pretty similar, averaging around 4.2. 
- The probability of getting 1 or 6 (roll-again value) is 1/6 each and twice in a row is 1/36, which is very small probability.

### 4. What is the distribution of move lengths for each roll again value? Make a histogram of move lengths for at least 1000 simulations of each roll-again value. How does this help you understand what you found for question 3?

- For roll again value of 1.
"""

move_list4=[move_r(1) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again:1  ");

"""- For roll again value of 2."""

move_list4=[move_r(2) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again: 2");

"""- For roll again value of 3."""

move_list4=[move_r(3) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again: 3");

"""- For roll again value of 4."""

move_list4=[move_r(4) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again: 4");

"""- For roll again value of 5."""

move_list4=[move_r(5) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again: 5");

"""- For roll again value of 6."""

move_list4=[move_r(6) for i in range(10000)]
n, bins, patches = plt.hist(move_list, color = 'g', edgecolor = 'y', bins = 50, zorder = 2)
plt.grid(zorder = 0)
plt.xlabel("Move length")
plt.ylabel("Frequency")
plt.title("Histogram of distribution of move length for roll-again: 6");

"""- As clearly seen in the histograms, the distribution of move length for all 1 to 6 roll-again values are pretty much same. This makes be believe that regardless of the roll-again value, the move length is the same in average. 
- They all have right skewed distribution.
- The game is fair.

# Conclusion
- We found out that no matter what roll-again value we pick (between 1 to 6), the average length seems to be farily same, averaging around 4.2. 
- If we were to play this game with someone with different roll-agian values, the game would be a fair battle. 

# Limitation and future work  
- We could do some more descriptive statistics and looked at the standard deviation, and compared different roll-again values. 
- As mentioned in the optional part, we could do some hypothesis testing and find statistical evidence for the fair nature of the game. 
- Thought, it is out of the scope of this course, but usining probabilites and finding the exact average length could be interesing.
"""