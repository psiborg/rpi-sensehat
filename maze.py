#!/usr/bin/env python3
# ========================================================================
# maze.py
#
# Description: Maze game that the player can navigate using either the
#              mini joystick or the keyboard. The objective is to reach
#              the green goal.
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

import random
import curses
from sense_hat import SenseHat
from time import sleep
from threading import Thread

# Initialize Sense HAT
sense = SenseHat()

# Maze and player configuration
maze_size = 8  # 8x8 grid
wall_color = (0, 0, 255)  # Blue walls
path_color = (0, 0, 0)    # Black paths
player_color = (255, 255, 0)  # Yellow player
goal_color = (0, 255, 0)   # Green goal

# Initialize maze
maze = [[1 for _ in range(maze_size)] for _ in range(maze_size)]
player_pos = [1, 1]  # Start position
goal_pos = [maze_size - 2, maze_size - 2]  # Temporary goal position

def generate_maze(x, y):
    """Recursive Depth-First Search to generate a random maze."""
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 1 <= nx < maze_size - 1 and 1 <= ny < maze_size - 1 and maze[ny][nx] == 1:
            maze[ny][nx] = 0
            maze[y + dy // 2][x + dx // 2] = 0
            generate_maze(nx, ny)

def find_reachable_goal():
    """Find a reachable goal position by scanning from the bottom-right corner."""
    for y in range(maze_size - 2, 0, -1):
        for x in range(maze_size - 2, 0, -1):
            if maze[y][x] == 0:
                return [x, y]
    return [1, 1]  # Fallback in case no position is found

def draw_maze():
    """Draw the maze on the Sense HAT."""
    for y in range(maze_size):
        for x in range(maze_size):
            color = wall_color if maze[y][x] == 1 else path_color
            sense.set_pixel(x, y, color)
    sense.set_pixel(goal_pos[0], goal_pos[1], goal_color)
    sense.set_pixel(player_pos[0], player_pos[1], player_color)

def move_player(dx, dy):
    """Move the player if the move is valid."""
    global player_pos
    nx, ny = player_pos[0] + dx, player_pos[1] + dy

    if 0 <= nx < maze_size and 0 <= ny < maze_size and maze[ny][nx] == 0:
        sense.set_pixel(player_pos[0], player_pos[1], path_color)
        player_pos = [nx, ny]
        sense.set_pixel(player_pos[0], player_pos[1], player_color)
        check_goal()

def check_goal():
    """Check if the player has reached the goal."""
    if player_pos == goal_pos:
        sense.show_message("You Win!", text_colour=(255, 0, 0))
        reset_game()

def joystick_movement(event):
    """Handle joystick movements."""
    if event.action != 'pressed':
        return
    if event.direction == 'up':
        move_player(0, -1)
    elif event.direction == 'down':
        move_player(0, 1)
    elif event.direction == 'left':
        move_player(-1, 0)
    elif event.direction == 'right':
        move_player(1, 0)

def keyboard_movement(stdscr):
    """Handle keyboard movements using curses."""
    stdscr.nodelay(True)  # Make getch non-blocking
    while True:
        key = stdscr.getch()
        if key == ord('w'):
            move_player(0, -1)
        elif key == ord('s'):
            move_player(0, 1)
        elif key == ord('a'):
            move_player(-1, 0)
        elif key == ord('d'):
            move_player(1, 0)
        sleep(0.1)

def reset_game():
    """Reset the game after winning."""
    global player_pos, goal_pos
    player_pos = [1, 1]
    goal_pos = find_reachable_goal()
    sense.clear()
    draw_maze()

try:
    print ("To quit, press Ctrl+C")

    # Generate and draw the maze
    maze[1][1] = 0
    generate_maze(1, 1)
    goal_pos = find_reachable_goal()
    draw_maze()

    # Start joystick listener
    sense.stick.direction_any = joystick_movement

    # Start curses-based keyboard listener
    curses.wrapper(keyboard_movement)

except KeyboardInterrupt:
    sense.clear()
