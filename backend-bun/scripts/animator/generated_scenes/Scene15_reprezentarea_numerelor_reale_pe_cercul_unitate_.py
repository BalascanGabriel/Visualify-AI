from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene15_reprezentarea_numerelor_reale_pe_cercul_unitate_(Scene):
    def construct(self):
        title = Text("Reprezentarea numerelor reale pe cercul unitate.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm cercul unitate centrat în originea sistemului de coordonate.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        explanation2 = Text("Fiecare număr real \\(x\\) poate fi reprezentat ca un punct pe cerc, corespunzând unui unghi \\(\\theta\\) măsurat de la axa pozitivă \\(x\\).", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(explanation2))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        axes = Axes(
        x_range=[-1.2, 1.2, 1],
        y_range=[-1.2, 1.2, 1],
        x_length=2.4,
        y_length=2.4,
        axis_config={"include_numbers": True},
        )
        self.play(Create(axes))
        theta = ValueTracker(0)
        dot = Dot(axes.c2p(1,0), color=RED)
        line = Line(axes.c2p(0,0), axes.c2p(1,0))
        def update_dot(mob):
        x = np.cos(theta.get_value())
        y = np.sin(theta.get_value())
        mob.move_to(axes.c2p(x,y))
        dot.add_updater(update_dot)
        self.play(theta.animate.set_value(2*PI), run_time=5)
        dot.remove_updater(update_dot)
        self.wait()
        formula1 = MathTex(r"\theta = x", font_size=40)
        formula1.to_edge(DOWN)
        self.play(Write(formula1))
        formula2 = MathTex(r"x \in \mathbb{R}", font_size=40)
        formula2.next_to(formula1, RIGHT)
        self.play(Write(formula2))
        explanation3 = Text("Unghiul \\(\\theta\\) este proporțional cu numărul real \\(x\\).", color=WHITE)
        explanation3.next_to(formula2, DOWN, buff=0.5)
        self.play(Write(explanation3))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(circle),
        FadeOut(axes),
        FadeOut(dot),
        FadeOut(formula1),
        FadeOut(formula2)
        )
