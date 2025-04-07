from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene10_conversia_de_la_radiani_la_grade_y_radiani_y_180_g(Scene):
    def construct(self):
        title = Text("Conversia de la radiani la grade", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Pentru a converti y radiani în grade, folosim formula:", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(Write(explanation))
        formula = MathTex(r"y \text{ radiani} = y \cdot \left( \frac{180}{\pi} \right) \text{ grade}")
        formula.next_to(explanation, DOWN)
        self.play(Write(formula))
        example = Text("Exemplu:  Convertim  \\pi/2 radiani în grade:", color=WHITE)
        example.next_to(formula, DOWN)
        self.play(Write(example))
        example_calculation = MathTex(r"\frac{\pi}{2} \text{ radiani} = \frac{\pi}{2} \cdot \left( \frac{180}{\pi} \right) \text{ grade} = 90 \text{ grade}")
        example_calculation.next_to(example, DOWN)
        self.play(Write(example_calculation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=GREEN)
        self.play(Create(arc))
        arc_label = MathTex(r"\frac{\pi}{2}").next_to(arc.get_center(), RIGHT)
        self.play(Write(arc_label))
        degree_label = MathTex(r"90^\circ").next_to(arc.get_center(), RIGHT+UP)
        self.play(Write(degree_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(example),
        FadeOut(example_calculation),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(arc_label),
        FadeOut(degree_label)
        )
