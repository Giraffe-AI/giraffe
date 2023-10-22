from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()

        # Label the sides of the triangle
        labels = ["a", "b", "c"]
        for side, label in zip(triangle, labels):
            side_label = Tex(label).next_to(side, UP)
            self.add(side_label)

        # Add the triangle to the scene
        self.add(triangle)

        # Add narration
        narration = Tex("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(DOWN)
        self.play(Write(narration))

        # Wait for a while before moving on to the next scene
        self.wait(3)

        # Clear the scene
        self.clear()

# Render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -p -c #000000 --video_dir ~/Videos/ {script_name} PythagoreanTheorem")