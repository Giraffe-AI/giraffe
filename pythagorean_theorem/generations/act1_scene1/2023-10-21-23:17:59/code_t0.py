from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)
        self.play(Create(triangle))

        # Label the sides
        labels = ["a", "b", "c"]
        for i, label in enumerate(labels):
            side_label = Tex(label).next_to(triangle.get_edge_center(DOWN if i == 0 else UP if i == 1 else RIGHT), DOWN if i == 0 else UP if i == 1 else LEFT)
            self.play(Write(side_label))

        # Add title
        title = Text("Introduction to Pythagorean Theorem").to_edge(UP)
        self.play(Write(title))

        # Add narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry.").to_edge(DOWN)
        self.play(Write(narration))

        # Wait for a while before moving on to the next scene
        self.wait(3)