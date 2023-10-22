from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = RightAngleTriangle()

        # Label the sides of the triangle
        labels = self.get_triangle_labels(triangle, "a", "b", "c")

        # Add the triangle and labels to the scene
        self.play(Create(triangle))
        self.play(Write(labels))

        # Add narration
        self.add_narration("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")

    def get_triangle_labels(self, triangle, *labels):
        # This function returns a VGroup of labels for the sides of the triangle
        return VGroup(*[
            Tex(label).next_to(side, direction=UP)
            for label, side in zip(labels, triangle)
        ])

    def add_narration(self, text):
        # This function adds a narration to the scene
        narration = Text(text)
        self.play(Write(narration))
        self.wait(5)
        self.play(FadeOut(narration))