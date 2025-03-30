import math
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from glyphs import (
    Circle,
    Glyph,
    GlyphAction,
    GlyphSize,
    PenAction,
    Point,
    PolarLine,
    RelCubicBezier,
    RelPoint,
    Rotation,
    VowelPosition,
    all as all_glyphs,
    punctuation,
)


@runtime_checkable
class Turtle(Protocol):
    @property
    def x(self) -> float: ...

    @property
    def y(self) -> float: ...

    @property
    def heading(self) -> float: ...

    @heading.setter
    def heading(self, value: float) -> None: ...

    @property
    def pen_color(self) -> str: ...

    @pen_color.setter
    def pen_color(self, value: str) -> None: ...

    def forward(self, distance: float) -> None: ...

    def jump_to(self, x: float, y: float) -> None: ...

    def move_to(self, x: float, y: float) -> None: ...

    def pen_up(self) -> None: ...

    def pen_down(self) -> None: ...


@dataclass
class Page:
    vowel_area_height_px: float
    current_glyph_height_px: float = 0
    current_line_bottom_px: float = 0
    current_line_left_px: float = 0
    furthest_from_left_px: float = 0
    furthest_from_top_px: float = 0


def calc_bezier(p1: Point, p2: Point, p3: Point, p4: Point, t: float) -> tuple[float, float]:
    """
    Calculate a point on a cubic Bezier curve for a given parameter t.

    Args:
        p1: First control point
        p2: Second control point
        p3: Third control point
        p4: Fourth control point
        t: Parameter value between 0 and 1

    Returns:
        A tuple (x, y) representing a point on the Bezier curve
    """
    u = 1 - t  # u is the complement of t

    # First level of linear interpolation between adjacent points
    x_p1_p2 = u * p1.x + t * p2.x
    x_p2_p3 = u * p2.x + t * p3.x
    x_p3_p4 = u * p3.x + t * p4.x
    y_p1_p2 = u * p1.y + t * p2.y
    y_p2_p3 = u * p2.y + t * p3.y
    y_p3_p4 = u * p3.y + t * p4.y

    # Second level of linear interpolation
    x_p1p2_p2p3 = u * x_p1_p2 + t * x_p2_p3
    x_p2p3_p3p4 = u * x_p2_p3 + t * x_p3_p4
    y_p1p2_p2p3 = u * y_p1_p2 + t * y_p2_p3
    y_p2p3_p3p4 = u * y_p2_p3 + t * y_p3_p4

    # Final interpolation
    x = u * x_p1p2_p2p3 + t * x_p2p3_p3p4
    y = u * y_p1p2_p2p3 + t * y_p2p3_p3p4

    return (x, y)


def find_rel_point(rel: RelPoint, ref_point: Point, unit_size_px: float) -> Point:
    return Point(
        y=ref_point.y + unit_size_px * rel.rel_y,
        x=ref_point.x + unit_size_px * rel.rel_x,
    )


# NOTE: have to use `turt` instead of `t` because of the name conflict
# with Bezier "t-parameter"
def draw_cubic_bezier(turt: Turtle, page: Page, curve: RelCubicBezier) -> None:
    p1 = Point(y=turt.y, x=turt.x)
    prev_x, prev_y = turt.x, turt.y

    for i in range(21):
        t = i / 20
        p2 = find_rel_point(curve.p2, p1, page.current_glyph_height_px)
        p3 = find_rel_point(curve.p3, p1, page.current_glyph_height_px)
        p4 = find_rel_point(curve.p4, p1, page.current_glyph_height_px)
        x, y = calc_bezier(p1, p2, p3, p4, t)

        if i == 0:
            turt.jump_to(x, y)
            prev_x, prev_y = x, y
            continue

        dx = x - prev_x
        dy = y - prev_y
        distance = math.sqrt(dx**2 + dy**2)

        angle = math.degrees(math.atan2(dy, dx))
        turt.heading = angle

        # Using draw_forward instead of t.move_to
        # to update furthest_from_left_px and furthest_from_top_px
        draw_forward(turt, page, distance)

        prev_x, prev_y = x, y


def draw_forward(t: Turtle, p: Page, distance_px: float) -> None:
    p.furthest_from_left_px = max(p.furthest_from_left_px, t.x)
    p.furthest_from_top_px = max(p.furthest_from_top_px, t.y)
    t.forward(distance_px)
    p.furthest_from_left_px = max(p.furthest_from_left_px, t.x)
    p.furthest_from_top_px = max(p.furthest_from_top_px, t.y)


