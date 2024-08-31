#!/usr/bin/env python3
# ========================================================================
# galaga.py
#
# Description: A basic implementation of a Galaga-type game on the
#              Sense HAT.
#
# pip3 install evdev
#
# ls -l /dev/input/by-id
#
#   Example:
#   usb-Controller_Controller_Controller-event-joystick -> ../event6
#
# Author: Jim Ing
# Date: 2024-08-31
# ========================================================================

from evdev import InputDevice, categorize, ecodes
from time import sleep, time
import random
import threading
from config import sense

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

# Initialize Gamepad
gamepad = InputDevice('/dev/input/event6')  # Replace 'eventX' with the correct device file for your gamepad

# Button and D-Pad codes (these might vary depending on your gamepad model)
BTN_A = 304
BTN_B = 305
BTN_X = 307
BTN_Y = 308
DPAD_LEFT = 17  # Left/Right axis
DPAD_RIGHT = 16  # Up/Down axis

# Alien movement variables
alien_move_interval = 0.5  # Time in seconds between alien movements
last_alien_move_time = time()  # Initialize the timer with the current time

def draw_fighter():
    sense.set_pixel(fighter_pos, 7, fighter_color)

def move_fighter(direction):
    global fighter_pos
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
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            if event.value == 1:  # Button press
                if event.code == DPAD_LEFT:
                    move_fighter('left')
                elif event.code == DPAD_RIGHT:
                    move_fighter('right')
                elif event.code == BTN_A:  # A button for firing
                    fire_bullet()
        elif event.type == ecodes.EV_ABS:  # Handle D-Pad axis
            if event.code == DPAD_LEFT and event.value == -1:
                move_fighter('left')
            elif event.code == DPAD_RIGHT and event.value == 1:
                move_fighter('right')

# Start Gamepad event handling in a separate thread
gamepad_thread = threading.Thread(target=handle_gamepad_events)
gamepad_thread.daemon = True
gamepad_thread.start()

# Main Game Loop
while not game_over:
    spawn_alien()
    move_bullets()
    move_aliens()
    draw_screen()

    # Print score and lives to the console
    print(f"Score: {score}  Lives: {lives}")

    sleep(0.1)  # Game speed

# Game Over
print(f"Game Over! Final Score: {score}")
sense.show_message(f"Score: {score}", text_colour=[255, 0, 0])
sense.clear()
