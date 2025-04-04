from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene05_extinderea_definitiei_functiilor_trigonometrice_la(Scene):
    def construct(self):
        title = Text("Extinderea definiției funcțiilor trigonometrice la numere reale", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation1 = Text("Funcțiile trigonometrice sunt inițial definite pentru unghiuri în triunghiuri dreptunghice.", color=WHITE)
        explanation1.next_to(title, DOWN, buff=1)
        self.play(Write(explanation1))
        formula1 = MathTex(r"\sin(\theta) = \frac{\text{latura opusă}}{\text{hipotenuză}}", r"\quad", r"\cos(\theta) = \frac{\text{latura adiacentă}}{\text{hipotenuză}}", r"\quad", r"\tan(\theta) = \frac{\text{latura opusă}}{\text{latura adiacentă}}")
        formula1.next_to(explanation1, DOWN)
        self.play(Write(formula1))
        explanation2 = Text("Însă, putem extinde definiția acestora la numere reale folosind cercul trigonometric.", color=WHITE)
        explanation2.next_to(formula1, DOWN, buff=1)
        self.play(Write(explanation2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line = Line(ORIGIN, 2*RIGHT)
        self.play(Create(line))
        dot = Dot(2*RIGHT)
        self.play(Create(dot))
        theta = MathTex(r"\theta")
        theta.next_to(line, UP, buff=0.2)
        self.play(Write(theta))
        arc = Arc(radius=2, start_angle=0, angle=PI/3, color=RED)
        self.play(Create(arc))
        explanation3 = Text("Un număr real  \\theta  reprezintă un unghi în radiani.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff=1)
        self.play(Write(explanation3))
        formula2 = MathTex(r"\sin(\theta) = y", r"\quad", r"\cos(\theta) = x")
        formula2.next_to(explanation3, DOWN)
        self.play(Write(formula2))
        explanation4 = Text("unde (x, y) sunt coordonatele punctului de intersecție dintre cerc și linia care formează unghiul \\theta cu axa x.", color=WHITE)
        explanation4.next_to(formula2, DOWN)
        self.play(Write(explanation4))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation1),
        FadeOut(formula1),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(line),
        FadeOut(dot),
        FadeOut(theta),
        FadeOut(arc),
        FadeOut(explanation3),
        FadeOut(formula2),
        FadeOut(explanation4)
        )