def draw_circle(t: Turtle, circle: Circle, page: Page) -> None:
    # Set initial heading
    t.heading = -circle.heading_deg  # Negative because turtle heading is clockwise

    # Calculate the number of steps based on the extent
    steps = max(int(abs(circle.extent_deg) / 5), 1)  # At least 1 step, otherwise 5 degrees per step
    angle_per_step = circle.extent_deg / steps

    # Calculate the side length for a regular polygon approximating the circle
    # When drawing a circle as a regular polygon, each segment is a chord of the circle
    # For a chord of a circle:
    # - The angle at the center is angle_per_step
    # - The chord length (side_length) = 2 * radius * sin(angle/2)
    # This formula gives the exact length needed to draw each side of the polygon
    step_angle_rad = math.radians(angle_per_step)
    radius_px = circle.rel_radius * page.current_glyph_height_px
    side_length = 2 * radius_px * math.sin(step_angle_rad / 2)

    for _ in range(steps):
        draw_forward(t, page, side_length)
        match circle.rotation:
            case Rotation.CCW:
                t.heading -= angle_per_step
            case Rotation.CW:
                t.heading += angle_per_step


def draw_polar_line(t: Turtle, p: Page, line: PolarLine) -> None:
    t.heading = -line.angle_deg
    draw_forward(t, p, p.current_glyph_height_px * line.rel_magnitude)


def draw_action(t: Turtle, page: Page, action: GlyphAction) -> None:
    match action:
        case PolarLine() as l:
            draw_polar_line(t, page, l)
        case RelCubicBezier() as crv:
            draw_cubic_bezier(t, page, crv)
        case Circle() as c:
            draw_circle(t, c, page)
        case PenAction.LIFT:
            t.pen_up()
        case PenAction.PLACE:
            t.pen_down()


def find_box_corner(page: Page, vowel_pos: VowelPosition) -> Point:
    lb = page.current_line_bottom_px
    ll = page.current_line_left_px
    us = page.vowel_area_height_px
    box_top_px = 0.0
    match vowel_pos:
        case VowelPosition.AE:
            box_top_px = lb - (us * 2.5)
        case VowelPosition.IY:
            box_top_px = lb - us * 2
        case VowelPosition.OU:
            box_top_px = lb - us * 1
    return Point(y=box_top_px, x=ll)


def draw_glyph(
    t: Turtle, page: Page, glyph: Glyph, pos: VowelPosition, gs: GlyphSize = GlyphSize.SINGLE
) -> None:
    page.current_glyph_height_px = page.vowel_area_height_px * gs.value
    match pos:
        case VowelPosition.AE | VowelPosition.IY | VowelPosition.OU as v:
            t.pen_up()

            box = find_box_corner(page, vowel_pos=v)
            y = box.y + page.current_glyph_height_px * glyph.start_pos.rel_y
            x = box.x + page.current_glyph_height_px * glyph.start_pos.rel_x
            t.jump_to(y=y, x=x)

            t.pen_down()
    for action in glyph.draw_actions:
        draw_action(t, page, action)


class EventRecorder:
    def __init__(self) -> None:
        self.events: list[dict[str, str]] = []

    def record_event(self, event: dict[str, str]) -> None:
        self.events.append(event)


def _draw_glyph(
    t: Turtle,
    page: Page,
    glyph: Glyph,
    pos: VowelPosition,
    gs: GlyphSize = GlyphSize.SINGLE,
    gid: str = "",
    event_recorder: EventRecorder | None = None,
) -> None:
    if event_recorder:
        event_recorder.record_event(
            {
                "name": "draw_glyph",
                "gid": gid,
                "vowel_pos": pos.name,
                "glyph_size": gs.name,
            }
        )
    draw_glyph(t, page, glyph, pos=pos, gs=gs)


def outline_vowel_areas(t: Turtle, p: Page) -> None:
    c1 = t.pen_color
    t.pen_color = "#DDDDDD"
    for i in range(4):
        y = p.current_line_bottom_px - (i * p.vowel_area_height_px)
        print(f"{y=}")
        t.jump_to(y=y, x=0)
        t.heading = 0
        t.forward(1000)
    t.pen_color = c1


