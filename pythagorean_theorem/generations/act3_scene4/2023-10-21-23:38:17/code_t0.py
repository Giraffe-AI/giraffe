from manim import *

class EquatingAreas(Scene):
    def construct(self):
        # Define the equation
        equation = MathTex("(a + b)^2", "=", "2ab", "+", "c^2")

        # Position the equation in the center of the screen
        equation.move_to(ORIGIN)

        # Add the equation to the scene
        self.play(Write(equation))

        # Wait for 3 seconds before ending the scene
        self.wait(3)

        # Clear the scene
        self.clear()

# Render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim {script_name} EquatingAreas -ql")