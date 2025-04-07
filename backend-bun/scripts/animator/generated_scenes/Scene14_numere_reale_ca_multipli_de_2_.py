from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene14_numere_reale_ca_multipli_de_2_(Scene):
    def construct(self):
        title = Text("Numere Reale ca Multipli de 2π", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Numerele reale pot fi reprezentate ca multipli ai lui 2π.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"x = n \times 2\pi", font_size=48)
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        explanation2 = Text("unde 'n' este un număr real.", color=WHITE)
        explanation2.next_to(formula1, DOWN, buff=1)
        self.play(Write(explanation2))
        formula2 = MathTex(r"n \in \mathbb{R}", font_size=48)
        formula2.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line = Line(start=circle.get_center(), end=circle.get_top(), color=RED)
        self.play(Create(line))
        arc = Arc(radius=2, start_angle=0, angle=TAU, color=GREEN)
        self.play(Create(arc))
        explanation3 = Text("2π reprezintă circumferința unui cerc cu raza 1.", color=WHITE)
        explanation3.next_to(formula2,DOWN, buff=1)
        self.play(Write(explanation3))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(explanation2),
        FadeOut(formula2),
        FadeOut(circle),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(explanation3)
        )
