from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()

        # Label the sides of the triangle
        a = Tex("a").next_to(triangle, LEFT)
        b = Tex("b").next_to(triangle, DOWN)
        c = Tex("c").next_to(triangle, RIGHT)

        # Add the triangle and labels to the scene
        self.add(triangle, a, b, c)

        # Create a narration text
        narration = Tex("Welcome to another episode of 3blue1brown. Today, we're going to explore the Pythagorean theorem, a fundamental principle in geometry that you've probably heard of. It's about right-angled triangles, like the one you see here.")
        narration.to_edge(UP)

        # Add the narration to the scene
        self.play(Write(narration))

        # Wait for a while before moving on to the next scene
        self.wait(3)

        # Clear the scene
        self.clear()

# Render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -p -c #FFFFFF --video_dir ~/Downloads/ {script_name} PythagoreanTheorem")