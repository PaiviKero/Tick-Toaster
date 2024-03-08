
from typing import Final

COLOR_WHITE: Final[str] = 'white'
COLOR_BASE: Final[str] = 'mint cream'
COLOR_BASE_SECONDARY: Final[str] = 'azure'
COLOR_BLACK: Final[str] = 'black'
COLOR_BLUE: Final[str] = 'steelblue'
COLOR_GREEN: Final[str] = 'DarkSeaGreen'
COLOR_YELLOW: Final[str] = 'lemon chiffon'
COLOR_RED: Final[str] = 'salmon'

RECORDER_WINDOW_WIDTH: Final[int] = 400
RECORDER_WINDOW_HEIGHT: Final[int] = 750
RECORDER_WINDOW_START_X: Final[int] = 50
RECORDER_WINDOW_START_Y: Final[int] = 50
MAIN_WINDOW_WIDTH: Final[int] = 900
MAIN_WINDOW_HEIGHT: Final[int] = 500
MAIN_WINDOW_START_X: Final[int] = RECORDER_WINDOW_START_X
MAIN_WINDOW_START_Y: Final[int] = RECORDER_WINDOW_HEIGHT+2*RECORDER_WINDOW_START_Y

BACKGROUND_IMAGE_SCALING_PERCENTAGE = 0.5

TIME_TYPES = ["Speech", "Evaluation", "Table Topics"]
SPEAKER_FILE: Final[str] = '\\Tick-Toaster\\Speakers.txt'

SPEECH_OPTIONS = {
    "Ice-Breaker": {
        "type": TIME_TYPES[0],
        "color_times": [4, 5, 6]
    },
    "Speech 5-7min": {
        "type": TIME_TYPES[0],
        "color_times":  [5, 6, 7]
    },
    "Speech 10-12min": {
        "type": TIME_TYPES[0],
        "color_times":  [10, 11, 12]
    }, 
    "Evaluation": {
        "type": TIME_TYPES[1],
        "color_times":  [2, 2.5, 3]
    }, 
    "Table Topics": {
        "type": TIME_TYPES[2],
        "color_times":  [1, 1.5, 2]
    },
    "Test": {
        "type": TIME_TYPES[0],
        "color_times":  [0.05, 0.10, 0.15]
    }
}