from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene09_relatia_dintre_radiani_si_grade_2_radiani_360_(Scene):
    def construct(self):
        title = Text("Relația dintre radiani și grade: 2π radiani = 360°", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc complet are 360 de grade (360°).  Aceeași rotație completă poate fi exprimată și în radiani, folosind π (pi), unde π ≈ 3.14159.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"360^\circ = 2\pi \text{ radiani}")
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"180^\circ = \pi \text{ radiani}")
        formula2.next_to(formula1, DOWN, buff=1)
        self.play(Write(formula2))
        formula3 = MathTex(r"1 \text{ radian} = \frac{180^\circ}{\pi}")
        formula3.next_to(formula2, DOWN, buff=1)
        self.play(Write(formula3))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        arc = Arc(radius=2, start_angle=0, angle=TAU, color=RED)
        self.play(Create(arc))
        arc_label = MathTex(r"2\pi \text{ radiani}", color=RED)
        arc_label.next_to(arc, DOWN)
        self.play(Write(arc_label))
        degree_label = MathTex(r"360^\circ", color=BLUE)
        degree_label.next_to(arc, UP)
        self.play(Write(degree_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(arc_label),
        FadeOut(degree_label)
        )
