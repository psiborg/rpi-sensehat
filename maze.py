#!/usr/bin/env python3
# ========================================================================
# maze.py
#
# Description: Maze game that a player can navigate using either the
#              mini joystick, a USB gamepad or a keyboard. The objective
#              is to reach the green goal.
#
# pip3 install pygame
#
# Author: Jim Ing
# Date: 2024-08-26
# ========================================================================

import curses
import pygame
import random
from threading import Thread
from time import sleep
from config import sense

# Rotation mapping for WASD keys based on rotation degrees
KEYBOARD_ROTATION_MAP = {
    0: {
        ord('w'): (0, -1),  # Move up
        ord('s'): (0, 1),   # Move down
        ord('a'): (-1, 0),  # Move left
        ord('d'): (1, 0)    # Move right
    },
    90: {
        ord('w'): (1, 0),   # Move right
        ord('s'): (-1, 0),  # Move left
        ord('a'): (0, -1),  # Move up
        ord('d'): (0, 1)    # Move down
    },
    180: {
        ord('w'): (0, 1),   # Move down
        ord('s'): (0, -1),  # Move up
        ord('a'): (1, 0),   # Move right
        ord('d'): (-1, 0)   # Move left
    },
    270: {
        ord('w'): (-1, 0),  # Move left
        ord('s'): (1, 0),   # Move right
        ord('a'): (0, 1),   # Move down
        ord('d'): (0, -1)   # Move up
    }
}

# Initialize Pygame and the joystick
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    joystick = None

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
    """Generate a maze using a modified DFS algorithm to create more challenging mazes."""
    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
    random.shuffle(directions)  # Randomize directions

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 < nx < maze_size and 0 < ny < maze_size and maze[ny][nx] == 1:
            maze[ny][nx] = 0
            maze[ny - dy // 2][nx - dx // 2] = 0  # Break down wall between cells
            if random.random() > 0.3:  # Reduce backtracking to create more dead ends
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
    """Move the player if the move is valid, adjusted for rotation."""
    global player_pos
    rotation = sense.rotation

    # Adjust movement based on the current rotation
    if rotation == 90:
        dx, dy = dy, -dx
    elif rotation == 180:
        dx, dy = -dx, -dy
    elif rotation == 270:
        dx, dy = -dy, dx

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
    #print(f"direction = {event.direction}")
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
    """Handle keyboard movements using curses with rotation mapping."""
    stdscr.nodelay(True)  # Make getch non-blocking

    # Get the current rotation of the Sense HAT
    rotation = sense.rotation

    # Apply the appropriate keyboard mapping based on current rotation
    key_mapping = KEYBOARD_ROTATION_MAP[rotation]

    while True:
        key = stdscr.getch()
        if key in key_mapping:
            dx, dy = key_mapping[key]
            move_player(dx, dy)
        sleep(0.1)

def gamepad_movement():
    """Handle gamepad movements."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                x_axis = joystick.get_axis(0)
                y_axis = joystick.get_axis(1)
                if x_axis < -0.5:  # Left
                    move_player(-1, 0)
                elif x_axis > 0.5:  # Right
                    move_player(1, 0)
                if y_axis < -0.5:  # Up
                    move_player(0, -1)
                elif y_axis > 0.5:  # Down
                    move_player(0, 1)
            elif event.type == pygame.JOYBUTTONDOWN:
                # Additional button handling can be added here
                pass
        sleep(0.1)

def reset_game():
    """Reset the game after winning by generating a new maze and setting a new goal."""
    global player_pos, goal_pos, maze

    # Reset the player's position
    player_pos = [1, 1]

    # Generate a new random maze
    maze = [[1 for _ in range(maze_size)] for _ in range(maze_size)]
    maze[1][1] = 0
    generate_maze(1, 1)

    # Find a new reachable goal position
    goal_pos = find_reachable_goal()

    # Clear the Sense HAT and redraw the maze
    sense.clear()
    draw_maze()

try:
    print("To quit, press Ctrl+C")

    # Generate and draw the maze
    maze[1][1] = 0
    generate_maze(1, 1)
    goal_pos = find_reachable_goal()
    draw_maze()

    # Start joystick listener
    sense.stick.direction_any = joystick_movement

    # Start gamepad listener
    if joystick:
        Thread(target=gamepad_movement, daemon=True).start()

    # Start curses-based keyboard listener
    curses.wrapper(keyboard_movement)

except KeyboardInterrupt:
    sense.clear()
