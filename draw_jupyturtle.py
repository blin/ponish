import re

from jupyturtle import jupyturtle

from draw import Page, Turtle


def get_svg(t: jupyturtle.Turtle) -> str:
    svg = t.get_SVG()
    svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"')
    svg = re.sub(r"'$", "", svg, flags=re.MULTILINE)
    svg = re.sub(r"^$\n", "", svg, flags=re.MULTILINE)
    return svg


class DrawingContext:
    """Context manager for creating and saving drawings."""

    def __init__(
        self,
        output_path: str | None = None,
        unit_size: float = 20,
        drawing_width: int = 180,
        drawing_height: int | None = None,
    ):
        self.output_path = output_path
        self.unit_size = unit_size
        self.drawing_width = drawing_width
        self.drawing_height = drawing_height if drawing_height else unit_size * 5
        self.page = None
        self.turtle = None

    def __enter__(self) -> tuple[Page, Turtle]:
        u = self.unit_size
        drawing = jupyturtle.Drawing(
            width=self.drawing_width, height=self.drawing_height, bgcolor="#FFFFFF"
        )
        self.page = Page(
            vowel_area_height_px=u,
            current_line_bottom_px=(u * 3) + (u // 2),
            current_line_left_px=u,
        )
        self.turtle = jupyturtle.Turtle(delay=0.00, drawing=drawing)
        self.turtle.pen_color = "#000000"
        return self.page, self.turtle

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.turtle.hide()
        if self.output_path:
            self.turtle.drawing.width = (
                self.page.furthest_from_left_px + self.page.vowel_area_height_px
            )
            self.turtle.drawing.height = (
                self.page.furthest_from_top_px + self.page.vowel_area_height_px
            )
            svg = get_svg(self.turtle)
            with open(self.output_path, "w") as f:
                f.write(svg)
