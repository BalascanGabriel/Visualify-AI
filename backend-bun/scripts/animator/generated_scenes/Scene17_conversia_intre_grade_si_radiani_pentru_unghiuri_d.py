from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene17_conversia_intre_grade_si_radiani_pentru_unghiuri_d(Scene):
    def construct(self):
        title = Text("Conversia între grade și radiani pentru unghiuri date.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Pentru a converti grade în radiani, folosim formula: Radianii = Grade * (π / 180)", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula_radians = MathTex(r"\text{Radianii} = \text{Grade} \times \frac{\pi}{180}")
        formula_radians.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_radians))
        explanation2 = Text("Pentru a converti radiani în grade, folosim formula: Grade = Radianii * (180 / π)", color=WHITE)
        explanation2.next_to(formula_radians, DOWN, buff=1)
        self.play(Write(explanation2))
        formula_degrees = MathTex(r"\text{Grade} = \text{Radianii} \times \frac{180}{\pi}")
        formula_degrees.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula_degrees))
        example1 = Text("Exemplu: Convertim 90 de grade în radiani.", color=WHITE)
        example1.next_to(formula_degrees, DOWN, buff=1)
        self.play(Write(example1))
        example1_calculation = MathTex(r"90^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{2} \text{ radiani}")
        example1_calculation.next_to(example1, DOWN, buff=1)
        self.play(Write(example1_calculation))
        example2 = Text("Exemplu: Convertim π/2 radiani în grade.", color=WHITE)
        example2.next_to(example1_calculation, DOWN, buff=1)
        self.play(Write(example2))
        example2_calculation = MathTex(r"\frac{\pi}{2} \text{ radiani} \times \frac{180^\circ}{\pi} = 90^\circ")
        example2_calculation.next_to(example2, DOWN, buff=1)
        self.play(Write(example2_calculation))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_radians),
        FadeOut(explanation2),
        FadeOut(formula_degrees),
        FadeOut(example1),
        FadeOut(example1_calculation),
        FadeOut(example2),
        FadeOut(example2_calculation)
        )
