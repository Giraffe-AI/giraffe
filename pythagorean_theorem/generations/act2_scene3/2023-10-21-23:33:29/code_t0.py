from manim import *

class PythagoreanProof(Scene):
    def construct(self):
        # Create the larger square
        square1 = Square(side_length=2)
        self.play(Create(square1))

        # Create the four triangles
        triangle1 = Triangle()
        triangle2 = Triangle()
        triangle3 = Triangle()
        triangle4 = Triangle()

        # Position the triangles
        triangle1.move_to(square1.get_corner(UP+LEFT))
        triangle2.move_to(square1.get_corner(UP+RIGHT))
        triangle3.move_to(square1.get_corner(DOWN+RIGHT))
        triangle4.move_to(square1.get_corner(DOWN+LEFT))

        # Create the smaller square
        square2 = Square(side_length=1)
        square2.move_to(square1.get_center())

        # Add the triangles and smaller square to the scene
        self.play(Create(triangle1), Create(triangle2), Create(triangle3), Create(triangle4), Create(square2))

        # Rearrange the triangles and smaller square
        self.play(
            triangle1.animate.move_to(square1.get_corner(DOWN+LEFT)),
            triangle2.animate.move_to(square1.get_corner(DOWN+RIGHT)),
            triangle3.animate.move_to(square1.get_corner(UP+RIGHT)),
            triangle4.animate.move_to(square1.get_corner(UP+LEFT)),
            square2.animate.move_to(square1.get_center())
        )