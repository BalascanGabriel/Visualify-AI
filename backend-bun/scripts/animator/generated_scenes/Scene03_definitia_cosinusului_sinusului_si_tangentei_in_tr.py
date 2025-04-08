from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene03_definitia_cosinusului_sinusului_si_tangentei_in_tr(Scene):
    def construct(self):
        title = Text("Definiția cosinusului, sinusului și tangentei în triunghiuri dreptunghice.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm un triunghi dreptunghic cu unghiul ascuțit \\theta.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        triangle = Triangle(color=YELLOW)
        triangle.scale(2).move_to(ORIGIN)
        self.play(Create(triangle))
        #Adaugam etichete
        a = MathTex("a").next_to(triangle.get_vertices()[1], LEFT)
        b = MathTex("b").next_to(triangle.get_vertices()[2], DOWN)
        c = MathTex("c").next_to(triangle.get_center(), RIGHT, buff=0.2).scale(1.2)
        theta = MathTex(r"\theta").next_to(triangle.get_vertices()[0], DOWN)
        self.play(Write(a),Write(b), Write(c), Write(theta))
        sin_formula = MathTex(r"\sin(\theta) = \frac{a}{c}")
        sin_formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(sin_formula))
        cos_formula = MathTex(r"\cos(\theta) = \frac{b}{c}")
        cos_formula.next_to(sin_formula, DOWN)
        self.play(Write(cos_formula))
        tan_formula = MathTex(r"\tan(\theta) = \frac{a}{b}")
        tan_formula.next_to(cos_formula, DOWN)
        self.play(Write(tan_formula))
        explanation2 = Text("unde:", color=WHITE)
        explanation2.next_to(tan_formula, DOWN, buff=0.5)
        self.play(FadeIn(explanation2))
        a_explanation = Text("a este latura opusă unghiului \\theta", color=WHITE)
        a_explanation.next_to(explanation2, DOWN)
        self.play(Write(a_explanation))
        b_explanation = Text("b este latura adiacentă unghiului \\theta", color=WHITE)
        b_explanation.next_to(a_explanation, DOWN)
        self.play(Write(b_explanation))
        c_explanation = Text("c este ipotenuza (latura opusă unghiului drept)", color=WHITE)
        c_explanation.next_to(b_explanation, DOWN)
        self.play(Write(c_explanation))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(explanation2),
        FadeOut(a_explanation),
        FadeOut(b_explanation),
        FadeOut(c_explanation),
        FadeOut(triangle),
        FadeOut(a),
        FadeOut(b),
        FadeOut(c),
        FadeOut(theta)
        )
