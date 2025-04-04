from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene04_calculul_cos_sin_si_tan_pentru_unghiuri_specifice(Scene):
    def construct(self):
        title = Text("Calculul cos, sin și tan pentru unghiuri specifice", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Vom calcula cosinusul, sinusul și tangenta pentru unghiuri de 30°, 45° și 60°.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula_sin30 = MathTex(r"\sin(30^\circ) = \frac{1}{2}")
        formula_sin30.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_sin30))
        formula_cos30 = MathTex(r"\cos(30^\circ) = \frac{\sqrt{3}}{2}")
        formula_cos30.next_to(formula_sin30, DOWN)
        self.play(Write(formula_cos30))
        formula_tan30 = MathTex(r"\tan(30^\circ) = \frac{1}{\sqrt{3}}")
        formula_tan30.next_to(formula_cos30, DOWN)
        self.play(Write(formula_tan30))
        formula_sin45 = MathTex(r"\sin(45^\circ) = \frac{\sqrt{2}}{2}")
        formula_sin45.next_to(formula_tan30, DOWN, buff=1)
        self.play(Write(formula_sin45))
        formula_cos45 = MathTex(r"\cos(45^\circ) = \frac{\sqrt{2}}{2}")
        formula_cos45.next_to(formula_sin45, DOWN)
        self.play(Write(formula_cos45))
        formula_tan45 = MathTex(r"\tan(45^\circ) = 1")
        formula_tan45.next_to(formula_cos45, DOWN)
        self.play(Write(formula_tan45))
        formula_sin60 = MathTex(r"\sin(60^\circ) = \frac{\sqrt{3}}{2}")
        formula_sin60.next_to(formula_tan45, DOWN, buff=1)
        self.play(Write(formula_sin60))
        formula_cos60 = MathTex(r"\cos(60^\circ) = \frac{1}{2}")
        formula_cos60.next_to(formula_sin60, DOWN)
        self.play(Write(formula_cos60))
        formula_tan60 = MathTex(r"\tan(60^\circ) = \sqrt{3}")
        formula_tan60.next_to(formula_cos60, DOWN)
        self.play(Write(formula_tan60))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_sin30),
        FadeOut(formula_cos30),
        FadeOut(formula_tan30),
        FadeOut(formula_sin45),
        FadeOut(formula_cos45),
        FadeOut(formula_tan45),
        FadeOut(formula_sin60),
        FadeOut(formula_cos60),
        FadeOut(formula_tan60)
        )
