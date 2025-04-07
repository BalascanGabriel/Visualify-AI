from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene02_etichetarea_unghiurilor_cu_litere_grecesti(Scene):
    def construct(self):
        title = Text("Etichetarea unghiurilor cu litere grecești", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Unghiurile sunt adesea etichetate cu litere grecești, cum ar fi \\theta, \\alpha și \\beta.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula1 = MathTex(r"\theta", font_size=72)
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        explanation2 = Text("Acest simbol (θ) reprezintă măsura unghiului.", color=WHITE)
        explanation2.next_to(formula1, DOWN)
        self.play(FadeIn(explanation2))
        formula2 = MathTex(r"\alpha", font_size=72)
        formula2.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula2))
        explanation3 = Text("Și acest simbol (α) poate reprezenta un alt unghi.", color=WHITE)
        explanation3.next_to(formula2, DOWN)
        self.play(FadeIn(explanation3))
        formula3 = MathTex(r"\beta", font_size=72)
        formula3.next_to(explanation3, DOWN, buff=1)
        self.play(Write(formula3))
        explanation4 = Text("Similar, (β) este un alt simbol folosit pentru unghiuri.", color=WHITE)
        explanation4.next_to(formula3, DOWN)
        self.play(FadeIn(explanation4))
        # Exemplu geometric
        circle = Circle(radius=1, color=YELLOW)
        line1 = Line(start=circle.get_center(), end=circle.point_at_angle(PI/4))
        line2 = Line(start=circle.get_center(), end=circle.point_at_angle(0))
        angle = Angle(line1, line2, radius=0.5, color=RED)
        theta_label = MathTex(r"\theta").next_to(angle, 0.5*UP)
        self.play(Create(circle), Create(line1), Create(line2), Create(angle), Write(theta_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(explanation4),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(angle),
        FadeOut(theta_label)
        )
