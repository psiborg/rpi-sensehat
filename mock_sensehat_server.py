#!/usr/bin/env python3

import socket
import pygame
import threading
import signal
import sys
import argparse
from concurrent.futures import ThreadPoolExecutor

# Command line arguments parser
parser = argparse.ArgumentParser(description="Mock Sense HAT Server")
parser.add_argument("--host", type=str, default="localhost", help="Server host")
parser.add_argument("--port", type=int, default=9999, help="Server port")
parser.add_argument("--matrix_size", type=int, default=8, help="LED Matrix size")
parser.add_argument("--pixel_size", type=int, default=40, help="Size of each LED pixel")
parser.add_argument("--debug", action="store_true", help="Enable debugging messages")
args = parser.parse_args()

# Constants
HOST = args.host
PORT = args.port
MATRIX_SIZE = args.matrix_size
PIXEL_SIZE = args.pixel_size
DEBUG = args.debug

class MockSenseHATServer:
    from mock_fonts import fonts

    def __init__(self, host=HOST, port=PORT):
        self.host = host
        self.port = port
        self.server_socket = None
        self.lock = threading.Lock()
        self.running = True

        # Initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((MATRIX_SIZE * PIXEL_SIZE, MATRIX_SIZE * PIXEL_SIZE)) # , pygame.RESIZABLE
        pygame.display.set_caption("Sense HAT LED Matrix (Mock)")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, PIXEL_SIZE * 2)

        # LED Matrix (8x8) initialized to black (off)
        self.matrix = [[(0, 0, 0) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]

        # Thread pool for handling clients
        self.executor = ThreadPoolExecutor(max_workers=10)

        # Draw initial grid
        self.draw_matrix()

    def debug_print(self, message):
        """Prints debugging messages if debug mode is enabled."""
        if DEBUG:
            print(f"[DEBUG] {message}")

    def draw_matrix(self):
        """Redraws the LED matrix in pygame."""
        self.screen.fill((0, 0, 0))  # Clear screen
        for y in range(MATRIX_SIZE):
            for x in range(MATRIX_SIZE):
                color = self.matrix[y][x]
                pygame.draw.rect(self.screen, color, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), border_radius=10)
                pygame.draw.rect(self.screen, (50, 50, 50), (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), 1)  # Grid outline
        pygame.display.flip()
        self.debug_print("Matrix redrawn")

    def show_message(self, message, color=(255, 255, 255), speed=0.2):
        """Displays a scrolling message on the matrix with dynamic letter spacing."""

        def get_char_width(pattern):
            """Calculates the actual width of a character based on non-empty columns."""
            width = 0
            for col in range(MATRIX_SIZE):  # Check each column in 8x8 grid
                if any(pattern[row * MATRIX_SIZE + col] != [0, 0, 0] for row in range(MATRIX_SIZE)):
                    width = col + 1  # Extend width to this column
            print("width", width)
            return width

        # Convert message to a list of (letter pattern, actual width)
        letter_data = [(self.fonts.get(letter, [[0, 0, 0]] * MATRIX_SIZE**2),
                        get_char_width(self.fonts.get(letter, [[0, 0, 0]] * MATRIX_SIZE**2)))
                    for letter in message]

        # Compute total width dynamically
        total_width = sum(width + 1 for _, width in letter_data) - 1  # 1 pixel space between characters

        # Initialize scrolling buffer (empty display)
        scroll_buffer = [[(0, 0, 0) for _ in range(total_width)] for _ in range(MATRIX_SIZE)]

        # Fill scroll buffer using actual widths
        x_offset = 0  # Track position in buffer
        for pattern, width in letter_data:
            for i, pixel in enumerate(pattern):
                x, y = i % MATRIX_SIZE, i // MATRIX_SIZE
                if x < width:  # Only use non-empty part of the character
                    if pixel == [255, 255, 255]:  # If pixel is white, apply color
                        scroll_buffer[y][x_offset + x] = color
                    else:
                        scroll_buffer[y][x_offset + x] = tuple(pixel)
            x_offset += width + 1  # Move to next character with 1 pixel spacing

        # Scroll the text across the matrix
        for offset in range(total_width - MATRIX_SIZE + 1):
            for y in range(MATRIX_SIZE):
                for x in range(MATRIX_SIZE):
                    self.matrix[y][x] = scroll_buffer[y][offset + x]
            self.draw_matrix()
            pygame.time.delay(int(speed * 500))  # Control scrolling speed

    def show_letter(self, letter, color=(255, 255, 255)):
        """Displays a single letter on the matrix using the fonts dictionary."""
        #print(letter, color)
        if letter in self.fonts:
            pattern = self.fonts[letter]
            for i, pixel in enumerate(pattern):
                x, y = i % MATRIX_SIZE, i // MATRIX_SIZE
                #print(pixel, tuple(pixel))
                if pixel == [255, 255, 255]:
                    self.matrix[y][x] = color  # Use the specified color
                else:
                    self.matrix[y][x] = tuple(pixel)  # Use the stored color
            self.draw_matrix()
        else:
            self.debug_print(f"Letter '{letter}' not found in font dictionary")

    def handle_client(self, conn):
        """Handles incoming client commands."""
        try:
            data = conn.recv(1024).decode("utf-8").strip()
            if not data:
                return

            parts = data.split()
            #print("parts", parts)
            command = parts[0] if parts else ""
            response = b"ERROR: Unknown command\n"

            self.debug_print(f"Received command: {data}")

            with self.lock:
                if command == "set_pixel" and len(parts) == 6:
                    try:
                        _, x, y, r, g, b = parts
                        x, y, r, g, b = map(int, [x, y, r, g, b])
                        if 0 <= x < MATRIX_SIZE and 0 <= y < MATRIX_SIZE:
                            self.matrix[y][x] = (r, g, b)
                            self.draw_matrix()
                            response = b"OK\n"
                        else:
                            response = b"ERROR: Invalid coordinates\n"
                    except ValueError:
                        response = b"ERROR: Invalid set_pixel format\n"
                elif command == "set_pixels" and len(parts) == 65:
                    try:
                        pixels = [tuple(map(int, pixel.split(","))) for pixel in parts[1:]]
                        if len(pixels) == 64:
                            for i, (r, g, b) in enumerate(pixels):
                                x, y = i % MATRIX_SIZE, i // MATRIX_SIZE
                                self.matrix[y][x] = (r, g, b)
                            self.draw_matrix()
                            response = b"OK\n"
                    except ValueError:
                        response = b"ERROR: Invalid set_pixels format\n"
                elif command == "clear":
                    self.matrix = [[(0, 0, 0) for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)]
                    self.draw_matrix()
                    response = b"OK\n"
                #elif command == "show_message" and len(parts) > 1:
                elif command == "show_message":
                    message = " ".join(parts[1:-3])  # Joins all parts except the last three
                    r = int(parts[-3])
                    g = int(parts[-2])
                    b = int(parts[-1])
                    #print("show_message", message, r,g ,b)
                    self.show_message(message, color=(r, g, b))
                    response = b"OK\n"
                #elif command == "show_letter" and len(parts) == 2:
                elif command == "show_letter":
                    letter = parts[1]
                    r = int(parts[2])
                    g = int(parts[3])
                    b = int(parts[4])
                    #print(letter, r,g ,b)
                    self.show_letter(letter, color=(r, g, b))
                    response = b"OK\n"

            conn.sendall(response)
            self.debug_print(f"Sent response: {response.decode().strip()}")
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            conn.close()

    def start_server(self):
        """Starts the mock Sense HAT server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((self.host, self.port))
            server.listen(5)
            self.server_socket = server
            print(f"Mock Sense HAT server running on {self.host}:{self.port}")

            while self.running:
                try:
                    conn, addr = server.accept()  # Capture client address
                    self.debug_print(f"Accepted new connection from {addr[0]}:{addr[1]}")
                    self.executor.submit(self.handle_client, conn)
                except OSError:
                    break

    def shutdown(self, signal=None, frame=None):
        print("\nShutting down the server gracefully...")
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        self.executor.shutdown(wait=True)
        pygame.quit()
        sys.exit(0)

if __name__ == "__main__":
    server = MockSenseHATServer()
    signal.signal(signal.SIGINT, server.shutdown)

    server_thread = threading.Thread(target=server.start_server)
    server_thread.daemon = True
    server_thread.start()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        server.clock.tick(60)

    server.shutdown()
