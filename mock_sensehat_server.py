#!/usr/bin/env python3

import socket
import pygame
import threading
import signal
import sys

# Constants
HOST = "localhost"
PORT = 9999
MATRIX_SIZE = 8
PIXEL_SIZE = 40  # Each LED is a 40x40 square in pygame

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((MATRIX_SIZE * PIXEL_SIZE, MATRIX_SIZE * PIXEL_SIZE))
pygame.display.set_caption("Sense HAT LED Matrix (Mock)")
clock = pygame.time.Clock()

# Socket server
server_socket = None

# LED Matrix (8x8) initialized to black (off)
matrix = [[(0, 0, 0) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

def draw_matrix():
    """Redraws the LED matrix in pygame."""
    screen.fill((0, 0, 0))  # Clear screen

    for y in range(MATRIX_SIZE):
        for x in range(MATRIX_SIZE):
            color = matrix[y][x]
            pygame.draw.rect(
                screen,
                color,
                (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE),
                border_radius=10
            )
            pygame.draw.rect(
                screen,
                (50, 50, 50),  # Grid outline (dim gray)
                (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE),
                1
            )

    pygame.display.flip()  # Refresh screen

def handle_client(conn):
    """Handles incoming client commands."""
    global matrix
    try:
        data = conn.recv(1024).decode("utf-8").strip()
        if not data:
            return

        parts = data.split()
        command = parts[0] if parts else ""

        #print(f"Received command: {data}")  # Debugging output

        if command == "set_pixel":
            try:
                _, x, y, r, g, b = data.split()
                x, y, r, g, b = int(x), int(y), int(r), int(g), int(b)
                if 0 <= x < MATRIX_SIZE and 0 <= y < MATRIX_SIZE:
                    matrix[y][x] = (r, g, b)
                    draw_matrix()
                    conn.sendall(b"OK\n")
                else:
                    conn.sendall(b"ERROR: Invalid coordinates\n")
            except ValueError:
                conn.sendall(b"ERROR: Invalid set_pixel format\n")

        elif command == "set_pixels":
            try:
                pixel_values = data[len("set_pixels "):].split()
                if len(pixel_values) != 64:
                    conn.sendall(b"ERROR: set_pixels requires 64 RGB values\n")
                else:
                    for i, pixel in enumerate(pixel_values):
                        r, g, b = map(int, pixel.split(","))
                        x, y = i % MATRIX_SIZE, i // MATRIX_SIZE  # Convert index to grid coordinates
                        matrix[y][x] = (r, g, b)
                    draw_matrix()
                    conn.sendall(b"OK\n")
            except ValueError:
                conn.sendall(b"ERROR: Invalid set_pixels format\n")

        elif command == "clear":
            matrix = [[(0, 0, 0) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
            draw_matrix()
            conn.sendall(b"OK\n")

        else:
            conn.sendall(b"ERROR: Unknown command\n")

    except Exception as e:
        print(f"Error handling client: {e}")

def start_server():
    """Starts the mock Sense HAT server."""
    global server_socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        server_socket = server  # Save the server socket reference

        print(f"Mock Sense HAT server running on {HOST}:{PORT}")

        while True:
            conn, _ = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn,))
            client_thread.daemon = True
            client_thread.start()

# Graceful shutdown on Ctrl+C
def shutdown_server(signal, frame):
    print("\nShutting down the server gracefully...")
    if server_socket:
        server_socket.close()
    pygame.quit()
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl-C)
signal.signal(signal.SIGINT, shutdown_server)

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True
server_thread.start()

# Main loop to keep the pygame window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)  # Limit FPS

pygame.quit()
