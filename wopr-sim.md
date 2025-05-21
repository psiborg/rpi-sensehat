## wopr-sim.py — WOPR 80s Terminal Simulation

**wopr-sim.py** is a Python script that simulates an interactive 1980s-style terminal inspired by the WOPR computer ("WarGames" movie), complete with animated ASCII art, simulated typing sounds, and optional LED matrix effects for the Raspberry Pi Sense HAT. It can respond to user commands using either a YAML file or AI-generated answers (with Ollama).

### Features

- **80s-Style Terminal Experience:** ASCII art banners, simulated typing, and loading bars evoke classic movie computer terminals.
- **Interactive Command Processing:** Users log in and enter commands; responses come from a YAML config or (optionally) AI via Ollama.
- **LED Matrix Visuals:** If a Sense HAT is attached, animated LED effects (WOPR-style, sine wave, KITT scanner) run in the background.
- **Typing Sound Effects:** Simulated keystroke audio accompanies on-screen text (requires a "typing_sound.mp3" sound file).
- **Customizable Responses:** YAML file (`wopr-sim_responses.yaml`) defines valid commands and responses; AI fallback available if enabled.
- **"Backdoor" Login Screens:** Simulated access screens flash on successful authentication.

### Requirements

- Python 3
- `PyYAML` for YAML parsing
- `pygame` (and system dependencies, e.g., `python3-pygame`) for sound
- Optional:
  - `sense_hat` for Raspberry Pi Sense HAT LED effects (or a compatible mock)
  - `ollama` for AI-generated replies

### Usage

Install dependencies:
```bash
sudo apt install python3-pygame
pip install pyyaml ollama  # (ollama is optional)
```

Run the script:
```bash
python3 wopr-sim.py [--led wopr_activity|sine_wave|kitt_scanner]
```

- The `--led` option controls the LED animation (default: wopr_activity).
- Make sure `wopr-sim_responses.yaml` and a typing sound file (`typing_sound.mp3`) are present in the same directory.

### How It Works

1. **Startup:** Displays a random ASCII art banner and simulates system boot/loading.
2. **Login:** Prompts for a username (set in the YAML file); only the correct user is granted access.
3. **Command Loop:** Accepts user commands. If a command matches an entry in the YAML file, the predefined response is shown; otherwise, if Ollama is available, it uses AI to generate a reply.
4. **LED & Sound:** Runs the chosen LED animation in a separate thread and plays typing sounds during output.
5. **Exit:** Type `quit`, `exit`, or similar to terminate the simulation.

### File Structure

- `wopr-sim.py` — Main simulation script
- `wopr-sim_responses.yaml` — YAML file with authentication info and command/response pairs
- `typing_sound.mp3` — Keystroke sound effect
- (Optional) `mock_sensehat.py` — For testing without actual Sense HAT hardware

### Customization

- Add or edit responses in `wopr-sim_responses.yaml`.
- Replace or edit ASCII art banners in the script for a different look.
- Swap out or add new LED animation modes.

