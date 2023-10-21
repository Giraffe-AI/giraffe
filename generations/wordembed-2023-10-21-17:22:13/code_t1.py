from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [2,0,0], [0,3,0], fill_opacity=0.5).shift(DOWN*2)

        # Create the squares on each side
        square_a = Square(side_length=2).next_to(triangle, DOWN, buff=0)
        square_b = Square(side_length=3).next_to(triangle, LEFT, buff=0)
        square_c = Square(side_length=3.6055).next_to(triangle.get_vertex(2), buff=0)

        # Create the labels for each side
        label_a = Tex("a").next_to(square_a, DOWN)
        label_b = Tex("b").next_to(square_b, LEFT)
        label_c = Tex("c").next_to(square_c, UP)

        # Create the equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2").next_to(triangle, RIGHT, buff=1)

        # Add everything to the scene
        self.play(Create(triangle))
        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(equation))

        # Show the areas of the squares on sides a and b combined
        self.play(square_a.animate.shift(UP*3), square_b.animate.shift(RIGHT*2))

        # Show the area of the square on side c
        self.play(square_c.animate.set_fill(color=BLUE, opacity=0.5))

        # Show the equation again
        self.play(ReplacementTransform(square_a, equation[0]), ReplacementTransform(square_b, equation[2]), ReplacementTransform(square_c, equation[4]))

        self.wait()