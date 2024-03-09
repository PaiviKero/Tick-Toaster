
from typing import Final

COLOR_WHITE: Final[str] = 'white'
COLOR_BASE: Final[str] = 'mint cream'
COLOR_BASE_SECONDARY: Final[str] = 'azure'
COLOR_BLACK: Final[str] = 'black'
COLOR_BLUE: Final[str] = 'steelblue'
COLOR_GREEN: Final[str] = 'DarkSeaGreen'
COLOR_YELLOW: Final[str] = 'lemon chiffon'
COLOR_RED: Final[str] = 'salmon'

RECORDER_WINDOW_WIDTH: Final[int] = 430
RECORDER_WINDOW_HEIGHT: Final[int] = 750
RECORDER_WINDOW_START_X: Final[int] = 50
RECORDER_WINDOW_START_Y: Final[int] = 50
MAIN_WINDOW_WIDTH: Final[int] = 900
MAIN_WINDOW_HEIGHT: Final[int] = 500
MAIN_WINDOW_START_X: Final[int] = RECORDER_WINDOW_START_X
MAIN_WINDOW_START_Y: Final[int] = RECORDER_WINDOW_HEIGHT+2*RECORDER_WINDOW_START_Y

TYPE_SPEECH = "Speech"
TYPE_EVALUATION = "Evaluation"
TYPE_TABLE_TOPICS = "Table Topics"
TYPE_TABLE_TOPICS_EVALUATION = "Table Topics Evaluation"
TYPE_NON_TIMED_BREAK = "Break"

TIME_TYPES = [TYPE_SPEECH, TYPE_EVALUATION, TYPE_TABLE_TOPICS, TYPE_TABLE_TOPICS_EVALUATION, TYPE_NON_TIMED_BREAK]
LOGGED_TIME_TYPES = [TYPE_SPEECH, TYPE_EVALUATION, TYPE_TABLE_TOPICS, TYPE_TABLE_TOPICS_EVALUATION]
SPEAKER_FILE: Final[str] = '\\Tick-Toaster\\Speakers.txt'

SPEECH_OPTIONS = {
    "Ice-Breaker": {
        "type": TYPE_SPEECH,
        "color_times": [4, 5, 6]
    },
    "Speech 5-7min": {
        "type": TYPE_SPEECH,
        "color_times":  [5, 6, 7]
    },
    "Speech 10-12min": {
        "type": TYPE_SPEECH,
        "color_times":  [10, 11, 12]
    }, 
    "Evaluation": {
        "type": TYPE_EVALUATION,
        "color_times":  [2, 2.5, 3]
    }, 
    "Table Topics": {
        "type": TYPE_TABLE_TOPICS,
        "color_times":  [1, 1.5, 2]
    },
    "Table Topics Evaluation": {
        "type": TYPE_TABLE_TOPICS_EVALUATION,
        "color_times":  [3, 3.5, 4]
    }, 
    "1 Minute Break": {
        "type": TYPE_NON_TIMED_BREAK,
        "color_times":  [0.5, 0.75, 1]
    },
    "Test Speech": {
        "type": TYPE_SPEECH,
        "color_times":  [0.05, 0.10, 0.15]
    },
    "Test Evaluation": {
        "type": TYPE_EVALUATION,
        "color_times":  [0.02, 0.04, 0.08]
    }
}