from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Define the triangle
        triangle = Polygon(
            np.array([0,0,0]),
            np.array([3,0,0]),
            np.array([0,2,0]),
            color=YELLOW
        )

        # Define the sides
        side_a = Line(np.array([0,0,0]), np.array([3,0,0]), color=RED)
        side_b = Line(np.array([0,0,0]), np.array([0,2,0]), color=BLUE)
        side_c = Line(np.array([0,2,0]), np.array([3,0,0]), color=GREEN)

        # Define the squares
        square_a = Square(side_length=3, color=RED).next_to(side_a, DOWN, buff=0)
        square_b = Square(side_length=2, color=BLUE).next_to(side_b, LEFT, buff=0)
        square_c = Square(side_length=np.sqrt(13), color=GREEN).next_to(side_c, buff=0)

        # Define the theorem text
        theorem_text = Text("a^2 + b^2 = c^2", color=WHITE).to_edge(UP)

        # Add everything to the scene
        self.play(Write(triangle))
        self.play(Write(side_a), Write(side_b), Write(side_c))
        self.play(Write(square_a), Write(square_b), Write(square_c))
        self.play(Write(theorem_text))

        # Wait for a while before ending the scene
        self.wait(3)