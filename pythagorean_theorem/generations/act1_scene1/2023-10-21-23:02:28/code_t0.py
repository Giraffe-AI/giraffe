from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)

        # Label sides a, b, and c
        a_label = Tex("a").next_to(triangle, LEFT)
        b_label = Tex("b").next_to(triangle, DOWN)
        c_label = Tex("c").next_to(triangle, RIGHT)

        # Add elements to the scene
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))

        # Add narration
        self.wait(1)
        narration = Tex("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry.")
        self.play(Write(narration))
        self.wait(2)

        # Remove elements
        self.play(FadeOut(narration))
        self.wait(1)

        # Ensure no overlap
        self.play(triangle.animate.shift(LEFT*2), a_label.animate.shift(LEFT*2), b_label.animate.shift(LEFT*2), c_label.animate.shift(LEFT*2))
        self.wait(1)

        # Ensure elements fit on screen
        self.play(triangle.animate.scale(0.5), a_label.animate.scale(0.5), b_label.animate.scale(0.5), c_label.animate.scale(0.5))
        self.wait(1)

        # End scene
        self.play(FadeOut(triangle), FadeOut(a_label), FadeOut(b_label), FadeOut(c_label))