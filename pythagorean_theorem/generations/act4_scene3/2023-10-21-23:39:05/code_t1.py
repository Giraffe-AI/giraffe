from manim import *

class PythagorasScene(Scene):
    def construct(self):
        # Create the characters
        pythagoras = ImageMobject("/path/to/pythagoras.png").scale(0.5)
        pythagoras.to_corner(UL)

        # Create the narration text
        narration_text = Text("It's amazing to think that a theorem discovered over two thousand years ago is still so fundamental to our understanding of the world.")
        narration_text.next_to(pythagoras, DOWN).scale(0.5)

        # Create the visual of the theorem
        triangle = Triangle()
        triangle.next_to(narration_text, DOWN)

        a_square = Square().scale(0.5)
        a_square.next_to(triangle, LEFT)

        b_square = Square().scale(0.5)
        b_square.next_to(triangle, RIGHT)

        c_square = Square().scale(0.5)
        c_square.next_to(triangle, UP)

        theorem_group = VGroup(triangle, a_square, b_square, c_square)
        theorem_group.center()

        # Animate the scene
        self.play(FadeIn(pythagoras))
        self.play(Write(narration_text))
        self.play(Create(triangle), Create(a_square), Create(b_square), Create(c_square))

        self.wait()

        # Remove elements
        self.play(FadeOut(pythagoras), FadeOut(narration_text), FadeOut(theorem_group))

        self.wait()