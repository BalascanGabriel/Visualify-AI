from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene21_analiza_graficelor_functiilor_trigonometrice(Scene):
    def construct(self):
        # Titlu
        title = Text("Analiza graficelor funcțiilor trigonometrice", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        # Introducere
        intro = Text("Vom analiza graficele funcțiilor trigonometrice de bază: sinus, cosinus și tangentă.", color=WHITE)
        intro.next_to(title, DOWN, buff=1)
        self.play(Write(intro))
        self.wait(2)
        # Sinus
        sin_text = Text("Funcția Sinus:  \\(\\sin(x)\\)", color=YELLOW)
        sin_text.next_to(intro, DOWN, buff=1)
        sin_graph = ParametricFunction(lambda t: np.array([t, np.sin(t), 0]), t_range=[-3*PI, 3*PI, 0.01], color=YELLOW)
        sin_formula = MathTex(r"\sin(x)", font_size=36)
        sin_formula.next_to(sin_text, DOWN)
        self.play(Write(sin_text))
        self.play(Create(sin_graph))
        self.play(Write(sin_formula))
        self.wait(3)
        # Cosinus
        cos_text = Text("Funcția Cosinus: \\(\\cos(x)\\)", color=GREEN)
        cos_text.next_to(sin_formula, DOWN, buff=1)
        cos_graph = ParametricFunction(lambda t: np.array([t, np.cos(t), 0]), t_range=[-3*PI, 3*PI, 0.01], color=GREEN)
        cos_formula = MathTex(r"\cos(x)", font_size=36)
        cos_formula.next_to(cos_text, DOWN)
        self.play(Write(cos_text))
        self.play(Create(cos_graph))
        self.play(Write(cos_formula))
        self.wait(3)
        # Tangentă
        tan_text = Text("Funcția Tangentă: \\(\\tan(x)\\)", color=RED)
        tan_text.next_to(cos_formula, DOWN, buff=1)
        tan_graph = ParametricFunction(lambda t: np.array([t, np.tan(t), 0]), t_range=[-3*PI, 3*PI, 0.01], color=RED)
        tan_formula = MathTex(r"\tan(x)", font_size=36)
        tan_formula.next_to(tan_text, DOWN)
        self.play(Write(tan_text))
        self.play(Create(tan_graph))
        self.play(Write(tan_formula))
        self.wait(3)
        # Perioadă
        period_text = Text("Observați perioadele funcțiilor.", color=WHITE)
        period_text.next_to(tan_formula, DOWN, buff=1)
        self.play(Write(period_text))
        self.wait(2)
        # Amplitudine
        amplitude_text = Text("Și amplitudinile (pentru sinus și cosinus).", color=WHITE)
        amplitude_text.next_to(period_text, DOWN, buff=1)
        self.play(Write(amplitude_text))
        self.wait(2)
        # Concluzie
        conclusion = Text("Acestea sunt doar funcțiile trigonometrice de bază. Există multe alte funcții și transformări care pot fi aplicate.", color=WHITE)
        conclusion.next_to(amplitude_text, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(3)
        # Final
        self.play(
        FadeOut(title),
        FadeOut(intro),
        FadeOut(sin_text),
        FadeOut(sin_graph),
        FadeOut(sin_formula),
        FadeOut(cos_text),
        FadeOut(cos_graph),
        FadeOut(cos_formula),
        FadeOut(tan_text),
        FadeOut(tan_graph),
        FadeOut(tan_formula),
        FadeOut(period_text),
        FadeOut(amplitude_text),
        FadeOut(conclusion)
        )
