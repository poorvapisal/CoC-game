## Clash-of-Clans terminal game

This application is a terminal based 2-D game in Python3, where the user can control either the king or the archer queen (different attacks), move it up, down, forward and backward, while destroying buildings and fighting defences (cannons and wizard towers) on its way. Concepts of object oriented programming are present within the code and the game simulates a basic version of Clash of clans. The objective of the game is to destroy as many buildings as possible including the townhall, and there will be an army of troops (archers, balloons and barbarians) to help the king/queen clean up. 

### Game play

Run: python3 play.py

- 0/1 - pick King/Queen as the hero
- w/s/a/d - control the King/Queen
- space - attack using King/Queen
- To spawn each kind of troops from the three points:
  - j/k/l - barbarians
  - b/n/m - archers
  - i/o/p - balloons
- r - rage spell
- h - heal spell
- q - quit the game

To watch the replay run: python3 replay.py

### Information

- **King** - Attacks a single location relative to the king with a sword.
- **Queen** - The Archer Queen will attack a distant AoE location with a volley of arrows. This location should be specified relative to the location of the queen, any building present in that location would be damaged by the queen’s arrows.
- **Barbarians** - The barbarians will always try to attack the nearest non-wall building and will always move towards it while destroying walls.
- **Archers** - Archers move similar to barbarians and can attack over walls and buildings i.e. they can attack anything in their range regardless of whether their path to the target is blocked or not.
- **Balloons** - Balloons prioritize attacking defensive buildings. Once all defensive buildings are destroyed, Balloons will then move destroying other non-wall buildings (similar to barbarians). Balloons can fly over walls and other buildings.
- **Cannons** - Attacks all the troops at a certain range from it.
- **Wizard Tower** - Attacks all the aerial troops at a certain range from it.

