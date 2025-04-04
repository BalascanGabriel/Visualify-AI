from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene08_functii_trigonometrice_inverse(Scene):
    def construct(self):
        title = Text("Funcții trigonometrice inverse", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Funcțiile trigonometrice inverse (\arcsin, \arccos, \arctan) returnează unghiul (în radiani sau grade) al cărui sinus, cosinus, respectiv tangentă este o anumită valoare.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        arcsin_formula = MathTex(r"\arcsin(x) = y \iff \sin(y) = x")
        arcsin_formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(arcsin_formula))
        arccos_formula = MathTex(r"\arccos(x) = y \iff \cos(y) = x")
        arccos_formula.next_to(arcsin_formula, DOWN, buff=1)
        self.play(Write(arccos_formula))
        arctan_formula = MathTex(r"\arctan(x) = y \iff \tan(y) = x")
        arctan_formula.next_to(arccos_formula, DOWN, buff=1)
        self.play(Write(arctan_formula))
        example = Text("Exemplu: \narcsin(1/2) = π/6 (30°), deoarece sin(π/6) = 1/2", color=WHITE)
        example.next_to(arctan_formula, DOWN, buff=1)
        self.play(Write(example))
        domain_range = Text("Domeniul și codomeniul funcțiilor inverse sunt restricționate pentru a asigura o funcție unu-la-unu.", color=WHITE)
        domain_range.next_to(example, DOWN, buff=1)
        self.play(Write(domain_range))
        graph = self.get_graph(lambda x: np.arcsin(x), x_range=[-1,1], color=GREEN)
        self.play(Create(graph))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(arcsin_formula),
        FadeOut(arccos_formula),
        FadeOut(arctan_formula),
        FadeOut(example),
        FadeOut(domain_range),
        FadeOut(graph)
        )
