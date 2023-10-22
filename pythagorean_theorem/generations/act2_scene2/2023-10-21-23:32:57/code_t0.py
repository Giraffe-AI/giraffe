from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # Create the larger square
        square1 = Square(side_length=5, color=BLUE)
        square1.shift(LEFT*2)

        # Create the smaller square
        square2 = Square(side_length=3, color=RED)
        square2.shift(RIGHT*2)

        # Create the four triangles
        triangle1 = Polygon([0,0,0], [4,0,0], [4,4,0], color=YELLOW)
        triangle2 = Polygon([0,0,0], [0,4,0], [-4,4,0], color=YELLOW)
        triangle3 = Polygon([0,0,0], [-4,0,0], [-4,-4,0], color=YELLOW)
        triangle4 = Polygon([0,0,0], [0,-4,0], [4,-4,0], color=YELLOW)

        # Position the triangles
        triangle1.shift(UP*2.5 + RIGHT*2.5)
        triangle2.shift(UP*2.5 + LEFT*2.5)
        triangle3.shift(DOWN*2.5 + LEFT*2.5)
        triangle4.shift(DOWN*2.5 + RIGHT*2.5)

        # Add all elements to the scene
        self.add(square1, square2, triangle1, triangle2, triangle3, triangle4)

        # Play the animation
        self.play(FadeIn(square1), FadeIn(square2), FadeIn(triangle1), FadeIn(triangle2), FadeIn(triangle3), FadeIn(triangle4))
        self.wait()