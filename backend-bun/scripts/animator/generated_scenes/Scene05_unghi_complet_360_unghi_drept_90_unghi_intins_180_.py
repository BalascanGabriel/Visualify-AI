from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene05_unghi_complet_360_unghi_drept_90_unghi_intins_180_(Scene):
    def construct(self):
        title = Text("Unghi complet (360°), unghi drept (90°), unghi întins (180°)", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un unghi complet este un unghi care măsoară 360°. Un unghi drept măsoară 90°, iar un unghi întins măsoară 180°.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula = MathTex(r"360^\circ \text{ (Unghi complet)}")
        formula.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(formula))
        formula2 = MathTex(r"90^\circ \text{ (Unghi drept)}")
        formula2.next_to(formula, DOWN, buff=0.5)
        self.play(Write(formula2))
        formula3 = MathTex(r"180^\circ \text{ (Unghi întins)}")
        formula3.next_to(formula2, DOWN, buff=0.5)
        self.play(Write(formula3))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        line1 = Line(ORIGIN, RIGHT*2)
        self.play(Create(line1))
        line2 = Line(ORIGIN, UP*2)
        self.play(Create(line2))
        right_angle = Arc(radius=0.3, start_angle=-PI/2, angle=PI/2, color=RED)
        right_angle.next_to(ORIGIN,RIGHT)
        self.play(Create(right_angle))
        line3 = Line(ORIGIN, LEFT*2)
        self.play(Create(line3))
        line4 = Line(ORIGIN, DOWN*2)
        self.play(Create(line4))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(line3),
        FadeOut(line4),
        FadeOut(right_angle)
        )