def advance_after_glyph(t: Turtle, page: Page) -> None:
    t.pen_up()
    page.current_line_left_px = page.furthest_from_left_px + page.vowel_area_height_px / 3
    t.jump_to(y=page.current_line_bottom_px, x=page.current_line_left_px)
    t.pen_down()


def _advance_after_glyph(
    t: Turtle,
    page: Page,
    event_recorder: EventRecorder | None = None,
) -> None:
    if event_recorder:
        event_recorder.record_event({"name": "advance_after_glyph"})
    advance_after_glyph(t, page)


def advance_after_word(t: Turtle, page: Page) -> None:
    t.pen_up()
    page.current_line_left_px = page.furthest_from_left_px + (page.vowel_area_height_px * 1.5)
    t.jump_to(y=page.current_line_bottom_px, x=page.current_line_left_px)
    t.pen_down()


def gid_at(word: str, idx: int) -> tuple[str, int]:
    subword = word[idx:]
    assert len(subword) > 0, f"id_at({word=}, {idx=}), empty subword"
    if len(subword) > 3 and subword[0] == "$" and subword[1] == "(":
        rb = subword.find(")")
        if rb == -1:
            raise ValueError(f"unterminated $() sequence in {word=}")
        gid = subword[2:rb]
        return gid, len(gid) + 3
    return subword[0], 1


# TODO: use is_vowel attribute of Glyph or remove the is_vowel attribute
def is_gid_vowel(gid: str) -> bool:
    gid_up = gid.upper()
    return gid_up in ["A", "E", "I", "O", "U", "Y"]


def split_into_chunks(word: str) -> list[str]:
    """Split a word into chunks, breaking at non-consecutive vowels.

    Examples:
        split_into_chunks("fire") -> ["f", "ir", "e"]
        split_into_chunks("mount") -> ["m", "ount"]
        split_into_chunks("s$(TR)ength") -> ["s$(TR)", "ength"]

    Returns:
        A list of word chunks
    """
    if not word:
        return []

    chunks = []
    current_chunk = ""
    word_pos = 0
    last_was_vowel = False
    all_vowels = True  # Track if the word consists of only vowels

    # First pass to check if it's all vowels
    check_pos = 0
    while check_pos < len(word):
        gid, advance = gid_at(word, check_pos)
        if not is_gid_vowel(gid):
            all_vowels = False
            break
        check_pos += advance

    # If it's all vowels, split each vowel into its own chunk
    if all_vowels and word:
        check_pos = 0
        while check_pos < len(word):
            gid, advance = gid_at(word, check_pos)
            chunks.append(word[check_pos : check_pos + advance])
            check_pos += advance
        return chunks

    # Normal processing for mixed vowels and consonants
    while word_pos < len(word):
        gid, advance = gid_at(word, word_pos)
        g_is_vowel = is_gid_vowel(gid)

        # Start a new chunk when we hit a vowel after a non-vowel
        if g_is_vowel and not last_was_vowel and current_chunk:
            chunks.append(current_chunk)
            current_chunk = ""

        current_chunk += word[word_pos : word_pos + advance]
        word_pos += advance
        last_was_vowel = g_is_vowel

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def extract_vowel_params(gid: str) -> VowelPosition:
    """Determine the VowelPosition based on the vowel glyph ID."""
    gid_up = gid.upper()
    match gid_up:
        case "A" | "E":
            return VowelPosition.AE
        case "I" | "Y":
            return VowelPosition.IY
        case "O" | "U":
            return VowelPosition.OU
        case _:
            raise ValueError(f"Got {gid=}, expected vowel")


