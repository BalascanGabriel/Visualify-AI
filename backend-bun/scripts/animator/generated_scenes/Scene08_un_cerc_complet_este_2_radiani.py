from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene08_un_cerc_complet_este_2_radiani(Scene):
    def construct(self):
        title = Text("Un cerc complet este 2π radiani", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc are 360 de grade.  Un radian este unghiul subtins de un arc cu lungimea egală cu raza cercului.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula1 = MathTex(r"360^\circ = 2\pi \text{ radiani}")
        formula1.next_to(explanation, DOWN)
        self.play(Write(formula1))
        formula2 = MathTex(r"1 \text{ radian} \approx 57.3^\circ")
        formula2.next_to(formula1, DOWN)
        self.play(Write(formula2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        arc = Arc(radius=2, start_angle=0, angle=TAU, color=RED)
        self.play(Create(arc))
        radius1 = Line(circle.get_center(), circle.point_at_angle(0), color=GREEN)
        radius2 = Line(circle.get_center(), circle.point_at_angle(TAU), color=GREEN)
        self.play(Create(radius1),Create(radius2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(radius1),
        FadeOut(radius2)
        )
