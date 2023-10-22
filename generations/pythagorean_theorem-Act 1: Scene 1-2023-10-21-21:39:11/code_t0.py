from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)

        # Label the sides
        a_label = Tex("a").next_to(triangle, LEFT)
        b_label = Tex("b").next_to(triangle, DOWN)
        c_label = Tex("c").next_to(triangle, RIGHT)

        # Create the narration
        narration = Tex("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(UP)

        # Add everything to the scene
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeIn(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(2)

        # Remove the narration
        self.play(FadeOut(narration))
        self.wait(2)