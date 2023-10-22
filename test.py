from manim import *

class WordEmbeddingsScene(ThreeDScene):
    def construct(self):
        # Create a 3D space
        axes = ThreeDAxes()
        
        # Define points for words
        king_point = [0, 1, 0]
        queen_point = [0, -1, 0]
        man_point = [2, 1, 0]
        woman_point = [2, -1, 0]
        
        # Create dots for each word
        king_dot = Dot(point=king_point, color=BLUE).label("King")
        queen_dot = Dot(point=queen_point, color=BLUE).label("Queen")
        man_dot = Dot(point=man_point, color=RED).label("Man")
        woman_dot = Dot(point=woman_point, color=RED).label("Woman")
        
        # Create arrows
        royalty_arrow_man = Arrow(man_point, king_point, color=YELLOW)
        royalty_arrow_woman = Arrow(woman_point, queen_point, color=YELLOW)
        
        royalty_label = Text("Royalty").next_to(royalty_arrow_man, UP)

        # Add objects to scene
        self.play(ShowCreation(axes), FadeIn(king_dot), FadeIn(queen_dot), FadeIn(man_dot), FadeIn(woman_dot))
        self.wait(1)
        self.play(GrowArrow(royalty_arrow_man), Write(royalty_label))
        self.play(GrowArrow(royalty_arrow_woman))
        
        # Emphasize the similarity
        self.play(royalty_arrow_man.animate.set_color(GREEN), royalty_arrow_woman.animate.set_color(GREEN))

        self.wait(3)
