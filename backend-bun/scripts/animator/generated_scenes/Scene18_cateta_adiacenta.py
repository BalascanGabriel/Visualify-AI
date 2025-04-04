from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene18_cateta_adiacenta(Scene):
    def construct(self):
        title = Text("Catetă adiacentă", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Catetă adiacentă este latura unui triunghi dreptunghic care este adiacentă (alături) unghiului de referință.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(FadeIn(explanation))
        triangle = Polygon([-2, -1, 0], [2, -1, 0], [2, 1, 0], color=YELLOW, fill_opacity=0.5)
        self.play(Create(triangle))
        angle_theta = Angle(triangle.get_vertices()[0], triangle.get_vertices()[1], triangle.get_vertices()[2], radius=0.5, color=RED)
        self.play(Create(angle_theta))
        theta_label = MathTex(r"\theta", color=RED)
        theta_label.next_to(angle_theta, 0.7*UP+0.4*RIGHT)
        self.play(Write(theta_label))
        adjacent_side = Line(triangle.get_vertices()[1], triangle.get_vertices()[2], color=GREEN)
        adjacent_side_label = MathTex(r"b", color=GREEN)
        adjacent_side_label.next_to(adjacent_side, RIGHT, buff=0.2)
        self.play(Create(adjacent_side),Write(adjacent_side_label))
        explanation2 = Text("În acest triunghi, latura b este catetă adiacentă unghiului θ.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=1)
        self.play(FadeIn(explanation2))
        formula = MathTex(r"\cos(\theta) = \frac{\text{Catetă adiacentă}}{\text{Hipotenuză}} = \frac{b}{c}")
        formula.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(formula),
        FadeOut(triangle),
        FadeOut(angle_theta),
        FadeOut(theta_label),
        FadeOut(adjacent_side),
        FadeOut(adjacent_side_label)
        )
