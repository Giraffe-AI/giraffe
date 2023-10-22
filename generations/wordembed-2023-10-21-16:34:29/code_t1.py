from manim import *

class WordEmbeddings(Scene):
    def construct(self):
        # Create text objects
        title = Text("Word Embeddings", font="Chalkboard")
        explanations = [
            "When trying to teach computers language, we need a representation that machines can understand.",
            "This is where word embeddings come into play.",
            "They are mathematical vectors that capture the essence of words. Words with similar meanings are represented closely, while unrelated words are distant."
        ]

        # Create a dictionary to store words and their positions
        words_positions = {"cat": LEFT*2, "dog": LEFT, "apple": RIGHT}

        # Create a VGroup for dots and labels
        dots_labels = VGroup()

        # Create dots and labels using a for loop
        for word, position in words_positions.items():
            dot = Dot().shift(position)
            label = Text(word).next_to(dot, DOWN)
            dots_labels.add(dot, label)

        # Add objects to the scene
        self.play(Write(title))
        self.wait(1)
        for explanation in explanations:
            self.play(Write(Text(explanation)))
            self.wait(1)
        self.play(FadeIn(dots_labels))

        # Emphasize similarity by moving dots closer
        self.play(dots_labels.animate.shift(RIGHT))
        self.wait(1)