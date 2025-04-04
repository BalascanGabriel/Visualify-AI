from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene03_definitiile_trigonometrice_in_triunghiuri_dreptung(Scene):
    def construct(self):
        title = Text("Definițiile trigonometrice în triunghiuri dreptunghice", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm un triunghi dreptunghic cu unghiul θ.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        triangle = Polygon(np.array([0,0,0]), np.array([4,0,0]), np.array([4,3,0]), color=YELLOW, fill_opacity=0.5)
        self.play(Create(triangle))
        angle_theta = Angle(triangle.get_vertices()[0], triangle.get_vertices()[2], triangle.get_vertices()[1], radius=0.5, color=RED)
        self.play(Create(angle_theta))
        self.add(MathTex(r"\theta").next_to(angle_theta, 0.7*RIGHT))
        a = Line(triangle.get_vertices()[0], triangle.get_vertices()[1], color=GREEN)
        b = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], color=BLUE)
        c = Line(triangle.get_vertices()[1], triangle.get_vertices()[2], color=PURPLE)
        self.play(Create(a), Create(b), Create(c))
        sin_formula = MathTex(r"\sin(\theta) = \frac{\text{cateta opusă}}{\text{ipotenuză}} = \frac{b}{c}")
        sin_formula.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(sin_formula))
        cos_formula = MathTex(r"\cos(\theta) = \frac{\text{cateta adiacentă}}{\text{ipotenuză}} = \frac{a}{c}")
        cos_formula.next_to(sin_formula, DOWN, buff=0.5)
        self.play(Write(cos_formula))
        tan_formula = MathTex(r"\tan(\theta) = \frac{\text{cateta opusă}}{\text{cateta adiacentă}} = \frac{b}{a}")
        tan_formula.next_to(cos_formula, DOWN, buff=0.5)
        self.play(Write(tan_formula))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(triangle),
        FadeOut(angle_theta),
        FadeOut(a),
        FadeOut(b),
        FadeOut(c)
        )
