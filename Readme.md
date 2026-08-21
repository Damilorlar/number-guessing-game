# Number Guessing Game

A CLI number guessing game that gives intelligent feedback to the player, tracks attempts, and supports multiple difficulty levels.

## What it does 

The computer secretly picks a number within a range (based on difficulty). The player guesses repeatedly, and after each guess the program tells them whether to go higher or lower. The game ends when the player guesses correctly or runs out of attempts, then shows a summary of; Attempts used, win/loss, and the score.

## Prerequisites

- Python 3 installed on your machine
- Ability to run a `.py` file from the terminal

## How to run it 

```bash
cd number-guessing-game
python3 game.py
```
> On Windows, use `python game.py` if `python3` isn't recognized.

## Difficulty levels

| Difficulty | Range | Attempts |
|------------|-------|----------|
| Easy       | 1–50  | 10       |
| Medium     | 1–100 | 7        |
| Hard       | 1–200 | 5        |

## Project structure
 
```
number-guessing-game/
├── game.py          ← main game logic
├── utils.py         ← helper functions (score calculator, input validator)
└── README.md        ← this file
```

## Scoring
 
```
score = (max_attempts - attempts_used + 1) * difficulty_multiplier
```

## Status
 
Core game (Steps 1–7) in progress. Extensions (leaderboard, hints, hot/cold mode) not yet built.
 

 ## Team - Group A
 
Built as part of Project 1.1 for Learn2Earn NG.