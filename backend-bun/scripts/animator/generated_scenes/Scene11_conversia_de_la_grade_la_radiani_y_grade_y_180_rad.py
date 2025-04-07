from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene11_conversia_de_la_grade_la_radiani_y_grade_y_180_rad(Scene):
    def construct(self):
        title = Text("Conversia de la grade la radiani", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Pentru a converti y grade în radiani, folosim formula:", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula = MathTex(r"y \text{ grade} = y \times \left( \frac{\pi}{180} \right) \text{ radiani}")
        formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula))
        example_text = Text("Exemplu: 90 grade =", color=WHITE)
        example_text.next_to(formula, DOWN, buff=1)
        self.play(Write(example_text))
        example_calculation = MathTex(r"90 \times \left( \frac{\pi}{180} \right) = \frac{\pi}{2} \text{ radiani}")
        example_calculation.next_to(example_text, RIGHT, buff=0.5)
        self.play(Write(example_calculation))
        explanation2 = Text("Deci, 90 grade sunt egale cu π/2 radiani.", color=WHITE)
        explanation2.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(explanation2))
        circle = Circle(radius=2, color=YELLOW)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=RED)
        self.play(Create(arc))
        arc_label = MathTex(r"\frac{\pi}{2}").scale(1.2)
        arc_label.next_to(arc.get_center(), RIGHT, buff=0.2)
        self.play(Write(arc_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(example_text),
        FadeOut(example_calculation),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(arc_label)
        )
