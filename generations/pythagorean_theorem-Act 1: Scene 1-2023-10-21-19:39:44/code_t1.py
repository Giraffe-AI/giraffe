from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()
        triangle.set_color(WHITE)

        # Label the sides of the triangle
        labels = ["a", "b", "c"]
        sides = [Line(triangle.points[i-1], triangle.points[i]) for i in range(3)]
        for label, side in zip(labels, sides):
            self.add(Text(label).next_to(side, UP))

        # Add the triangle to the scene
        self.add(triangle)

        # Narration
        self.play(Create(triangle))
        self.wait()
        self.play(*[Write(Text(label).next_to(side, UP)) for label, side in zip(labels, sides)])
        self.wait()

        # Scene title
        title = Text("Introduction to Pythagorean Theorem", color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        # Scene narration
        narration = Text("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(DOWN)
        self.play(Write(narration))
        self.wait()

# To render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} PythagoreanTheorem -p -ql")