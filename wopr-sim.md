# wopr-sim.py

This is a Python script that simulates an interactive 1980s-style "WOPR" terminal, inspired by the movie WarGames. Here’s a summary of what it does:

**Key Features:**

- **Terminal Simulation:**  
  Presents ASCII art and simulates boot-up and login prompts, creating a retro terminal experience in the command line.

- **Raspberry Pi Sense HAT Integration (Optional):**  
  If a Sense HAT is attached and the sense_hat Python library is installed, the script activates animated LED effects on the Pi’s LED matrix (such as “WOPR activity,” sine waves, and a KITT scanner effect).

- **Interactive Command Processing:**  
  After logging in with a specified username (defined in a YAML file), the user can enter commands. The script responds based on a YAML-defined set of commands and responses (wopr-sim_responses.yaml).

- **AI-Generated Responses (Optional):**  
  If the ollama library and an AI model are available, unrecognized commands will generate AI-based responses.

- **YAML Configuration:**  
  Responses, authentication details, and special backdoor screens are read from a YAML file (wopr-sim_responses.yaml).

- **Visual Effects:**  
  Includes simulated typing, loading bars, and animated ASCII “backdoor” screens for extra realism.

- **Threaded LED Animations:**  
  LED animations run in a separate thread and adjust speed based on user activity.

**Intended Use:**
- This script is designed for entertainment, demonstration, or retro-themed projects, especially on a Raspberry Pi with a Sense HAT. It provides a fun, interactive terminal with visual effects and customizable command/response behavior.
