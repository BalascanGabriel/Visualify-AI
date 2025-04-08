from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene18_ipotenuza_cateta_opusa_cateta_adiacenta_(Scene):
    def construct(self):
        title = Text("Ipotenuză, catetă opusă, catetă adiacentă.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Într-un triunghi dreptunghic, ipotenuza este latura opusă unghiului drept.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        triangle = Polygon(np.array([0,0,0]), np.array([4,0,0]), np.array([4,3,0]), color=YELLOW, fill_opacity=0.5)
        self.play(Create(triangle))
        hypotenuse = Line(triangle.points[0], triangle.points[2], color=RED)
        hypotenuse_label = MathTex(r"\text{Ipotenuză}", color=RED)
        hypotenuse_label.next_to(hypotenuse, UP)
        self.play(Create(hypotenuse), Write(hypotenuse_label))
        opposite_side = Line(triangle.points[0], triangle.points[1], color=GREEN)
        opposite_side_label = MathTex(r"\text{Catetă opusă}", color=GREEN)
        opposite_side_label.next_to(opposite_side, RIGHT)
        self.play(Create(opposite_side), Write(opposite_side_label))
        adjacent_side = Line(triangle.points[1], triangle.points[2], color=BLUE)
        adjacent_side_label = MathTex(r"\text{Catetă adiacentă}", color=BLUE)
        adjacent_side_label.next_to(adjacent_side, DOWN)
        self.play(Create(adjacent_side), Write(adjacent_side_label))
        angle_label = MathTex(r"\theta")
        angle_label.next_to(triangle.points[0], RIGHT, buff=0.2)
        self.play(Write(angle_label))
        formula_sin = MathTex(r"\sin(\theta) = \frac{\text{Catetă opusă}}{\text{Ipotenuză}}")
        formula_sin.next_to(adjacent_side_label, DOWN, buff=1)
        self.play(Write(formula_sin))
        formula_cos = MathTex(r"\cos(\theta) = \frac{\text{Catetă adiacentă}}{\text{Ipotenuză}}")
        formula_cos.next_to(formula_sin, DOWN)
        self.play(Write(formula_cos))
        formula_tan = MathTex(r"\tan(\theta) = \frac{\text{Catetă opusă}}{\text{Catetă adiacentă}}")
        formula_tan.next_to(formula_cos, DOWN)
        self.play(Write(formula_tan))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(triangle),
        FadeOut(hypotenuse),
        FadeOut(hypotenuse_label),
        FadeOut(opposite_side),
        FadeOut(opposite_side_label),
        FadeOut(adjacent_side),
        FadeOut(adjacent_side_label),
        FadeOut(angle_label),
        FadeOut(formula_sin),
        FadeOut(formula_cos),
        FadeOut(formula_tan)
        )
