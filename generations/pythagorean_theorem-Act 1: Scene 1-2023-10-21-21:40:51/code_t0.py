from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()
        triangle.set_color(WHITE)

        # Label the sides of the triangle
        labels = ["a", "b", "c"]
        sides = [Line(triangle.points[i-1], triangle.points[i]) for i in range(3)]
        for side, label in zip(sides, labels):
            side_label = Tex(label).next_to(side, DOWN)
            self.play(Write(side), Write(side_label))

        # Add narration
        narration = Tex("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(DOWN)
        self.play(Write(narration))

        # Wait for a while before ending the scene
        self.wait(5)

        # Clear the scene
        self.play(*[FadeOut(mobj) for mobj in self.mobjects])