from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene16_reprezentarea_grafica_a_unghiurilor(Scene):
    def construct(self):
        title = Text("Reprezentarea grafică a unghiurilor", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un unghi este format din două raze care pornesc dintr-un punct comun (vârful unghiului).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        line1 = Line(ORIGIN, 2*RIGHT, color=RED)
        line2 = Line(ORIGIN, 2*np.array([np.cos(np.pi/3), np.sin(np.pi/3), 0]), color=GREEN)
        self.play(Create(line1), Create(line2))
        angle_arc = Arc(radius=0.8, start_angle=0, angle=np.pi/3, color=BLUE)
        self.play(Create(angle_arc))
        theta = MathTex(r"\theta")
        theta.next_to(angle_arc, RIGHT, buff=0.2)
        self.play(Write(theta))
        explanation2 = Text("Măsura unghiului \\theta se poate exprima în grade sau radiani.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=1)
        self.play(Write(explanation2))
        degrees = MathTex(r"\theta = 60^\circ")
        radians = MathTex(r"\theta = \frac{\pi}{3} \text{ rad}")
        degrees.next_to(explanation2, DOWN, buff=0.5, aligned_edge=LEFT)
        radians.next_to(degrees, RIGHT, buff=1)
        self.play(Write(degrees), Write(radians))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(angle_arc),
        FadeOut(theta),
        FadeOut(degrees),
        FadeOut(radians)
        )
