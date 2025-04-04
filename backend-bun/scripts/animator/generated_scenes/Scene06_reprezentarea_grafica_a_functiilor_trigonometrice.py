from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene06_reprezentarea_grafica_a_functiilor_trigonometrice(Scene):
    def construct(self):
        # Titlu
        title = Text("Reprezentarea grafică a funcțiilor trigonometrice", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        # Explicație
        explanation = Text("Funcțiile trigonometrice (sinus, cosinus, tangentă) descriu relațiile dintre unghiuri și laturile unui triunghi dreptunghic, dar pot fi reprezentate grafic pentru a vizualiza comportamentul lor.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        # Formule matematice
        sin_formula = MathTex(r"\sin(\theta) = \frac{\text{latura opusă}}{\text{ipotenuză}}")
        cos_formula = MathTex(r"\cos(\theta) = \frac{\text{latura adiacentă}}{\text{ipotenuză}}")
        tan_formula = MathTex(r"\tan(\theta) = \frac{\text{latura opusă}}{\text{latura adiacentă}}")
        sin_formula.next_to(explanation, DOWN, buff=1)
        cos_formula.next_to(sin_formula, DOWN, buff=0.5)
        tan_formula.next_to(cos_formula, DOWN, buff=0.5)
        self.play(Write(sin_formula))
        self.play(Write(cos_formula))
        self.play(Write(tan_formula))
        # Grafice
        axes = Axes(
        x_range=[-2*PI, 2*PI, PI/2],
        y_range=[-1.5, 1.5, 0.5],
        axis_config={"include_numbers": True}
        )
        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN)
        tan_graph = axes.plot(lambda x: np.tan(x), color=RED, x_range=[-PI+0.1, PI-0.1]) # evităm asimptote
        self.play(Create(axes))
        self.play(Create(sin_graph), run_time=2)
        self.play(Create(cos_graph), run_time=2)
        self.play(Create(tan_graph), run_time=2)
        # Legende grafice
        sin_label = Text("sin(θ)", color=YELLOW).next_to(sin_graph.point_from_proportion(0.5), UP)
        cos_label = Text("cos(θ)", color=GREEN).next_to(cos_graph.point_from_proportion(0.5), UP)
        tan_label = Text("tan(θ)", color=RED).next_to(tan_graph.point_from_proportion(0.5), UP)
        self.play(Write(sin_label))
        self.play(Write(cos_label))
        self.play(Write(tan_label))
        # Final
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(axes),
        FadeOut(sin_label),
        FadeOut(cos_label),
        FadeOut(tan_label)
        )
