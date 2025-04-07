from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene04_divizarea_cercului_in_360_de_grade(Scene):
    def construct(self):
        title = Text("Divizarea cercului în 360 de grade", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc complet are 360 de grade. Această diviziune este arbitrară, dar convențională și utilă în matematică și alte domenii.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        degree_marks = []
        for i in range(0, 361, 15):  # Marchează la fiecare 15 grade pentru vizualizare
        angle = i * DEGREES
        point = circle.point_from_proportion(i / 360)
        mark = Line(point, point + rotate_vector(RIGHT, angle), color=WHITE)
        degree_marks.append(mark)
        self.play(*[Create(mark) for mark in degree_marks])
        formula1 = MathTex(r"360^\circ = 2\pi \text{ radiani}", color=GREEN)
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"1^\circ = \frac{2\pi}{360} \text{ radiani} = \frac{\pi}{180} \text{ radiani}", color=GREEN)
        formula2.next_to(formula1, DOWN, buff=0.5)
        self.play(Write(formula2))
        explanation2 = Text("Fiecare grad reprezintă o fracțiune din cerc.", color=WHITE)
        explanation2.next_to(formula2, DOWN, buff=1)
        self.play(Write(explanation2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(formula1),
        FadeOut(formula2),
        *[FadeOut(mark) for mark in degree_marks]
        )
