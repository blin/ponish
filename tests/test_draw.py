import math

import pytest
from syrupy.assertion import SnapshotAssertion

import lesson_2_passage_conan
import lesson_3_examples_1
import lesson_3_examples_3
import lesson_3_examples_4
from draw import (
    EventRecorder,
    Page,
    Turtle,
    draw_word,
)


def words_from_text(text: list[str]) -> set[str]:
    return {word for line in text for word in line.split()}


def words_from_words(words: list[tuple[str, str]]) -> set[str]:
    return {spelling for _, spelling in words}


WORDBANK: set[str] = set()
WORDBANK.update(words_from_text(lesson_2_passage_conan.text))
WORDBANK.update(words_from_words(lesson_3_examples_1.words))
WORDBANK.update(words_from_words(lesson_3_examples_3.words))
WORDBANK.update(words_from_text(lesson_3_examples_4.text_combined))


# Mock Turtle implementation adhering to the Turtle Protocol
class MockTurtle(Turtle):
    def __init__(self):
        self._x = 0.0
        self._y = 0.0
        self._heading = 0.0
        self._pen_color = "#000000"
        self.is_pen_down = True
        # Log high-level actions relevant for testing draw_word logic
        self.log: list[tuple] = []

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def heading(self) -> float:
        return self._heading

    @heading.setter
    def heading(self, value: float) -> None:
        self._heading = value
        # self.log.append(("set_heading", round(value, 2))) # Less relevant for draw_word logic

    @property
    def pen_color(self) -> str:
        return self._pen_color

    @pen_color.setter
    def pen_color(self, value: str) -> None:
        self._pen_color = value
        # self.log.append(("set_pen_color", value)) # Less relevant

    def forward(self, distance: float) -> None:
        # Simplified movement, primarily for state tracking if needed,
        # but draw_word logic focuses on higher-level events.
        rad = -math.radians(self._heading)  # Turtle heading is clockwise, math is CCW
        dx = distance * math.cos(rad)
        dy = distance * math.sin(rad)
        new_x = self._x + dx
        new_y = self._y + dy
        # self.log.append(("forward", round(distance, 2), f"to ({round(new_x, 2)}, {round(new_y, 2)})"))
        self._x = new_x
        self._y = new_y

    def jump_to(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
        self.log.append(("jump_to", round(x, 2), round(y, 2)))

    def move_to(self, x: float, y: float) -> None:
        # Treat move_to like jump_to for logging purposes in this mock
        self._x = x
        self._y = y
        self.log.append(("move_to", round(x, 2), round(y, 2)))

    def pen_up(self) -> None:
        if self.is_pen_down:
            self.is_pen_down = False
            self.log.append(("pen_up",))

    def pen_down(self) -> None:
        if not self.is_pen_down:
            self.is_pen_down = True
            self.log.append(("pen_down",))


@pytest.mark.parametrize(
    "word",
    WORDBANK,
)
def test_draw_word_events(snapshot: SnapshotAssertion, word: str):
    """Test the sequence of high-level events generated by draw_word."""
    mock_turtle = MockTurtle()
    # Consistent starting page state for predictable results
    page = Page(
        vowel_area_height_px=20,
        current_line_bottom_px=100,
        current_line_left_px=50,
        furthest_from_left_px=50,  # Initialize based on current_line_left_px
        furthest_from_top_px=100,  # Initialize based on current_line_bottom_px
    )
    event_recorder = EventRecorder()

    # Execute the function under test
    draw_word(mock_turtle, page, word, event_recorder)

    # Snapshot the recorded high-level events (draw_glyph, advance_after_glyph)
    assert event_recorder.events == snapshot
