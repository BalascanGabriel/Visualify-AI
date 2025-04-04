from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene13_reprezentarea_numerelor_reale_pe_cercul_unitar(Scene):
    def construct(self):
        title = Text("Reprezentarea numerelor reale pe cercul unitar", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Fiecare număr real poate fi reprezentat ca un punct pe cercul unitar.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        explanation2 = Text("Luăm în considerare cercul cu raza 1 centrat în origine.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(explanation2))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        explanation3 = Text("Un număr real \\(x\\) corespunde unui punct \\((\\cos(x), \\sin(x))\\) pe cerc.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff=0.5)
        self.play(Write(explanation3))
        formula = MathTex(r"\cos(x)", r"\sin(x)")
        formula.next_to(explanation3, DOWN, buff=0.5)
        formula.scale(1.5)
        self.play(Write(formula[0]), Write(formula[1]))
        dot = Dot(color=RED)
        dot.move_to(circle.point(TAU/4))
        self.play(Create(dot))
        angle_arc = Arc(radius=0.2, start_angle=0, angle=TAU/4, color=GREEN)
        angle_arc.move_to(ORIGIN)
        self.play(Create(angle_arc))
        x_value = MathTex(r"x = \frac{\pi}{2}")
        x_value.next_to(dot, RIGHT, buff=0.5)
        self.play(Write(x_value))
        coords = MathTex(r"(\cos(\frac{\pi}{2}), \sin(\frac{\pi}{2})) = (0, 1)")
        coords.next_to(x_value, DOWN)
        self.play(Write(coords))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(formula),
        FadeOut(circle),
        FadeOut(dot),
        FadeOut(angle_arc),
        FadeOut(x_value),
        FadeOut(coords)
        )
