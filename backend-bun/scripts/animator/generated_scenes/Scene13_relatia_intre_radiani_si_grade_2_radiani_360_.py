from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene13_relatia_intre_radiani_si_grade_2_radiani_360_(Scene):
    def construct(self):
        title = Text("Relația între radiani și grade (2π radiani = 360°).", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un cerc complet are 360 de grade sau 2π radiani.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula = MathTex(r"2\pi \text{ radiani} = 360^\circ")
        formula.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula))
        conversion_factor = MathTex(r"1 \text{ radian} = \frac{360^\circ}{2\pi} \approx 57.3^\circ")
        conversion_factor.next_to(formula, DOWN, buff=1)
        self.play(Write(conversion_factor))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        #Adaugarea unei linii care reprezinta un radian
        line = Line(circle.get_center(), circle.point_at_angle(1), color=RED)
        self.play(Create(line))
        arc = Arc(radius=2, start_angle=0, angle=1, color=GREEN)
        self.play(Create(arc))
        arc_label = MathTex(r"1 \text{ radian}")
        arc_label.next_to(arc, RIGHT, buff=0.2)
        self.play(Write(arc_label))
        #Adaugarea unei linii care reprezinta 360 de grade
        full_circle_arc = Circle(radius=2, color=GREEN, stroke_width=3)
        self.play(Transform(arc, full_circle_arc))
        self.play(FadeOut(line),FadeOut(arc_label))
        full_circle_label = MathTex(r"360^\circ")
        full_circle_label.move_to(circle.get_center())
        self.play(Write(full_circle_label))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(conversion_factor),
        FadeOut(circle),
        FadeOut(full_circle_arc),
        FadeOut(full_circle_label)
        )
