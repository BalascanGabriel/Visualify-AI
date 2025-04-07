from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene16_conversia_unghiurilor_date_in_grade_si_radiani_rep(Scene):
    def construct(self):
        title = Text("Conversia unghiurilor date în grade și radiani, reprezentarea grafică", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Pentru a converti un unghi din grade în radiani, folosim formula: Radiani = Grade * (π / 180)", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula_degrees_to_radians = MathTex(r"\text{Radiani} = \text{Grade} \times \frac{\pi}{180}")
        formula_degrees_to_radians.next_to(explanation, DOWN)
        self.play(Write(formula_degrees_to_radians))
        example_degrees = Text("Exemplu: 90 grade", color=WHITE)
        example_degrees.next_to(formula_degrees_to_radians, DOWN)
        self.play(Write(example_degrees))
        calculation_degrees_to_radians = MathTex(r"90^\circ \times \frac{\pi}{180} = \frac{\pi}{2} \text{ radiani}")
        calculation_degrees_to_radians.next_to(example_degrees, DOWN)
        self.play(Write(calculation_degrees_to_radians))
        explanation_radians_to_degrees = Text("Pentru a converti un unghi din radiani în grade, folosim formula: Grade = Radiani * (180 / π)", color=WHITE)
        explanation_radians_to_degrees.next_to(calculation_degrees_to_radians, DOWN)
        self.play(Write(explanation_radians_to_degrees))
        formula_radians_to_degrees = MathTex(r"\text{Grade} = \text{Radiani} \times \frac{180}{\pi}")
        formula_radians_to_degrees.next_to(explanation_radians_to_degrees, DOWN)
        self.play(Write(formula_radians_to_degrees))
        example_radians = Text("Exemplu: π/2 radiani", color=WHITE)
        example_radians.next_to(formula_radians_to_degrees, DOWN)
        self.play(Write(example_radians))
        calculation_radians_to_degrees = MathTex(r"\frac{\pi}{2} \times \frac{180}{\pi} = 90^\circ")
        calculation_radians_to_degrees.next_to(example_radians, DOWN)
        self.play(Write(calculation_radians_to_degrees))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line = Line(ORIGIN, 2*UP)
        self.play(Create(line))
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=GREEN)
        self.play(Create(arc))
        angle_text_degrees = MathTex(r"90^\circ").next_to(arc, RIGHT, buff=0.2)
        angle_text_radians = MathTex(r"\frac{\pi}{2}").next_to(angle_text_degrees, DOWN, buff=0.2)
        self.play(Write(angle_text_degrees), Write(angle_text_radians))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_degrees_to_radians),
        FadeOut(example_degrees),
        FadeOut(calculation_degrees_to_radians),
        FadeOut(explanation_radians_to_degrees),
        FadeOut(formula_radians_to_degrees),
        FadeOut(example_radians),
        FadeOut(calculation_radians_to_degrees),
        FadeOut(circle),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(angle_text_degrees),
        FadeOut(angle_text_radians)
        )
