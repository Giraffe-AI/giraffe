from manim import *

class WordEmbeddings(Scene):
    def construct(self):
        # Create the computer screen border
        screen_border = RoundedRectangle(height=6, width=8, color=WHITE)
        self.play(FadeIn(screen_border))

        # Create the text paragraph
        paragraph_text = """
        In tasks like sentiment analysis, it's vital to understand the sentiment or emotion of a word.
        Embeddings allow machines to capture these nuances, letting them 'feel' the text almost like a human would.
        """
        words = paragraph_text.split()
        words_mobjects = [Text(word) for word in words]

        # Highlight words with similar meanings
        similar_words = ["happy", "joyful", "pleased"]
        for word_mobject in words_mobjects:
            if word_mobject.text in similar_words:
                word_mobject.set_color(GREEN)

        # Highlight words with opposite meanings
        opposite_words = ["sad", "unhappy"]
        for word_mobject in words_mobjects:
            if word_mobject.text in opposite_words:
                word_mobject.set_color(RED)

        paragraph = VGroup(*words_mobjects).arrange_in_grid(rows=1)
        paragraph.scale(0.5).next_to(screen_border, UP)
        self.play(Write(paragraph))

        # Narration text
        narration_text = Text("""
        Now, why are these embeddings so crucial?
        """)
        narration_text.next_to(screen_border, DOWN)
        self.play(Write(narration_text))