# Terminal-Based Tic-Tac-Toe Game

A simple terminal-based Tic-Tac-Toe game built in Python. The game supports both single-player (against an AI opponent) and two-player modes.



## Features

- **Game Modes:**
  - Two-player mode for playing with a friend on the same terminal.
  - Single-player mode with an AI opponent.

- **Gameplay:**
  - Displays the Tic-Tac-Toe board after each move.
  - Validates user inputs to ensure moves are within bounds and on empty cells.
  - Detects game-ending conditions (win, loss, or draw) and announces the result.

- **AI Behavior:**
  - Makes strategic moves, including blocking the player’s winning moves and prioritizing the center or corners.


## Gameplay Input Format

### Starting the Game
- After running the game, we will be prompted to choose the game mode:
- Enter `two-player` to play with a friend.
- Enter `single-player` to play against the AI.

### Playing the Game
- The board is a 3x3 grid where each cell is identified by its row and column indices zero based.

#### Input Format
- **Row Index**: The row where we want to place your mark (values: `0`, `1`, `2`).
- **Column Index**: The column where we want to place your mark (values: `0`, `1`, `2`).

- The move is valid only if:
- The row and column values are between `0` and `2`.
- The selected cell is empty.

### Board Display
After every move, the updated board will be displayed:



## Project Setup

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/UtkJaiswal/tic-tac-toe.git
   cd tic-tac-toe
   ```


## Run the Game

```bash
python main.py
```