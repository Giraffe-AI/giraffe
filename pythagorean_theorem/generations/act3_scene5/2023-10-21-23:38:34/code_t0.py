from manim import *

class SolveEquation(Scene):
    def construct(self):
        # Define the equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2")

        # Position the equation in the center of the screen
        equation.move_to(ORIGIN)

        # Add the equation to the scene
        self.play(Write(equation))

        # Define the narration text
        narration = Text("Simplifying this equation, we find that a^2 + b^2 = c^2.")

        # Position the narration text below the equation
        narration.next_to(equation, DOWN)

        # Add the narration to the scene
        self.play(Write(narration))

        # Wait for 3 seconds before ending the scene
        self.wait(3)

        # Clear the scene
        self.play(FadeOut(equation), FadeOut(narration))