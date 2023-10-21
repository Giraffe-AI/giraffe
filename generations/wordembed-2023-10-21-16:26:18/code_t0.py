from manim import *

class WordEmbeddings(Scene):
    def construct(self):
        # Create the 3D space
        axes = ThreeDAxes()

        # Create the points
        king_point = Dot3D(np.array([1, 2, 0]))
        queen_point = Dot3D(np.array([1, 3, 0]))
        man_point = Dot3D(np.array([2, 2, 0]))
        woman_point = Dot3D(np.array([2, 3, 0]))

        # Create the labels
        king_label = Text("king").next_to(king_point, RIGHT)
        queen_label = Text("queen").next_to(queen_point, RIGHT)
        man_label = Text("man").next_to(man_point, LEFT)
        woman_label = Text("woman").next_to(woman_point, LEFT)

        # Create the arrows
        arrow1 = Arrow(man_point.get_center(), king_point.get_center(), buff=0)
        arrow2 = Arrow(woman_point.get_center(), queen_point.get_center(), buff=0)

        # Create the arrow labels
        arrow1_label = Text("royalty").next_to(arrow1, UP)
        arrow2_label = Text("royalty").next_to(arrow2, UP)

        # Add everything to the scene
        self.add(axes, king_point, queen_point, man_point, woman_point, king_label, queen_label, man_label, woman_label, arrow1, arrow2, arrow1_label, arrow2_label)

        # Emphasize the arrows
        self.play(GlowEffect(arrow1), GlowEffect(arrow2), run_time=2)
        self.wait()