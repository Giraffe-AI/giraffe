from manim import *

class SpectralTheorem(Scene):
    def construct(self):
        # Define the matrix and its eigenvectors and eigenvalues
        matrix = np.array([[2, 1], [1, 2]])

        # Create arrow vectors
        vec1 = Arrow(start=[0, 0, 0], end=[1, 1, 0], color=YELLOW)
        vec2 = Arrow(start=[0, 0, 0], end=[1, -1, 0], color=BLUE)

        # Create transformed arrow vectors
        trans_vec1_coords = np.dot(matrix, [1, 1])
        trans_vec1 = Arrow(start=[0, 0, 0], end=[trans_vec1_coords[0], trans_vec1_coords[1], 0], color=YELLOW)

        trans_vec2_coords = np.dot(matrix, [1, -1])
        trans_vec2 = Arrow(start=[0, 0, 0], end=[trans_vec2_coords[0], trans_vec2_coords[1], 0], color=BLUE)

        # Create labels
        vec1_label = MathTex("|v_1\\rangle").next_to(vec1, RIGHT).scale(0.7)
        vec2_label = MathTex("|v_2\\rangle").next_to(vec2, DOWN).scale(0.7)

        trans_vec1_label = MathTex("A|v_1\\rangle").next_to(trans_vec1, RIGHT).scale(0.7)
        trans_vec2_label = MathTex("A|v_2\\rangle").next_to(trans_vec2, DOWN).scale(0.7)

        # Add original vectors to scene
        self.play(Create(vec1), Write(vec1_label))
        self.play(Create(vec2), Write(vec2_label))
        self.wait(1)

        # Transform the vectors
        self.play(Transform(vec1, trans_vec1), Transform(vec1_label, trans_vec1_label))
        self.play(Transform(vec2, trans_vec2), Transform(vec2_label, trans_vec2_label))

        self.wait(1)
