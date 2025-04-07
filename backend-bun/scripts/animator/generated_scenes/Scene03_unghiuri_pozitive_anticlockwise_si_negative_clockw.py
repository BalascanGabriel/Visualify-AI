from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene03_unghiuri_pozitive_anticlockwise_si_negative_clockw(Scene):
    def construct(self):
        title = Text("Unghiuri pozitive (anticlockwise) și negative (clockwise)", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Unghiurile pozitive sunt măsurate în sens invers acelor de ceasornic (anticlockwise), iar unghiurile negative sunt măsurate în sensul acelor de ceasornic (clockwise).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        arrow_positive = Arrow(start=circle.get_center(), end=circle.point_at_angle(PI/4), buff=0, color=GREEN)
        theta_positive = MathTex(r"\theta = \frac{\pi}{4}", font_size=36)
        theta_positive.next_to(arrow_positive, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow_positive), Write(theta_positive))
        self.wait(1)
        arrow_negative = Arrow(start=circle.get_center(), end=circle.point_at_angle(-PI/4), buff=0, color=RED)
        theta_negative = MathTex(r"\theta = -\frac{\pi}{4}", font_size=36)
        theta_negative.next_to(arrow_negative, RIGHT, buff=0.2)
        self.play(GrowArrow(arrow_negative), Write(theta_negative))
        self.wait(1)
        explanation2 = Text("Unghiul  "+r"$\frac{\pi}{4}$"+ " este pozitiv (anticlockwise), iar unghiul " + r"$-\frac{\pi}{4}$" + " este negativ (clockwise).", color=WHITE)
        explanation2.next_to(theta_negative, DOWN, buff=0.5)
        self.play(Write(explanation2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(arrow_positive),
        FadeOut(theta_positive),
        FadeOut(arrow_negative),
        FadeOut(theta_negative)
        )
