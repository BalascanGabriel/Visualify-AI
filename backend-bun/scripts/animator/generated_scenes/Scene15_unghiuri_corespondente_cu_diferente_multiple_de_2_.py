from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene15_unghiuri_corespondente_cu_diferente_multiple_de_2_(Scene):
    def construct(self):
        title = Text("Unghiuri corespondente cu diferențe multiple de 2π", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Două unghiuri, θ₁ și θ₂, sunt corespondente dacă diferența lor este un multiplu întreg de 2π (2πk, unde k este un număr întreg).  Aceasta înseamnă că unghiurile se află în aceeași poziție pe cerc trigonometric.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"\theta_2 = \theta_1 + 2\pi k", font_size=48)
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"k \in \mathbb{Z}", font_size=48)
        formula2.next_to(formula1, RIGHT, buff=1)
        self.play(Write(formula2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        theta1 = 0.5*PI
        theta2 = theta1 + 2*PI
        line1 = Line(ORIGIN, 2*np.array([np.cos(theta1), np.sin(theta1), 0]))
        line2 = Line(ORIGIN, 2*np.array([np.cos(theta2), np.sin(theta2), 0]))
        arc1 = Arc(radius=2, start_angle=0, angle=theta1, color=RED)
        arc2 = Arc(radius=2, start_angle=0, angle=theta2, color=GREEN)
        self.play(Create(line1),Create(arc1))
        self.play(Create(line2),Create(arc2))
        explanation2 = Text("Observăm că unghiurile, deși numeric diferite,  au aceeași poziție pe cerc.", color=WHITE)
        explanation2.next_to(formula2, DOWN, buff=1)
        self.play(Write(explanation2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(arc1),
        FadeOut(arc2)
        )
