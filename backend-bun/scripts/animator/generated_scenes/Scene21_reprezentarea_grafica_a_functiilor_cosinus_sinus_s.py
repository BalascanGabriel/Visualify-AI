from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene21_reprezentarea_grafica_a_functiilor_cosinus_sinus_s(Scene):
    def construct(self):
        title = Text("Reprezentarea grafică a funcțiilor cosinus, sinus și tangentă.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Vom reprezenta grafic funcțiile trigonometrice fundamentale: sinus, cosinus și tangentă.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(FadeIn(explanation))
        sin_formula = MathTex(r"\sin(\theta) = \frac{\text{latura opusă}}{\text{ipotenuză}}")
        sin_formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(sin_formula))
        cos_formula = MathTex(r"\cos(\theta) = \frac{\text{latura adiacentă}}{\text{ipotenuză}}")
        cos_formula.next_to(sin_formula, DOWN, buff=1)
        self.play(Write(cos_formula))
        tan_formula = MathTex(r"\tan(\theta) = \frac{\text{latura opusă}}{\text{latura adiacentă}}")
        tan_formula.next_to(cos_formula, DOWN, buff=1)
        self.play(Write(tan_formula))
        axes = Axes(
        x_range=[-3 * PI, 3 * PI, PI / 2],
        y_range=[-2, 2, 1],
        axis_config={"include_numbers": True},
        )
        axes.to_edge(DOWN)
        self.play(Create(axes))
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED)
        cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN)
        tan_graph = axes.plot(lambda x: np.tan(x), color=BLUE)
        self.play(Create(sin_graph), run_time=2)
        self.play(Create(cos_graph), run_time=2)
        self.play(Create(tan_graph), run_time=2)
        sin_label = MathTex(r"y = \sin(x)").next_to(sin_graph.get_end(), RIGHT)
        cos_label = MathTex(r"y = \cos(x)").next_to(cos_graph.get_end(), RIGHT)
        tan_label = MathTex(r"y = \tan(x)").next_to(tan_graph.get_end(), RIGHT)
        self.play(Write(sin_label))
        self.play(Write(cos_label))
        self.play(Write(tan_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(axes),
        FadeOut(sin_graph),
        FadeOut(cos_graph),
        FadeOut(tan_graph),
        FadeOut(sin_label),
        FadeOut(cos_label),
        FadeOut(tan_label),
        )
