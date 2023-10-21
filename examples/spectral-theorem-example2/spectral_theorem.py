from manim import *

# Scene 1: Imagining Eigenvectors
class ImaginingEigenvectors(Scene):
    def construct(self):
        self.next_scene = "Orthogonality"
        vec = Arrow(start=np.array([0,0,0]), end=np.array([1,1,0]), color=BLUE)
        self.play(Create(vec))
        self.play(vec.animate.scale(2), run_time=2)
        self.play(vec.animate.scale(0.5), run_time=2)

# Scene 2: Orthogonality
class Orthogonality(Scene):
    def construct(self):
        self.next_scene = "Diagonalization"
        vec1 = Arrow(start=np.array([0,0,0]), end=np.array([1,1,0]), color=BLUE)
        vec2 = Arrow(start=np.array([0,0,0]), end=np.array([1,-1,0]), color=RED)
        self.play(Create(vec1), Create(vec2))
        self.play(vec1.animate.scale(2), vec2.animate.scale(2), run_time=2)
        self.play(vec1.animate.scale(0.5), vec2.animate.scale(0.5), run_time=2)

# Scene 3: Diagonalization
class Diagonalization(Scene):
    def construct(self):
        self.next_scene = "PuttingItTogether"
        diag_matrix = IntegerMatrix([[2, 0], [0, 2]])
        self.play(Create(diag_matrix))
        self.wait(2)

# Scene 4: Putting it Together
class PuttingItTogether(Scene):
    def construct(self):
        vec1 = Arrow(start=np.array([0,0,0]), end=np.array([1,1,0]), color=BLUE)
        vec2 = Arrow(start=np.array([0,0,0]), end=np.array([1,-1,0]), color=RED)
        diag_matrix = IntegerMatrix([[2, 0], [0, 2]])
        self.play(Create(vec1), Create(vec2), Create(diag_matrix))
        self.play(vec1.animate.scale(2), vec2.animate.scale(2), run_time=2)
        self.play(vec1.animate.scale(0.5), vec2.animate.scale(0.5), run_time=2)
        self.wait(2)
