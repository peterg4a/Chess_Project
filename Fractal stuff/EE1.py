from manim import *

class NameOfAnimation(Scene):
    def construct(self):
        box = Rectangle(stroke_color = GREEN_C, fill_color = RED_B, height=1, width=1)
        self.add(box)
        self.play(box.animate.shift(RIGHT*2), run_time=2)
        self.play(box.animate.shift(LEFT*2), run_time=2)