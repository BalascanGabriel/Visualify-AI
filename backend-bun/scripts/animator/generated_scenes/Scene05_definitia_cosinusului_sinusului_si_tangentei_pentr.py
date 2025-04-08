from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene05_definitia_cosinusului_sinusului_si_tangentei_pentr(Scene):
    def construct(self):
        title = Text("Definiția cosinusului, sinusului și tangentei pentru toate numerele reale.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm cercul trigonometric cu raza 1.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        explanation2 = Text("Fie \\(\\theta\\) un unghi măsurat în radiani.", color=WHITE)
        explanation2.next_to(explanation, DOWN)
        self.play(FadeIn(explanation2))
        line = Line(ORIGIN, RIGHT)
        self.play(Create(line))
        arc = Arc(radius=1, start_angle=0, angle=PI/2, color=GREEN)
        self.play(Create(arc))
        angle_label = MathTex(r"\theta")
        angle_label.next_to(arc, RIGHT)
        self.play(Write(angle_label))
        point = Dot(circle.point_from_proportion(PI/2/TAU))
        self.play(Create(point))
        line_x = Line(ORIGIN, point.get_center()[0]*RIGHT, color=RED)
        line_y = Line(ORIGIN, point.get_center()[1]*UP, color=BLUE)
        self.play(Create(line_x), Create(line_y))
        sin_formula = MathTex(r"\sin(\theta) = y")
        cos_formula = MathTex(r"\cos(\theta) = x")
        tan_formula = MathTex(r"\tan(\theta) = \frac{y}{x}")
        sin_formula.next_to(explanation2, DOWN, buff=0.5)
        cos_formula.next_to(sin_formula, DOWN)
        tan_formula.next_to(cos_formula, DOWN)
        self.play(Write(sin_formula), Write(cos_formula), Write(tan_formula))
        explanation3 = Text("Pentru orice număr real \\(\\theta\\),  \\(x\\) și \\(y\\) sunt coordonatele punctului de intersecție al razei cu cercul.", color=WHITE)
        explanation3.next_to(tan_formula, DOWN)
        self.play(FadeIn(explanation3))
        explanation4 = Text("Astfel, definim sinusul, cosinusul și tangenta pentru orice număr real.", color=WHITE)
        explanation4.next_to(explanation3, DOWN)
        self.play(FadeIn(explanation4))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(explanation4),
        FadeOut(circle),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(angle_label),
        FadeOut(point),
        FadeOut(line_x),
        FadeOut(line_y),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula)
        )
