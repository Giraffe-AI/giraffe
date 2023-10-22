from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()
        triangle.set_color(WHITE)

        # Label the sides of the triangle
        labels = ["a", "b", "c"]
        sides = [Line(triangle.points[i-1], triangle.points[i], color=BLUE) for i in range(3)]
        for i in range(3):
            label = Tex(labels[i]).next_to(sides[i], buff=SMALL_BUFF)
            self.add(sides[i], label)

        # Add title
        title = Text("Introduction to Pythagorean Theorem").to_edge(UP)
        self.add(title)

        # Add narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry.")
        self.play(Write(narration))
        self.wait()

        # Remove elements
        self.play(FadeOut(narration))
        self.wait()

        # Ensure no overlap
        self.play(triangle.animate.shift(LEFT))

        # Ensure fit on screen
        self.play(triangle.animate.scale(0.8))

        # Output video
        self.wait()