# Rock Paper Scissors Plus Game
# Rules:
# - Best of 3 rounds
# - Moves: rock, paper, scissors, bomb
# - Bomb can be used only once per player
# - Bomb beats all moves
# - Invalid input wastes the round

state = {
    "round": 1,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False
}
def validate_move(move, bomb_used):
    valid_moves = ["rock", "paper", "scissors", "bomb"]

    if move not in valid_moves:
        return False

    if move == "bomb" and bomb_used:
        return False

    return True

def resolve_round(user_move, bot_move):
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"

    if bot_move == "bomb":
        return "bot"

    if user_move == "rock" and bot_move == "scissors":
        return "user"
    if user_move == "scissors" and bot_move == "paper":
        return "user"
    if user_move == "paper" and bot_move == "rock":
        return "user"

    return "bot"
def update_state(state, winner):
    if winner == "user":
        state["user_score"] += 1
    elif winner == "bot":
        state["bot_score"] += 1

    state["round"] += 1

import random

def bot_move(state):
    moves = ["rock", "paper", "scissors"]

    if not state["bot_bomb_used"]:
        moves.append("bomb")

    choice = random.choice(moves)

    if choice == "bomb":
        state["bot_bomb_used"] = True

    return choice
def play_game():
    print("Welcome to Rock Paper Scissors Plus!")
    print("Rules:")
    print("- Best of 3 rounds")
    print("- Moves: rock, paper, scissors, bomb")
    print("- Bomb can be used only once\n")

    while state["round"] <= 3:
        user_move = input(f"Round {state['round']} - Enter your move: ").lower().strip()

        # Validate user input
        if not validate_move(user_move, state["user_bomb_used"]):
            print("Invalid move! Round wasted.\n")
            state["round"] += 1
            continue

        # Mark user bomb usage
        if user_move == "bomb":
            state["user_bomb_used"] = True

        # Bot plays
        bot_choice = bot_move(state)

        # Decide winner
        winner = resolve_round(user_move, bot_choice)

        # Update state
        update_state(state, winner)

        print(f"Bot played: {bot_choice}")
        print(f"Round winner: {winner}\n")

    # Final result
    print("Game Over!")
    print("Your score:", state["user_score"])
    print("Bot score:", state["bot_score"])

    if state["user_score"] > state["bot_score"]:
        print("🎉 You win!")
    elif state["bot_score"] > state["user_score"]:
        print("🤖 Bot wins!")
    else:
        print("🤝 It's a draw!")
play_game()
