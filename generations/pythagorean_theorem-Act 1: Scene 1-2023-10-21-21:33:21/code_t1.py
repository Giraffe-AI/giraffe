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

        # Render the scene
        self.wait()