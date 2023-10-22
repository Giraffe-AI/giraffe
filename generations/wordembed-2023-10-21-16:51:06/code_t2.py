from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle and scale it
        triangle = Polygon([0,0,0], [2,0,0], [0,2,0], fill_opacity=0.5)
        triangle.set_color(ORANGE)

        # Create the sides based on the scaled triangle
        side_a = Line([0,0,0], [2,0,0])
        side_b = Line([0,0,0], [0,2,0])
        side_c = Line([2,0,0], [0,2,0])

        # Create the labels for the sides
        label_a = Tex("a").next_to(side_a, DOWN)
        label_b = Tex("b").next_to(side_b, LEFT)
        label_c = Tex("c").next_to(side_c, RIGHT)

        # Create the equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2").next_to(triangle, UP)

        # Add everything to the scene
        self.play(Create(triangle))
        self.play(Create(side_a), Create(side_b), Create(side_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(equation))