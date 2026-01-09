AI Game Referee – Rock Paper Scissors Plus

This project implements a simple conversational game referee that runs a
3-round Rock–Paper–Scissors–Plus game.

State Model:
The game state is stored in a dictionary tracking round number, scores,
and bomb usage for both players.

Tool Design:
- validate_move: checks move validity and bomb constraints
- resolve_round: determines the winner of each round
- update_state: mutates game state after each round

Design Choices:
Logic, state handling, and user interaction are clearly separated.
The bot uses a simple random strategy for clarity and correctness.

Future Improvements:
With more time, I would add adaptive bot strategy and structured ADK schemas.
