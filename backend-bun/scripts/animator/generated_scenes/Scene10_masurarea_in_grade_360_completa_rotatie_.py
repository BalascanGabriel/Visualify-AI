from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene10_masurarea_in_grade_360_completa_rotatie_(Scene):
    def construct(self):
        title = Text("Măsurarea în grade (360° completă rotație).", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("O rotație completă în jurul unui punct se măsoară în 360 de grade (360°).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=2, color=YELLOW)
        self.play(Create(circle))
        angle = Angle(circle.get_edge_center(UP), circle.get_center(), circle.get_edge_center(RIGHT), radius=0.7, color=RED)
        angle_label = MathTex(r"360^\circ", color=RED)
        angle_label.next_to(angle, 1.2*UP)
        self.play(Create(angle), Write(angle_label))
        explanation2 = Text("Aceasta reprezintă o rotație completă.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=1)
        self.play(Write(explanation2))
        #Demonstrație rotație
        self.play(Rotate(angle, angle.get_angle(), about_point=circle.get_center(), rate_func=linear))
        self.wait(1)
        self.play(Uncreate(angle))
        explanation3 = Text("Un cerc are 360°.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff =1)
        self.play(Write(explanation3))
        #Adăugare arc de 90 de grade
        arc = Arc(start_angle=0, angle=PI/2, radius=2, color=GREEN)
        arc_label = MathTex(r"90^\circ", color=GREEN)
        arc_label.next_to(arc.get_center(), RIGHT)
        self.play(Create(arc), Write(arc_label))
        explanation4 = MathTex(r"\frac{360^\circ}{4} = 90^\circ", color=GREEN)
        explanation4.next_to(explanation3, DOWN, buff=1)
        self.play(Write(explanation4))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(explanation4),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(arc_label),
        )
