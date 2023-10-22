from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right-angled triangle
        triangle = Triangle()

        # Label the sides of the triangle
        labels = self.get_triangle_labels(triangle, "a", "b", "c")

        # Add the triangle and labels to the scene
        self.play(Create(triangle))
        self.play(Write(labels))

    def get_triangle_labels(self, triangle, *labels):
        # Get the vertices of the triangle
        vertices = triangle.get_vertices()

        # Create labels for the sides of the triangle
        label_objects = VGroup()
        for vertex, label in zip(vertices, labels):
            label_object = Tex(label).next_to(vertex, direction=DOWN)
            label_objects.add(label_object)

        return label_objects

# Render the scene
if __name__ == "__main__":
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim -p -c #000000 --disable_caching -ql {script_name} PythagoreanTheorem")