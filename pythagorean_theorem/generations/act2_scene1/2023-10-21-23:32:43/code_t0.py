from manim import *

class TransitionToProof(Scene):
    def construct(self):
        triangle = Polygon(
            np.array([0,0,0]),
            np.array([1,0,0]),
            np.array([0,1,0]),
            fill_opacity=0.5
        )
        question_mark = Text("?").scale(2).next_to(triangle, UP)
        self.play(FadeIn(triangle))
        self.play(Write(question_mark))
        self.wait(2)
        self.play(FadeOut(triangle), FadeOut(question_mark))
        self.wait()