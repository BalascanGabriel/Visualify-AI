from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene20_extinderea_definitiei_la_numere_reale(Scene):
    def construct(self):
        title = Text("Extinderea definiției la numere reale", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation1 = Text("Funcțiile trigonometrice sunt inițial definite pentru unghiuri în triunghiuri dreptunghice.", color=WHITE)
        explanation1.next_to(title, DOWN, buff=1)
        self.play(Write(explanation1))
        formula1 = MathTex(r"\sin(\theta) = \frac{\text{opus}}{\text{hipotenuză}}", r"\quad", r"\cos(\theta) = \frac{\text{adjacent}}{\text{hipotenuză}}", r"\quad", r"\tan(\theta) = \frac{\text{opus}}{\text{adjacent}}")
        formula1.next_to(explanation1, DOWN, buff=0.5)
        self.play(Write(formula1))
        explanation2 = Text("Dar putem extinde definiția acestor funcții la toate numerele reale utilizând cercul trigonometric.", color=WHITE)
        explanation2.next_to(formula1, DOWN, buff=1)
        self.play(Write(explanation2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line_x = Line([-2,0,0],[2,0,0],color=WHITE)
        line_y = Line([0,-2,0],[0,2,0],color=WHITE)
        self.play(Create(line_x), Create(line_y))
        theta = MathTex(r"\theta").scale(1.5).set_color(RED)
        theta.move_to([1,0.8,0])
        arc = Arc(radius=1, start_angle=0, angle=PI/4, color=RED)
        self.play(Create(arc),Write(theta))
        point = Dot([1,1,0],color=RED)
        self.play(Create(point))
        formula2 = MathTex(r"\sin(\theta) = y", r"\quad", r"\cos(\theta) = x", r"\quad", r"\tan(\theta) = \frac{y}{x}")
        formula2.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula2))
        explanation3 = Text("Astfel, funcțiile trigonometrice sunt definite pentru orice unghi, reprezentat de un număr real,  pe cercul trigonometric.", color=WHITE)
        explanation3.next_to(formula2, DOWN, buff=1)
        self.play(Write(explanation3))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation1),
        FadeOut(formula1),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(line_x),
        FadeOut(line_y),
        FadeOut(theta),
        FadeOut(arc),
        FadeOut(point),
        FadeOut(formula2),
        FadeOut(explanation3)
        )
