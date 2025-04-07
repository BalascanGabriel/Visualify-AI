from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene06_minute_si_secunde_ca_fractiuni_de_grad(Scene):
    def construct(self):
        title = Text("Minute și secunde ca fracțiuni de grad", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un grad este împărțit în 60 de minute, iar un minut este împărțit în 60 de secunde.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula_minutes = MathTex(r"1^\circ = 60' ", font_size=48)
        formula_minutes.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_minutes))
        formula_seconds = MathTex(r"1' = 60''", font_size=48)
        formula_seconds.next_to(formula_minutes, DOWN, buff=0.5)
        self.play(Write(formula_seconds))
        conversion_minutes = MathTex(r"x' = \frac{x}{60}^\circ", font_size=48)
        conversion_minutes.next_to(formula_seconds, DOWN, buff=1)
        self.play(Write(conversion_minutes))
        conversion_seconds = MathTex(r"y'' = \frac{y}{3600}^\circ", font_size=48)
        conversion_seconds.next_to(conversion_minutes, DOWN, buff=0.5)
        self.play(Write(conversion_seconds))
        example = Text("Exemplu: 30' = 30/60 = 0.5°  și 180'' = 180/3600 = 0.05°", color=WHITE)
        example.next_to(conversion_seconds, DOWN, buff=1)
        self.play(Write(example))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_minutes),
        FadeOut(formula_seconds),
        FadeOut(conversion_minutes),
        FadeOut(conversion_seconds),
        FadeOut(example)
        )
