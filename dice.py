import random 
from socket32 import Socket32, create_new_socket


def send(conn: Socket32, message: str):
    conn.sendall(message + "\n")

def recv(conn: Socket32) -> str | None:
    msg = conn.recv()
    if not msg:
        return None
    return msg.strip()


def remove_piece(board, conn, player_marker):
    if not any(player_marker in row for row in board):
        send(conn, f"No '{player_marker}' pieces on the board to remove.")
        return False

    while True:
        send(conn, f"Select a '{player_marker}' piece to remove (1-9): ")
        response = recv(conn)

        if response is None:
            raise ConnectionError("Player disconnected during remove_piece.")

        if not response.isdigit():
            send(conn, "Invalid input. Enter a number 1-9.")
            continue

        move = int(response)
        if move < 1 or move > 9:
            send(conn, "Please enter a number between 1-9.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] != player_marker:
            send(conn, f"That spot does not contain '{player_marker}'. Try again.")
            continue

        board[row][col] = " "
        send(conn, f"Removed '{player_marker}' piece.")
        return True


# dice 1 will have a 1/6 chance for removing opponents or your own piece. 4/6 chance for null and placing a piece like normal game play

def roll_dice_one(board, active_conn, active_marker, opponent_marker):
    roll = random.randint(1, 6)
    send(active_conn, f"\nYou rolled a {roll}!")

    if roll == 1:
        send(active_conn, f"Remove one of Player {opponent_marker}'s pieces.")
        return remove_piece(board, active_conn, opponent_marker)

    elif roll == 6:
        send(active_conn, "You must remove one of your own pieces.")
        return remove_piece(board, active_conn, active_marker)

    else:
        send(active_conn, "Go ahead and just place your piece.")
        return False

# dice 2 will have a 1/4 chance for removing opponents or your own piece. 1/2 chance for null and placing a piece like normal game play

def roll_dice_two(board, active_conn, active_marker, opponent_marker):
    roll = random.choice([1, 2, 5, 6])
    send(active_conn, f"\nYou rolled a {roll}!")

    if roll == 1:
        send(active_conn, f"Remove one of Player {opponent_marker}'s pieces.")
        return remove_piece(board, active_conn, opponent_marker)

    elif roll == 6:
        send(active_conn, "You must remove one of your own pieces.")
        return remove_piece(board, active_conn, active_marker)

    else:
        send(active_conn, "Go ahead and just place your piece.")
        return False
  
# dice 3 will have a 1/2 chance for opponents opps or your own piece.
def roll_dice_three(board, active_conn, active_marker, opponent_marker):
    roll = random.choice([1, 6])
    send(active_conn, f"\nYou rolled a {roll}!")

    if roll == 1:
        send(active_conn, f"Remove one of Player {opponent_marker}'s pieces.")
        return remove_piece(board, active_conn, opponent_marker)

    else:
        send(active_conn, "You must remove one of your own pieces.")
        return remove_piece(board, active_conn, active_marker)
