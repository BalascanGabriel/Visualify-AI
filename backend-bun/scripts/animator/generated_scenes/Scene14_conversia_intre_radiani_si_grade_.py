from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene14_conversia_intre_radiani_si_grade_(Scene):
    def construct(self):
        title = Text("Conversia între radiani și grade.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("180 grade = π radiani.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula_radians_to_degrees = MathTex(r"Grade = \frac{180}{\pi} \times Radiani")
        formula_radians_to_degrees.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_radians_to_degrees))
        example_radians = MathTex(r"\text{Exemplu: } \frac{\pi}{2} \text{ radiani}")
        example_radians.next_to(formula_radians_to_degrees, DOWN, buff=1)
        self.play(Write(example_radians))
        conversion_example = MathTex(r"Grade = \frac{180}{\pi} \times \frac{\pi}{2} = 90^\circ")
        conversion_example.next_to(example_radians, DOWN, buff=1)
        self.play(Write(conversion_example))
        formula_degrees_to_radians = MathTex(r"Radiani = \frac{\pi}{180} \times Grade")
        formula_degrees_to_radians.next_to(conversion_example, DOWN, buff=1)
        self.play(Write(formula_degrees_to_radians))
        example_degrees = MathTex(r"\text{Exemplu: } 360^\circ")
        example_degrees.next_to(formula_degrees_to_radians, DOWN, buff=1)
        self.play(Write(example_degrees))
        conversion_example2 = MathTex(r"Radiani = \frac{\pi}{180} \times 360 = 2\pi")
        conversion_example2.next_to(example_degrees, DOWN, buff=1)
        self.play(Write(conversion_example2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_radians_to_degrees),
        FadeOut(example_radians),
        FadeOut(conversion_example),
        FadeOut(formula_degrees_to_radians),
        FadeOut(example_degrees),
        FadeOut(conversion_example2)
        )