def draw_chunk(
    t: Turtle,
    p: Page,
    chunk: str,
    is_first_chunk: bool,
    is_last_chunk: bool,
    event_recorder: EventRecorder | None = None,
):
    """Draws the glyphs in a word chunk, updating and returning the drawing state."""
    # Pre-calculate glyphs for the chunk
    chunk_gs: list[tuple[str, Glyph]] = []
    parse_pos = 0
    while parse_pos < len(chunk):
        gid, advance = gid_at(chunk, parse_pos)
        g = all_glyphs.get(gid, None) or all_glyphs.get(gid.upper(), None)
        assert g, f"Glyph {gid} not found in glyph list for chunk '{chunk}'"
        chunk_gs.append((gid, g))
        parse_pos += advance

    # The first chunk starts with a vowel or a consonant
    # The middle and last chunks start with a vowel
    gpos = VowelPosition.IY
    consecutive_vowels = 0

    for i, (gid, g) in enumerate(chunk_gs):
        g_is_first_in_chunk = i == 0
        g_is_first_in_word = g_is_first_in_chunk and is_first_chunk

        g_is_last_in_chunk = i == len(chunk_gs) - 1
        g_is_last_in_word = g_is_last_in_chunk and is_last_chunk

        g_is_vowel = is_gid_vowel(gid)
        consecutive_vowels = consecutive_vowels + 1 if g_is_vowel else 0

        next_gid_is_consonant = False
        if i + 1 < len(chunk_gs):
            next_gid, _ = chunk_gs[i + 1]
            if not is_gid_vowel(next_gid):
                next_gid_is_consonant = True

        g_to_draw = g
        gid_to_draw = gid
        # Cases to consider "I", "brow", "hi", "today", "yu"
        if g_is_vowel and not g_is_first_in_word and g_is_last_in_word and g_is_first_in_chunk:
            g_to_draw = all_glyphs["high-dot"]
            gid_to_draw = "high-dot"

        should_draw = False
        should_advance = False

        if g_is_vowel:
            vpos = extract_vowel_params(gid)

            if is_first_chunk and g_is_first_in_chunk:
                should_draw = True
            elif g_is_last_in_word and g_is_first_in_chunk:
                should_advance = True
                gpos = vpos
                should_draw = True
            elif consecutive_vowels == 2:
                should_draw = True
                consecutive_vowels = 0
            else:
                # First vowel encountered (or first after a consonant)
                # Update state for the *next* glyph and advance position
                gpos = vpos
                should_advance = True
                # Skip drawing this vowel directly, its position determines the next consonant/vowel
        else:
            # If not a vowel or special case, draw the consonant/glyph
            should_draw = True

        if gpos == VowelPosition.IY and not next_gid_is_consonant:
            gs = GlyphSize.DOUBLE
        else:
            gs = GlyphSize.SINGLE

        if should_advance:
            _advance_after_glyph(t, p, event_recorder=event_recorder)

        if should_draw:
            _draw_glyph(
                t, p, g_to_draw, pos=gpos, gs=gs, gid=gid_to_draw, event_recorder=event_recorder
            )
            # Reset state after drawing a consonant/non-vowel
            gpos = VowelPosition.CONT
            gs = GlyphSize.SINGLE


def draw_word(t: Turtle, p: Page, word: str, event_recorder: EventRecorder | None = None):
    chunks = split_into_chunks(word)

    for i, chunk in enumerate(chunks):
        is_first_chunk = i == 0
        is_last_chunk = i == len(chunks) - 1

        draw_chunk(t, p, chunk, is_first_chunk, is_last_chunk, event_recorder)

    # Advance after the entire word is drawn


def draw_article(
    t: Turtle,
    p: Page,
    # TODO: figure out literal
    article: str,
):
    pass
    article_pos = VowelPosition.OU if article == "the" else VowelPosition.AE
    draw_glyph(t, p, all_glyphs["low-dot"], pos=article_pos)
    advance_after_glyph(t, p)


def draw_punctuation(
    t: Turtle,
    p: Page,
    punct: str,
):
    gpos = VowelPosition.OU
    gs = GlyphSize.DOUBLE
    match punct:
        case "," | ".":
            gs = GlyphSize.SINGLE
        case ":" | "!":
            gpos = VowelPosition.IY
    draw_glyph(t, p, punctuation[punct], pos=gpos, gs=gs)
    advance_after_word(t, p)


def draw_sentence(
    t: Turtle,
    p: Page,
    sentence: str,
):
    # NOTE: sentence is a single drawing line, rather than an actual sentence
    words = sentence.split(" ")
    sentence_pos = 0
    while sentence_pos < len(words):
        word = words[sentence_pos]
        sentence_pos += 1
        word_is_last = sentence_pos >= len(words)

        if word in punctuation:
            draw_punctuation(t, p, word)
            continue

        if word.lower() in ["a", "an", "the"] and not word_is_last:
            draw_article(t, p, word)
            continue

        draw_word(t, p, word)
        advance_after_word(t, p)
