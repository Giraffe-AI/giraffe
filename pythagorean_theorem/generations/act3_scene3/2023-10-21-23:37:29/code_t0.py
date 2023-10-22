from manim import *

class Scene3(Scene):
    def construct(self):
        # Create the four triangles
        triangle1 = Triangle().scale(0.5).shift(LEFT*2 + UP*2)
        triangle2 = Triangle().scale(0.5).shift(RIGHT*2 + UP*2)
        triangle3 = Triangle().scale(0.5).shift(LEFT*2 + DOWN*2)
        triangle4 = Triangle().scale(0.5).shift(RIGHT*2 + DOWN*2)

        # Create the smaller square
        square = Square().scale(0.5)

        # Create the text
        text1 = Text("Each triangle has area 1/2ab").shift(UP*3)
        text2 = Text("So the four triangles together have area 2ab").shift(UP*2)
        text3 = Text("The smaller square has area c^2").shift(UP)

        # Add everything to the scene
        self.play(Write(text1))
        self.wait(1)
        self.play(Write(text2))
        self.wait(1)
        self.play(Write(text3))
        self.wait(1)
        self.play(Create(triangle1), Create(triangle2), Create(triangle3), Create(triangle4), Create(square))
        self.wait(2)

        # Remove the elements no longer needed
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3))
        self.wait(1)

        # Ensure no elements overlap
        self.play(triangle1.animate.shift(LEFT*2), triangle2.animate.shift(RIGHT*2), triangle3.animate.shift(LEFT*2), triangle4.animate.shift(RIGHT*2), square.animate.shift(DOWN*2))
        self.wait(2)

        # Ensure any text, diagrams or formulas fit fully on the screen
        self.play(triangle1.animate.scale(0.8), triangle2.animate.scale(0.8), triangle3.animate.scale(0.8), triangle4.animate.scale(0.8), square.animate.scale(0.8))
        self.wait(2)

        # End scene
        self.play(FadeOut(triangle1), FadeOut(triangle2), FadeOut(triangle3), FadeOut(triangle4), FadeOut(square))