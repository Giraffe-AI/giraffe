from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)
        self.play(Create(triangle))

        # Label the sides
        labels = ["a", "b", "c"]
        sides = [Line(triangle.points[i-1], triangle.points[i]) for i in range(3)]
        for side, label in zip(sides, labels):
            side_label = MathTex(label).next_to(side, direction=UP)
            self.play(Write(side_label))

        # Add narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        self.play(Write(narration))

        # Ensure everything fits on screen
        self.wait(5)
        self.play(*[FadeOut(mob) for mob in self.mobjects])