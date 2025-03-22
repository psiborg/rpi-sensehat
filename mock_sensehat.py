#!/usr/bin/env python3

import socket

class SenseHat:
    def __init__(self, host="localhost", port=9999):
        self.host = host
        self.port = port

    def send_command(self, command):
        """Send a command to the mock server."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(command.encode("utf-8"))
                return s.recv(1024).decode("utf-8").strip()
        except ConnectionRefusedError:
            print("Error: Could not connect to Sense HAT Mock Server. Make sure it's running.")

    def set_pixel(self, x, y, color):
        """Set a single LED pixel."""
        r, g, b = color
        return self.send_command(f"set_pixel {x} {y} {r} {g} {b}")

    def set_pixels(self, pixel_list):
        """Set all 64 pixels at once."""
        if len(pixel_list) != 64:
            raise ValueError("Pixel list must contain exactly 64 (R, G, B) tuples.")

        pixel_data = " ".join(f"{r},{g},{b}" for (r, g, b) in pixel_list)
        return self.send_command(f"set_pixels {pixel_data}")

    def clear(self):
        """Clear the LED matrix."""
        return self.send_command("clear")
