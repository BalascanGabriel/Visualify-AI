from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene02_conversia_intre_radiani_si_grade(Scene):
    def construct(self):
        title = Text("Conversia între radiani și grade", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc complet are 360 de grade sau 2π radiani.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"360^\circ = 2\pi \text{ radiani}")
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"1^\circ = \frac{2\pi}{360} \text{ radiani} = \frac{\pi}{180} \text{ radiani}")
        formula2.next_to(formula1, DOWN, buff=1)
        self.play(Write(formula2))
        formula3 = MathTex(r"1 \text{ radian} = \frac{360}{2\pi} ^\circ = \frac{180}{\pi} ^\circ")
        formula3.next_to(formula2, DOWN, buff=1)
        self.play(Write(formula3))
        example_degrees = Text("Exemplu: Convertim 45° în radiani:", color=WHITE)
        example_degrees.next_to(formula3, DOWN, buff=1)
        self.play(Write(example_degrees))
        example_calculation = MathTex(r"45^\circ = 45 \times \frac{\pi}{180} \text{ radiani} = \frac{\pi}{4} \text{ radiani}")
        example_calculation.next_to(example_degrees, DOWN, buff=1)
        self.play(Write(example_calculation))
        example_radians = Text("Exemplu: Convertim π/2 radiani în grade:", color=WHITE)
        example_radians.next_to(example_calculation, DOWN, buff=1)
        self.play(Write(example_radians))
        example_calculation2 = MathTex(r"\frac{\pi}{2} \text{ radiani} = \frac{\pi}{2} \times \frac{180}{\pi} ^\circ = 90^\circ")
        example_calculation2.next_to(example_radians, DOWN, buff=1)
        self.play(Write(example_calculation2))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        self.wait(1)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(example_degrees),
        FadeOut(example_calculation),
        FadeOut(example_radians),
        FadeOut(example_calculation2),
        FadeOut(circle)
        )
