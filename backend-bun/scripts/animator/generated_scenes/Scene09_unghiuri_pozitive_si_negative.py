from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene09_unghiuri_pozitive_si_negative(Scene):
    def construct(self):
        title = Text("Unghiuri pozitive și negative", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Unghiurile pozitive sunt măsurate în sens trigonometric pozitiv (contra-sensul acelor de ceasornic), în timp ce unghiurile negative sunt măsurate în sens trigonometric negativ (sensul acelor de ceasornic).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line1 = Line(ORIGIN, 2*RIGHT, color=GREEN)
        self.play(Create(line1))
        line2 = Line(ORIGIN, 2*UP, color=RED)
        self.play(Create(line2))
        angle1 = Angle(line1, line2, radius=0.7, color=BLUE)
        self.play(Create(angle1))
        angle_text1 = MathTex(r"\theta", color=BLUE)
        angle_text1.next_to(angle1, 0.7*UP + 0.3*RIGHT)
        self.play(Write(angle_text1))
        explanation2 = Text("Acesta este un unghi pozitiv  \\theta.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=1)
        self.play(Write(explanation2))
        line3 = Line(ORIGIN, 2*RIGHT, color=GREEN)
        line4 = Line(ORIGIN, 2*DOWN, color=RED)
        angle2 = Angle(line3, line4, radius=0.7, color=PURPLE)
        angle_text2 = MathTex(r"-\theta", color=PURPLE)
        angle_text2.next_to(angle2, 0.7*DOWN + 0.3*RIGHT)
        self.play(ReplacementTransform(line2, line4), ReplacementTransform(angle1, angle2), ReplacementTransform(angle_text1, angle_text2))
        explanation3 = Text("Acesta este un unghi negativ -\\theta.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff=1)
        self.play(Write(explanation3))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(circle),
        FadeOut(line3),
        FadeOut(line4),
        FadeOut(angle_text2),
        FadeOut(angle2)
        )
