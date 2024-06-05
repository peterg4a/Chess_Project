from manim import *

class meh(Scene):
    def construct(self):
        axes = Axes(x_range = [0, 10, 1], y_range = [0, 5, 1], x_length = 10, y_length = 5)
        box = Rectangle(stroke_color = GREEN_C, fill_color = RED_B, height=1, width=1)
        self.add(box)
        self.add(axes)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(LEFT*2), run_time=2)