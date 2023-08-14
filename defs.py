
from typing import Final

COLOR_WHITE: Final[str] = 'white'
COLOR_BLACK: Final[str] = 'black'
COLOR_BLUE: Final[str] = 'blue'
COLOR_GREEN: Final[str] = 'green'
COLOR_YELLOW: Final[str] = 'orange'
COLOR_RED: Final[str] = 'red'

TIME_TYPES = ["Speech", "Evaluation", "Table Topics"]

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