from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene04_calculul_cosinusului_sinusului_si_tangentei_pentru(Scene):
    def construct(self):
        title = Text("Calculul cosinusului, sinusului și tangentei pentru unghiuri specifice (π/6, π/4, π/2).", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Vom calcula valorile pentru unghiurile π/6, π/4 și π/2 folosind cercul trigonometric.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        pi_6_group = VGroup()
        pi_6_text = MathTex(r"\frac{\pi}{6} \approx 30^\circ")
        pi_6_sin = MathTex(r"\sin\left(\frac{\pi}{6}\right) = \frac{1}{2}")
        pi_6_cos = MathTex(r"\cos\left(\frac{\pi}{6}\right) = \frac{\sqrt{3}}{2}")
        pi_6_tan = MathTex(r"\tan\left(\frac{\pi}{6}\right) = \frac{1}{\sqrt{3}}")
        pi_6_group.add(pi_6_text, pi_6_sin, pi_6_cos, pi_6_tan)
        pi_6_group.arrange(DOWN)
        pi_6_group.next_to(explanation, DOWN, buff=1)
        pi_4_group = VGroup()
        pi_4_text = MathTex(r"\frac{\pi}{4} = 45^\circ")
        pi_4_sin = MathTex(r"\sin\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2}")
        pi_4_cos = MathTex(r"\cos\left(\frac{\pi}{4}\right) = \frac{\sqrt{2}}{2}")
        pi_4_tan = MathTex(r"\tan\left(\frac{\pi}{4}\right) = 1")
        pi_4_group.add(pi_4_text, pi_4_sin, pi_4_cos, pi_4_tan)
        pi_4_group.arrange(DOWN)
        pi_4_group.next_to(pi_6_group, RIGHT, buff=2)
        pi_2_group = VGroup()
        pi_2_text = MathTex(r"\frac{\pi}{2} = 90^\circ")
        pi_2_sin = MathTex(r"\sin\left(\frac{\pi}{2}\right) = 1")
        pi_2_cos = MathTex(r"\cos\left(\frac{\pi}{2}\right) = 0")
        pi_2_tan = MathTex(r"\tan\left(\frac{\pi}{2}\right) = \text{undefined}")
        pi_2_group.add(pi_2_text, pi_2_sin, pi_2_cos, pi_2_tan)
        pi_2_group.arrange(DOWN)
        pi_2_group.next_to(pi_4_group, RIGHT, buff=2)
        self.play(Write(pi_6_group), Write(pi_4_group), Write(pi_2_group))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(pi_6_group),
        FadeOut(pi_4_group),
        FadeOut(pi_2_group),
        FadeOut(circle)
        )
