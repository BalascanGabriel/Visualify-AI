from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene20_extinderea_definitiei_functiilor_trigonometrice_la(Scene):
    def construct(self):
        title = Text("Extinderea definiției funcțiilor trigonometrice la toate numerele reale.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation1 = Text("Funcțiile trigonometrice, inițial definite pentru unghiuri în intervalul [0, 2π) (sau [0, 360°]), pot fi extinse la toate numerele reale utilizând cercul trigonometric.", color=WHITE)
        explanation1.next_to(title, DOWN, buff=1)
        self.play(Write(explanation1))
        self.wait(2)
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        x_axis = Line((-4,0,0),(4,0,0),color=WHITE)
        y_axis = Line((0,-2.5,0),(0,2.5,0),color=WHITE)
        self.play(Create(x_axis),Create(y_axis))
        angle_label = MathTex(r"\theta")
        angle_label.next_to(circle,RIGHT,buff=0.2)
        self.play(Write(angle_label))
        point = Dot([2,0,0],color=RED)
        self.play(Create(point))
        line = Line(ORIGIN, point.get_center(), color=BLUE)
        self.play(Create(line))
        explanation2 = Text("Considerăm un punct pe cerc.  Unghiul  θ  poate fi măsurat în sens trigonometric pozitiv (contra-sensul acelor de ceasornic) sau negativ (sensul acelor de ceasornic).", color=WHITE)
        explanation2.next_to(explanation1, DOWN, buff=1)
        self.play(Write(explanation2))
        self.wait(2)
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=GREEN)
        self.play(Create(arc))
        explanation3 = Text("Extensia la numere reale se face prin înfășurarea repetată a liniei în jurul cercului.  Un număr real  θ  reprezintă numărul de rotații complete plus unghiul rămas.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff=1)
        self.play(Write(explanation3))
        self.wait(2)
        sin_formula = MathTex(r"\sin(\theta) = y")
        cos_formula = MathTex(r"\cos(\theta) = x")
        sin_formula.next_to(explanation3, DOWN, buff=1)
        cos_formula.next_to(sin_formula, RIGHT, buff=1)
        self.play(Write(sin_formula),Write(cos_formula))
        self.wait(3)
        self.play(
        FadeOut(title),
        FadeOut(explanation1),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(circle),
        FadeOut(x_axis),
        FadeOut(y_axis),
        FadeOut(angle_label),
        FadeOut(point),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(sin_formula),
        FadeOut(cos_formula)
        )
