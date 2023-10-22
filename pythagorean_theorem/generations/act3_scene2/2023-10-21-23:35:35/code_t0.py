from manim import *

class SquareScene(Scene):
    def construct(self):
        # Define the side lengths
        a = 3
        b = 4

        # Create the larger square
        square = Square(side_length=a+b, color=BLUE)
        square_label = Tex("(a + b)^2").next_to(square, UP)

        # Animation
        self.play(Create(square))
        self.play(Write(square_label))
        self.wait()

        # Save the scene
        self.save_state()

# Render the scene
SquareScene().render()