#!/usr/bin/env python3
# ========================================================================
# galaga.py
#
# Description: A basic implementation of a Galaga-type game on the
#              Sense HAT.
#
# pip3 install pygame
#
# Author: Jim Ing
# Date: 2024-09-04
# ========================================================================

import pygame
from time import sleep, time
import os
import random
import threading
from config import sense

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() < 1:
    raise RuntimeError("No joystick connected")

# Get the first connected joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Get the current rotation of the Sense HAT
rotation = sense.rotation

# Game Variables
score = 0
lives = 10
fighter_pos = 3  # Fighter starts in the middle of the bottom row
aliens = []
bullets = []
game_over = False

# Colors
fighter_color = (0, 255, 0)
alien_color = (255, 0, 0)
bullet_color = (255, 255, 255)
bg_color = (0, 0, 0)

# Button indices for the joystick
BTN_A = 1 # for secondary actions, like confirming choices in menus, jumping, or performing special actions
BTN_B = 2 # for primary actions, such as running, attacking, or canceling options in menus
BTN_X = 0 # for alternative actions or context-sensitive functions, such as changing weapons or using items
BTN_Y = 3 # for primary attacks or secondary movement, like running or dashing
DPAD_HORIZONTAL = 0
DPAD_VERTICAL = 1

# Alien movement variables
alien_move_interval = 0.75  # Time in seconds between alien movements
last_alien_move_time = time()  # Initialize the timer with the current time

def print_at(x, y, text):
    # Move the cursor to the specified position, clear the line, and print the text
    print(f"\033[{y};{x}H\033[2K{text}")

def draw_fighter():
    sense.set_pixel(fighter_pos, 7, fighter_color)

def move_fighter(direction):
    global fighter_pos
    if rotation == 0:
        if direction == 'left' and fighter_pos > 0:
            fighter_pos -= 1
        elif direction == 'right' and fighter_pos < 7:
            fighter_pos += 1
    elif rotation == 90:
        if direction == 'left' and fighter_pos < 7:
            fighter_pos += 1
        elif direction == 'right' and fighter_pos > 0:
            fighter_pos -= 1
    elif rotation == 180:
        if direction == 'left' and fighter_pos < 7:
            fighter_pos += 1
        elif direction == 'right' and fighter_pos > 0:
            fighter_pos -= 1
    elif rotation == 270:
        if direction == 'left' and fighter_pos > 0:
            fighter_pos -= 1
        elif direction == 'right' and fighter_pos < 7:
            fighter_pos += 1

def fire_bullet():
    bullets.append([fighter_pos, 6])  # Fire bullet from just above the fighter

def move_bullets():
    global score
    for bullet in bullets:
        bullet[1] -= 1
        if bullet[1] < 0:  # If bullet is off the screen
            bullets.remove(bullet)
        else:
            # Check if bullet hits an alien
            for alien in aliens:
                if bullet == alien:
                    aliens.remove(alien)
                    bullets.remove(bullet)
                    score += 1
                    break

def spawn_alien():
    # Only spawn a new alien if there are fewer than 5 aliens on the screen
    if len(aliens) < 3:
        new_alien = [random.randint(0, 7), 0]  # Random position at the top
        aliens.append(new_alien)

def move_aliens():
    global lives, game_over, last_alien_move_time
    current_time = time()
    if current_time - last_alien_move_time >= alien_move_interval:
        last_alien_move_time = current_time
        for alien in aliens:
            alien[1] += 1
            if alien[1] > 7:  # If alien reaches the bottom row
                aliens.remove(alien)
                lives -= 1
                if lives == 0:
                    game_over = True

def draw_screen():
    sense.clear()
    draw_fighter()
    for bullet in bullets:
        sense.set_pixel(bullet[0], bullet[1], bullet_color)
    for alien in aliens:
        sense.set_pixel(alien[0], alien[1], alien_color)

def handle_gamepad_events():
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == BTN_B:
                    fire_bullet()
            elif event.type == pygame.JOYAXISMOTION:
                if event.axis == DPAD_HORIZONTAL:
                    if event.value < -0.5:
                        move_fighter('left')
                    elif event.value > 0.5:
                        move_fighter('right')

# Start Gamepad event handling in a separate thread
gamepad_thread = threading.Thread(target=handle_gamepad_events)
gamepad_thread.daemon = True
gamepad_thread.start()

os.system('clear')  # Clear the screen

# Main Game Loop
while not game_over:
    spawn_alien()
    move_bullets()
    move_aliens()
    draw_screen()

    # Print score and lives to the console
    print_at(1, 1, f"Score: {score}  Lives: {lives}")

    sleep(0.1)  # Game speed

# Game Over
print(f"Game Over! Final Score: {score}")
sense.show_message(f"Score: {score}", text_colour=[255, 0, 0])
sense.clear()

# Quit Pygame
pygame.quit()
