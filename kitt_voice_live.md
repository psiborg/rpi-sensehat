# Kitt's Voice Box (Live)

![KITT](./images/kitt.gif)

## Setup:

1. Plug the USB Microphone into one of the Raspberry Pi’s USB ports.

2. Install necessary audio utilities:

    ```sh
    sudo apt-get update
    sudo apt-get install alsa-utils
    ```

3. Check if the microphone is detected:

    ```sh
    arecord -l
    ```

    This command lists all available recording devices. You should see your USB microphone listed.

4. Test the microphone:

    You can test the microphone by recording a short clip:

    ```sh
    arecord -D plughw:1,0 -d 3 test.wav
    ```

    - Replace 1,0 with the appropriate card and device number if different.
    - This records a 3-second clip and saves it as test.wav.
    - You can play it back with:

    ```sh
    aplay test.wav
    ```

    Once your microphone is set up, you can use it with Python libraries like pyaudio to capture audio and drive your Sense HAT animation.

5. Install required libraries:

    You can install the required libraries using pip:

    ```sh
    pip install pyaudio numpy
    ```
