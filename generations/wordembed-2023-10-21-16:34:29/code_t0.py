from manim import *

class WordEmbeddings(Scene):
    def construct(self):
        # Create text objects
        title = Text("Word Embeddings", font="Chalkboard")
        explanation1 = Text("When trying to teach computers language, we need a representation that machines can understand.")
        explanation2 = Text("This is where word embeddings come into play.")
        explanation3 = Text("They are mathematical vectors that capture the essence of words. Words with similar meanings are represented closely, while unrelated words are distant.")

        # Create dot objects for words
        cat_dot = Dot().shift(LEFT*2)
        dog_dot = Dot().shift(LEFT)
        apple_dot = Dot().shift(RIGHT)

        # Create labels for dots
        cat_label = Text("cat").next_to(cat_dot, DOWN)
        dog_label = Text("dog").next_to(dog_dot, DOWN)
        apple_label = Text("apple").next_to(apple_dot, DOWN)

        # Create lines between dots
        cat_dog_line = Line(cat_dot.get_center(), dog_dot.get_center())
        cat_apple_line = Line(cat_dot.get_center(), apple_dot.get_center())

        # Add objects to the scene
        self.play(Write(title))
        self.wait(1)
        self.play(Write(explanation1))
        self.wait(1)
        self.play(Write(explanation2))
        self.wait(1)
        self.play(Write(explanation3))
        self.wait(1)
        self.play(FadeIn(cat_dot), FadeIn(dog_dot), FadeIn(apple_dot))
        self.play(Write(cat_label), Write(dog_label), Write(apple_label))
        self.play(Create(cat_dog_line), Create(cat_apple_line))

        # Emphasize similarity by moving dots closer
        self.play(cat_dot.animate.shift(RIGHT), dog_dot.animate.shift(RIGHT/2), apple_dot.animate.shift(LEFT))
        self.wait(1)