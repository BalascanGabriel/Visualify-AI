from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene07_definitia_radianului_ca_lungimea_arcului_pe_cercul(Scene):
    def construct(self):
        title = Text("Definiția radianului ca lungimea arcului pe cercul unitar", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un radian este unghiul subtins la centru de un arc de cerc cu lungimea egală cu raza cercului.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        radius = Line(circle.get_center(), circle.point_at_angle(0), color=RED)
        self.play(Create(radius))
        arc = Arc(radius=2, angle=1, start_angle=0, color=GREEN)
        self.play(Create(arc))
        arc_length_text = MathTex(r"s = r\theta")
        arc_length_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(arc_length_text))
        explanation2 = Text("Dacă \\(\\theta = 1\\) radian, atunci lungimea arcului \\(s\\) este egală cu raza \\(r\\).", color=WHITE)
        explanation2.next_to(arc_length_text, DOWN, buff=1)
        self.play(Write(explanation2))
        theta_text = MathTex(r"\theta = 1 \, \text{radian}")
        theta_text.next_to(explanation2, DOWN, buff=1)
        self.play(Write(theta_text))
        s_equal_r_text = MathTex(r"s = r")
        s_equal_r_text.next_to(theta_text, DOWN, buff=1)
        self.play(Write(s_equal_r_text))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(arc_length_text),
        FadeOut(theta_text),
        FadeOut(s_equal_r_text),
        FadeOut(circle),
        FadeOut(radius),
        FadeOut(arc)
        )
