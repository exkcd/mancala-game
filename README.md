# CSCI 3202 PROJECT: We can never get it back, can we?

Name(s): Alex Schwarz, Rey Stone

---

## Mancala rules being implemented

**There are many different rules sets for Mancala. Please read this before writing the code:**

- Players sit on opposite sides of the long edge of the board
- There are 6 small pits in the middle of the board and 2 large ones at each end. The small ones in the middle and the large pit on your right are yours. The small ones on the other side and the large pit to your opponent's right are theirs
- The large pits at the end of the board are called Mancalas
- Set up the board with 4 stones per small pit (none in the mancalas)
- On every turn, select a pit on your side of the board that contains one or more stones, then distribute its stones, one stone per pit, in an counter-clockwise direction until you have no stones remaining
- If you encounter your opponent's mandala, skip it
- If you encounter your mancala, drop a stone into it
- If the last stone lands in an empty pit on your side of the board, capture this stone and any stones in your opponent's pit on the other side of the board, collect all of these stones, including the one that just landed, and place them into your mancala.
- If either player's pits are entirely empty, the game concludes.
- The player who still has stones on his side of the board when the game concludes places all of these pieces into their mancala.
  The player with the most stones in their mancala is declared the winner. If both players have an equal number of stones in their mancala, the game results in a tie.

## Files

There are several files contianed in this repo integral for running the game.

- `MancalaGame.py` &rarr; contains the entire game file
- `formatting.py` &rarr; formats the shell output to look pretty
- `run.py` &rarr; runs the simulation of 100 games
- `report.md` &rarr; intermediate project report

## Playing the Game

Copy this repo and run the following commands.

```shell
git clone https://github.com/exkcd/mancala-game.git

cd mancala-game

python3 output.py
```
