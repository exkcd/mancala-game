# Report: Mancala Game

Name(s): Alex Schwarz, Rey Stone

Project name: We Can Never Get It Back, Can We?

## Current state

For this project, we have chosen to simulate the game of Mancala, with the rules stated in the project overview. We have successfully implemented the Mancala game from a previous homework assignment, as well as took the creative liberty of adding some new functions to make sure the game ran properly. A list of those functions can be found below.

check_win: self explanatory, checks who won in the case that winning_eval is true
switch_player: Switch acting player
get_pit_index: get current pit
print_moves: print which pit the current player selected
capture_stones: captures stones, increasing the mancala of whoever captured the stones

So far, both random players are working and fully functional. We have code in the `output.py` file that runs through one hundred Mancala games and then reports all of the statistics afterwards. 

There is not a first move advantage, this makes sense since both players are playing randomly for now.