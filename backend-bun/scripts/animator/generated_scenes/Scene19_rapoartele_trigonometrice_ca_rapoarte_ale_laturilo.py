from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene19_rapoartele_trigonometrice_ca_rapoarte_ale_laturilo(Scene):
    def construct(self):
        title = Text("Rapoartele trigonometrice ca rapoarte ale laturilor triunghiului", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm un triunghi dreptunghic cu unghiul θ.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        triangle = Triangle(color=YELLOW)
        triangle.scale(2)
        triangle.move_to(ORIGIN)
        self.play(Create(triangle))
        #Adăugăm etichetele vârfurilor
        A = Dot(triangle.get_vertices()[0], color=RED)
        B = Dot(triangle.get_vertices()[1], color=GREEN)
        C = Dot(triangle.get_vertices()[2], color=BLUE)
        self.play(Create(A), Create(B), Create(C))
        #Adăugăm etichetele laturilor
        a = Line(B.get_center(),C.get_center())
        b = Line(A.get_center(),C.get_center())
        c = Line(A.get_center(),B.get_center())
        self.play(Create(a),Create(b),Create(c))
        a_label = MathTex("a").next_to(a, DOWN)
        b_label = MathTex("b").next_to(b, LEFT)
        c_label = MathTex("c").next_to(c, UP)
        self.play(Write(a_label), Write(b_label), Write(c_label))
        explanation2 = Text("Rapoartele trigonometrice sunt definite ca:", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=1)
        self.play(Write(explanation2))
        sin_formula = MathTex(r"\sin(\theta) = \frac{\text{latura opusa}}{\text{ipotenuza}} = \frac{a}{c}")
        sin_formula.next_to(explanation2, DOWN, buff=0.5)
        self.play(Write(sin_formula))
        cos_formula = MathTex(r"\cos(\theta) = \frac{\text{latura alăturată}}{\text{ipotenuza}} = \frac{b}{c}")
        cos_formula.next_to(sin_formula, DOWN, buff=0.5)
        self.play(Write(cos_formula))
        tan_formula = MathTex(r"\tan(\theta) = \frac{\text{latura opusă}}{\text{latura alăturată}} = \frac{a}{b}")
        tan_formula.next_to(cos_formula, DOWN, buff=0.5)
        self.play(Write(tan_formula))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(triangle),
        FadeOut(A),
        FadeOut(B),
        FadeOut(C),
        FadeOut(a),
        FadeOut(b),
        FadeOut(c),
        FadeOut(a_label),
        FadeOut(b_label),
        FadeOut(c_label)
        )
