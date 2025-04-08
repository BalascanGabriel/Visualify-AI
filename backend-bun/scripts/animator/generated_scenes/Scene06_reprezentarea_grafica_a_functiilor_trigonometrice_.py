from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene06_reprezentarea_grafica_a_functiilor_trigonometrice_(Scene):
    def construct(self):
        title = Text("Reprezentarea grafică a funcțiilor trigonometrice.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Funcțiile trigonometrice (\sin, \cos, \tan) descriu relațiile dintre unghiuri și laturi într-un triunghi dreptunghic, dar pot fi reprezentate grafic pe un sistem de coordonate.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        sin_formula = MathTex(r"\sin(\theta) = \frac{\text{latura opusă}}{\text{hipotenuză}}")
        sin_formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(sin_formula))
        cos_formula = MathTex(r"\cos(\theta) = \frac{\text{latura alăturată}}{\text{hipotenuză}}")
        cos_formula.next_to(sin_formula, DOWN, buff=1)
        self.play(Write(cos_formula))
        tan_formula = MathTex(r"\tan(\theta) = \frac{\text{latura opusă}}{\text{latura alăturată}}")
        tan_formula.next_to(cos_formula, DOWN, buff=1)
        self.play(Write(tan_formula))
        axes = Axes(
        x_range=[-3*PI, 3*PI, PI/2],
        y_range=[-1.5, 1.5, 0.5],
        axis_config={"include_numbers": True}
        )
        self.play(Create(axes))
        sin_graph = axes.plot(lambda x: np.sin(x), color=RED)
        cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN)
        tan_graph = axes.plot(lambda x: np.tan(x), color=BLUE)
        self.play(Create(sin_graph), Create(cos_graph), Create(tan_graph))
        sin_label = MathTex(r"\sin(\theta)").next_to(sin_graph.point_from_proportion(0.5), UP, buff=0.2)
        cos_label = MathTex(r"\cos(\theta)").next_to(cos_graph.point_from_proportion(0.5), UP, buff=0.2)
        tan_label = MathTex(r"\tan(\theta)").next_to(tan_graph.point_from_proportion(0.5), UP, buff=0.2)
        self.play(Write(sin_label), Write(cos_label), Write(tan_label))
        final_explanation = Text("Graficele arată variația funcțiilor trigonometrice în funcție de unghiul θ.", color=YELLOW)
        final_explanation.next_to(tan_label, DOWN, buff=1)
        self.play(Write(final_explanation))
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
        FadeOut(final_explanation)
        )
