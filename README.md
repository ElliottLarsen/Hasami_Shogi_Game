# Hasami Shogi Game 
This is a console version of Hasami Shogi written in Python.  It follows the rules for "Variant 1" found [HERE](https://en.wikipedia.org/wiki/Hasami_shogi).  Blue(B) and Orange(O) pieces are used and the Blue player must make the first move.  
<br>

## Technologies
---
* Python
<br>

## Game Walkthrough
---
This is the initial board configuration:
```
  1 2 3 4 5 6 7 8 9
a O O O O O O O O O
b . . . . . . . . .
c . . . . . . . . .
d . . . . . . . . .
e . . . . . . . . .
f . . . . . . . . .
g . . . . . . . . .
h . . . . . , . . .
i B B B B B B B B B
```
Here is a simple example of how the game can be played:
```python
hsg = HasamiShogiGame()
#hsg.play(oldCoordinate, newCoordinate)
hsg.play("i1", "b1")
hsg.play("a9", "h9")
```
which will display the following on your computer console:
```
  1 2 3 4 5 6 7 8 9 
a O O O O O O O O . 
b B . . . . . . . . 
c . . . . . . . . . 
d . . . . . . . . . 
e . . . . . . . . . 
f . . . . . . . . . 
g . . . . . . . . . 
h . . . . . . . . O 
i . B B B B B B B B 

0 Blue Pieces Have Been Captured.
0 Orange Pieces Have Been Captured.
```
<br>
<<<<<<< HEAD

## Contact
---
Elliott Larsen

* Email elliottlrsn@gmail.com
* GitHub [@elliottlarsen](https://github.com/elliottlarsen)
* LinkedIn [@elliottlarsen](https://www.linkedin.com/in/elliottlarsen)


<br>
<h3 align = "right"> Elliott Larsen </h3>
=======
<h3 align = "right"> Elliott Larsen </h3>
>>>>>>> 025721ff7e7e09b1f714aac3d8a953e431cea7f3
