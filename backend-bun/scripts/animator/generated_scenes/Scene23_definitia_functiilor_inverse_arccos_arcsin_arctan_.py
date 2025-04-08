from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene23_definitia_functiilor_inverse_arccos_arcsin_arctan_(Scene):
    def construct(self):
        title = Text("Definiția funcțiilor inverse (arccos, arcsin, arctan).", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Funcțiile inverse trigonometrice (arccos, arcsin, arctan) ne dau unghiul în funcție de valoarea raportului trigonometric.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        arcsin_formula = MathTex(r"\arcsin(x) = y \iff \sin(y) = x, \quad -\frac{\pi}{2} \le y \le \frac{\pi}{2}")
        arcsin_formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(arcsin_formula))
        arccos_formula = MathTex(r"\arccos(x) = y \iff \cos(y) = x, \quad 0 \le y \le \pi")
        arccos_formula.next_to(arcsin_formula, DOWN, buff=1)
        self.play(Write(arccos_formula))
        arctan_formula = MathTex(r"\arctan(x) = y \iff \tan(y) = x, \quad -\frac{\pi}{2} < y < \frac{\pi}{2}")
        arctan_formula.next_to(arccos_formula, DOWN, buff=1)
        self.play(Write(arctan_formula))
        example_text = Text("Exemplu:  \\( \arcsin(\frac{1}{2}) = \frac{\pi}{6} \\) deoarece \\( \sin(\frac{\pi}{6}) = \frac{1}{2} \\)", color=WHITE)
        example_text.next_to(arctan_formula, DOWN, buff=1)
        self.play(Write(example_text))
        domain_restriction_text = Text("Observație: Domeniul de definiție este restricționat pentru a asigura unicitatea.", color=YELLOW)
        domain_restriction_text.next_to(example_text, DOWN, buff=1)
        self.play(Write(domain_restriction_text))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(arcsin_formula),
        FadeOut(arccos_formula),
        FadeOut(arctan_formula),
        FadeOut(example_text),
        FadeOut(domain_restriction_text)
        )
