from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene14_revolutii_complete_si_fractiuni_de_revolutii(Scene):
    def construct(self):
        title = Text("Revoluții complete și fracțiuni de revoluții", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("O revoluție completă este o rotație de 360 grade sau $2\pi$ radiani.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula_360 = MathTex(r"360^\circ = 2\pi \text{ radiani}")
        formula_360.next_to(explanation, DOWN)
        self.play(Write(formula_360))
        explanation2 = Text("Fracțiunile de revoluții reprezintă rotații mai mici de 360 grade.", color=WHITE)
        explanation2.next_to(formula_360, DOWN)
        self.play(FadeIn(explanation2))
        formula_fraction = MathTex(r"\frac{1}{2} \text{ revoluție} = 180^\circ = \pi \text{ radiani}")
        formula_fraction.next_to(explanation2, DOWN)
        self.play(Write(formula_fraction))
        formula_fraction2 = MathTex(r"\frac{1}{4} \text{ revoluție} = 90^\circ = \frac{\pi}{2} \text{ radiani}")
        formula_fraction2.next_to(formula_fraction, DOWN)
        self.play(Write(formula_fraction2))
        circle = Circle(radius=1, color=YELLOW)
        circle.to_edge(LEFT, buff=1)
        self.play(Create(circle))
        arc1 = Arc(radius=1, start_angle=0, angle=PI, color=GREEN)
        arc1.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(arc1))
        arc2 = Arc(radius=1, start_angle=0, angle=PI/2, color=RED)
        arc2.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(arc2))
        self.wait()
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(formula_360),
        FadeOut(formula_fraction),
        FadeOut(formula_fraction2),
        FadeOut(circle),
        FadeOut(arc1),
        FadeOut(arc2)
        )
