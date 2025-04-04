from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene17_cateta_opusa(Scene):
    def construct(self):
        title = Text("Catetă opusă", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Catetă opusă este latura unui triunghi dreptunghic opus unghiului considerat.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        triangle = Polygon(np.array([0,0,0]), np.array([4,0,0]), np.array([4,3,0]), color=YELLOW)
        self.play(Create(triangle))
        angle_label = MathTex(r"\theta")
        angle_label.next_to(triangle.get_vertices()[0], RIGHT, buff=0.2)
        self.play(Write(angle_label))
        opposite_side = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], color=RED)
        self.play(Create(opposite_side))
        opposite_label = MathTex(r"a")
        opposite_label.move_to(triangle.get_center() + np.array([0.5,1.5,0]))
        self.play(Write(opposite_label))
        explanation2 = Text("În contextul funcțiilor trigonometrice, catetă opusă este utilizată în definirea sinusului.", color=WHITE)
        explanation2.next_to(explanation, DOWN)
        self.play(FadeIn(explanation2))
        formula = MathTex(r"\sin(\theta) = \frac{\text{catetă opusă}}{\text{hipotenuză}} = \frac{a}{c}")
        formula.next_to(explanation2, DOWN)
        self.play(Write(formula))
        hypotenuse = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], color=BLUE)
        self.play(Create(hypotenuse))
        hypotenuse_label = MathTex(r"c")
        hypotenuse_label.move_to(triangle.get_center()+ np.array([2,0,0]))
        self.play(Write(hypotenuse_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(formula),
        FadeOut(triangle),
        FadeOut(angle_label),
        FadeOut(opposite_side),
        FadeOut(opposite_label),
        FadeOut(hypotenuse),
        FadeOut(hypotenuse_label)
        )
