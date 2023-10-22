from manim import *

class SquareScene(Scene):
    def construct(self):
        # Define the side lengths
        a = 3
        b = 4

        # Create the larger square
        square = Square(side_length=a+b, color=BLUE)
        square_label_text = f"({a} + {b})^2"
        square_label = MathTex(square_label_text).next_to(square, UP)

        # Animation
        self.play(Create(square))
        self.play(Write(square_label))
        self.wait()

# Render the scene
SquareScene().render()