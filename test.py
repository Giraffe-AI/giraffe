from manim import *

class ChainRuleExample(Scene):
    def construct(self):
        # Define the functions and their derivatives
        f = Tex("f(x) = \\sin(x)")
        g = Tex("g(x) = x^2")
        f_deriv = Tex("f'(x) = \\cos(x)")
        g_deriv = Tex("g'(x) = 2x")

        # Position the functions and their derivatives
        f.shift(UP * 2)
        g.next_to(f, DOWN)
        f_deriv.next_to(g, DOWN)
        g_deriv.next_to(f_deriv, DOWN)

        # Define the chain rule formula
        chain_rule = Tex("f'(g(x)) = f'(g(x)) \\cdot g'(x)")

        # Position the chain rule formula
        chain_rule.next_to(g_deriv, DOWN * 2)

        # Define the specific example
        example = Tex("f'(g(x)) = \\cos(x^2) \\cdot 2x")

        # Position the specific example
        example.next_to(chain_rule, DOWN)

        # Add everything to the scene
        self.play(Write(f), Write(g))
        self.wait(1)
        self.play(Write(f_deriv), Write(g_deriv))
        self.wait(1)
        self.play(Write(chain_rule))
        self.wait(1)
        self.play(Write(example))
        self.wait(2)