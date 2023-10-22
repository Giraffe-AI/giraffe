from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()

        # Label the sides of the triangle
        a_label = Tex("a").next_to(triangle, LEFT)
        b_label = Tex("b").next_to(triangle, DOWN)
        c_label = Tex("c").next_to(triangle, RIGHT)

        # Add the triangle and labels to the scene
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))

        # Add narration
        self.add_narration("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")

        # Render the scene
        self.wait()