from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create the triangle
        triangle = Polygon([0,0,0], [1,0,0], [0,1,0], fill_opacity=0.5)

        # Create the labels for the sides
        labels = [
            Tex("a").next_to(triangle, LEFT),
            Tex("b").next_to(triangle, DOWN),
            Tex("c").next_to(triangle.get_edge_center(RIGHT), RIGHT)
        ]

        # Create the title
        title = Text("Introduction to Pythagorean Theorem").to_edge(UP)

        # Create the narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry.").to_edge(DOWN)

        # Add everything to the scene
        self.add(triangle, *labels, title, narration)

        # Render the scene
        self.wait()