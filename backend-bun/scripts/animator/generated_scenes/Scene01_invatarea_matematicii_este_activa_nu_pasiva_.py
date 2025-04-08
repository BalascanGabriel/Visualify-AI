from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene01_invatarea_matematicii_este_activa_nu_pasiva_(Scene):
    def construct(self):
        title = Text("Învățarea matematicii este activă, nu pasivă.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation1 = Text("Pasiv: Citirea unui manual sau vizionarea unei lecții.", color=WHITE)
        explanation1.next_to(title, DOWN, buff=1)
        self.play(Write(explanation1))
        explanation2 = Text("Activ: Rezolvarea de probleme, demonstrarea de teoreme, experimentarea.", color=WHITE)
        explanation2.next_to(explanation1, DOWN, buff=0.5)
        self.play(Write(explanation2))
        formula1 = MathTex(r"2 + 2 = 4")
        formula1.next_to(explanation2, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"\int_0^1 x^2 \, dx = \frac{1}{3}")
        formula2.next_to(formula1, RIGHT, buff=2)
        self.play(Write(formula2))
        rect = SurroundingRectangle(formula1, color=YELLOW)
        self.play(Create(rect))
        arrow = Arrow(formula1.get_right(), formula2.get_left(), buff=0.2)
        self.play(Create(arrow))
        problem = Text("Încearcă să rezolvi:", color=WHITE)
        problem.next_to(formula2, DOWN, buff=1)
        self.play(Write(problem))
        problem_math = MathTex(r"x^2 + 5x + 6 = 0")
        problem_math.next_to(problem, DOWN)
        self.play(Write(problem_math))
        solution = MathTex(r"x = -2, x = -3")
        solution.next_to(problem_math, DOWN)
        solution.set_color(GREEN)
        self.play(Write(solution))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation1),
        FadeOut(explanation2),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(rect),
        FadeOut(arrow),
        FadeOut(problem),
        FadeOut(problem_math),
        FadeOut(solution)
        )
