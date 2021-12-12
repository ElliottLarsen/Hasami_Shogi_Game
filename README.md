# Hasami Shogi Game 

This is a console version of Hasami Shogi written in Python.  It follows the rules for "Variant 1" found [here](https://en.wikipedia.org/wiki/Hasami_shogi).  Blue(B) and Orange(O) pieces are used and the Blue player must make the first move.  This is the initial board configuration:



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
<h3 align = "right"> Elliott Larsen </h3>