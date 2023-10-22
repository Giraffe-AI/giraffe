from manim import *

class EquatingAreas(Scene):
    def construct(self):
        # Define the variables
        a = 3
        b = 4
        c = 5

        # Create the larger square
        square1 = Square(side_length=a+b).set_color(BLUE)
        self.play(Create(square1))

        # Label the larger square
        square1_label = MathTex("(a + b)^2").next_to(square1, UP)
        self.play(Write(square1_label))

        # Create the four triangles
        triangle1 = Triangle().scale(a).set_color(YELLOW)
        triangle2 = Triangle().scale(a).set_color(YELLOW)
        triangle3 = Triangle().scale(b).set_color(YELLOW)
        triangle4 = Triangle().scale(b).set_color(YELLOW)

        # Position the triangles
        triangle1.next_to(square1, LEFT, buff=0)
        triangle2.next_to(square1, RIGHT, buff=0)
        triangle3.next_to(square1, DOWN, buff=0)
        triangle4.next_to(square1, UP, buff=0)

        # Create the smaller square
        square2 = Square(side_length=c).set_color(RED)
        square2.move_to(square1.get_center())

        # Label the smaller square
        square2_label = MathTex("c^2").next_to(square2, DOWN)
        self.play(Write(square2_label))

        # Show the triangles and smaller square
        self.play(Create(triangle1), Create(triangle2), Create(triangle3), Create(triangle4), Create(square2))

        # Label the combined area
        combined_area_label = MathTex("2ab + c^2").next_to(square2, UP)
        self.play(Write(combined_area_label))

        # Show the equation
        equation = MathTex("(a + b)^2 = 2ab + c^2").to_edge(DOWN)
        self.play(Write(equation))

        self.wait()

# To render the scene, use the following command in your terminal:
# manim -p -ql file_name.py EquatingAreas