from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)
        self.play(Create(triangle))

        # Create squares on each side
        square_a = Square(side_length=1).next_to(triangle, LEFT)
        square_b = Square(side_length=1).next_to(triangle, DOWN)
        square_c = Square(side_length=np.sqrt(2)).rotate(PI/4).next_to(triangle, UP+RIGHT)

        # Animate the squares
        self.play(Create(square_a), Create(square_b), Create(square_c))

        # Create labels for the sides
        labels = ["a", "b", "c"]
        for label, side in zip(labels, [square_a, square_b, square_c]):
            text = Text(label).scale(0.5).next_to(side, UP)
            self.play(Write(text))

        # Create the equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2").next_to(triangle, 4*DOWN)
        self.play(Write(equation))

        # Show that the areas of the squares on sides a and b are combined to form the square on side c
        self.wait(2)
        self.play(Transform(square_a, square_c), Transform(square_b, square_c))
        self.wait(2)