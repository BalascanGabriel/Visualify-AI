from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene11_formula_de_conversie(Scene):
    def construct(self):
        title = Text("Formula de conversie: Celsius în Fahrenheit", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Formula de conversie de la grade Celsius (°C) la grade Fahrenheit (°F) este:", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(FadeIn(explanation))
        formula = MathTex(r"F = \frac{9}{5}C + 32")
        formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula))
        explanation2 = Text("Unde:", color=WHITE)
        explanation2.next_to(formula, DOWN, buff=1)
        self.play(FadeIn(explanation2))
        c_explanation = MathTex(r"C = \text{temperatura in grade Celsius}")
        c_explanation.next_to(explanation2, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(c_explanation))
        f_explanation = MathTex(r"F = \text{temperatura in grade Fahrenheit}")
        f_explanation.next_to(c_explanation, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(Write(f_explanation))
        example = Text("Exemplu: Convertim 20°C în Fahrenheit:", color=WHITE)
        example.next_to(f_explanation, DOWN, buff=1)
        self.play(FadeIn(example))
        example_calculation = MathTex(r"F = \frac{9}{5}(20) + 32 = 36 + 32 = 68")
        example_calculation.next_to(example, DOWN, buff=1)
        self.play(Write(example_calculation))
        result = Text("Deci, 20°C = 68°F", color=GREEN)
        result.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(result))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(explanation2),
        FadeOut(c_explanation),
        FadeOut(f_explanation),
        FadeOut(example),
        FadeOut(example_calculation),
        FadeOut(result)
        )
