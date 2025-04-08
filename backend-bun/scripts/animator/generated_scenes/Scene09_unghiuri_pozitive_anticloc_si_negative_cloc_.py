from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene09_unghiuri_pozitive_anticloc_si_negative_cloc_(Scene):
    def construct(self):
        title = Text("Unghiuri pozitive (anticloc) și negative (cloc).", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Unghiurile pozitive sunt măsurate în sens invers acelor de ceasornic (anticloc), iar unghiurile negative sunt măsurate în sensul acelor de ceasornic (cloc).", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line1 = Line(ORIGIN, 2*RIGHT, color=RED)
        self.play(Create(line1))
        angle_positive = Angle(line1, 2*UP, radius=1, color=GREEN)
        angle_positive_label = MathTex(r"\theta > 0").next_to(angle_positive, RIGHT, buff=0.2)
        self.play(Create(angle_positive), Write(angle_positive_label))
        line2 = Line(ORIGIN, 2*RIGHT, color=RED)
        angle_negative = Angle(line2, 2*DOWN, radius=1, color=BLUE)
        angle_negative_label = MathTex(r"\theta < 0").next_to(angle_negative, RIGHT, buff=0.2)
        self.play(Create(angle_negative), Write(angle_negative_label))
        explanation2 = Text("Unghiul verde este pozitiv (anticloc), iar unghiul albastru este negativ (cloc).", color=WHITE)
        explanation2.next_to(angle_negative_label, DOWN)
        self.play(Write(explanation2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(angle_positive),
        FadeOut(angle_positive_label),
        FadeOut(angle_negative),
        FadeOut(angle_negative_label)
        )
