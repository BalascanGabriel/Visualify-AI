from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene08_functiile_trigonometrice_inverse_(Scene):
    def construct(self):
        title = Text("Funcțiile trigonometrice inverse.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Funcțiile trigonometrice inverse sunt funcții care ne permit să găsim unghiul dintr-o valoare trigonometrică.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        arcsin_formula = MathTex(r"\arcsin(x) = \theta \iff \sin(\theta) = x")
        arcsin_formula.next_to(explanation, DOWN)
        self.play(Write(arcsin_formula))
        arccos_formula = MathTex(r"\arccos(x) = \theta \iff \cos(\theta) = x")
        arccos_formula.next_to(arcsin_formula, DOWN)
        self.play(Write(arccos_formula))
        arctan_formula = MathTex(r"\arctan(x) = \theta \iff \tan(\theta) = x")
        arctan_formula.next_to(arccos_formula, DOWN)
        self.play(Write(arctan_formula))
        example = Text("Exemplu: Dacă \\(\\sin(\\theta) = \\frac{1}{2}\\), atunci \\(\\arcsin(\\frac{1}{2}) = 30^\circ\\)", color=WHITE)
        example.next_to(arctan_formula, DOWN)
        self.play(Write(example))
        domain_range = Text("Domeniul și codomeniul funcțiilor inverse sunt restricționate pentru a asigura o funcție univocă.", color=WHITE)
        domain_range.next_to(example, DOWN)
        self.play(Write(domain_range))
        # Adăugăm un grafic pentru a ilustra mai bine
        axes = Axes(
        x_range=[-1, 1, 0.5],
        y_range=[-1.57, 1.57, 0.785],
        x_length=4,
        y_length=3,
        axis_config={"include_numbers": True}
        )
        arcsin_graph = axes.plot(lambda x: np.arcsin(x), color=YELLOW)
        self.play(Create(axes), Create(arcsin_graph))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(arcsin_formula),
        FadeOut(arccos_formula),
        FadeOut(arctan_formula),
        FadeOut(example),
        FadeOut(domain_range),
        FadeOut(axes),
        FadeOut(arcsin_graph)
        )
