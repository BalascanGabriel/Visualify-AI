from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene15_conversia_intre_grade_si_radiani(Scene):
    def construct(self):
        title = Text("Conversia între grade și radiani", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc complet are 360 de grade sau 2π radiani.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"360^\circ = 2\pi \text{ radiani}")
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"1^\circ = \frac{2\pi}{360} \text{ radiani} = \frac{\pi}{180} \text{ radiani}")
        formula2.next_to(formula1, DOWN, buff=1)
        self.play(Write(formula2))
        formula3 = MathTex(r"x^\circ = x \times \frac{\pi}{180} \text{ radiani}")
        formula3.next_to(formula2, DOWN, buff=1)
        self.play(Write(formula3))
        formula4 = MathTex(r"x \text{ radiani} = x \times \frac{180}{\pi} ^\circ")
        formula4.next_to(formula3, DOWN, buff=1)
        self.play(Write(formula4))
        example = Text("Exemplu: Convertim 90 de grade în radiani:", color=WHITE)
        example.next_to(formula4, DOWN, buff=1)
        self.play(Write(example))
        example_formula = MathTex(r"90^\circ = 90 \times \frac{\pi}{180} = \frac{\pi}{2} \text{ radiani}")
        example_formula.next_to(example, DOWN, buff=1)
        self.play(Write(example_formula))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=GREEN)
        self.play(Create(arc))
        pi_over_2 = MathTex(r"\frac{\pi}{2}").scale(1.5).next_to(arc, RIGHT)
        self.play(Write(pi_over_2))
        ninety_degrees = MathTex(r"90^\circ").scale(1.5).next_to(arc, UP)
        self.play(Write(ninety_degrees))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(formula4),
        FadeOut(example),
        FadeOut(example_formula),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(pi_over_2),
        FadeOut(ninety_degrees)
        )
