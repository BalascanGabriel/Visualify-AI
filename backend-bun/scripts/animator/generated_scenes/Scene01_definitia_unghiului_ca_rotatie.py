from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene01_definitia_unghiului_ca_rotatie(Scene):
    def construct(self):
        title = Text("Definiția unghiului ca rotație", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un unghi poate fi definit ca o rotație a unei semi-drepte în jurul unui punct fix.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        explanation2 = Text("Considerăm o semi-dreaptă OA, care rotește în jurul punctului O până la poziția OB.", color=WHITE)
        explanation2.next_to(explanation, DOWN, buff=0.5)
        self.play(Write(explanation2))
        # Desenăm un cerc și două semi-drepte
        circle = Circle(radius=2, color=YELLOW)
        line1 = Line(ORIGIN, 2*RIGHT, color=GREEN)
        line2 = Line(ORIGIN, 2*RIGHT, color=GREEN)
        line2.rotate(PI/3, about_point=ORIGIN)
        self.play(Create(circle))
        self.play(Create(line1))
        self.play(Transform(line1.copy(), line2))
        #Adaugam puncte si etichete
        dot_O = Dot(ORIGIN, color=RED)
        dot_A = Dot(2*RIGHT, color=RED)
        dot_B = Dot(line2.get_end(), color=RED)
        label_O = Text("O", color=RED).next_to(dot_O, DOWN)
        label_A = Text("A", color=RED).next_to(dot_A, UP)
        label_B = Text("B", color=RED).next_to(dot_B, UP)
        self.play(Create(dot_O), Create(dot_A), Create(dot_B), Write(label_O), Write(label_A), Write(label_B))
        #Formula pentru unghi
        formula = MathTex(r"\theta", color=YELLOW)
        formula.scale(1.5)
        formula.move_to(line1.get_center()+0.5*UP)
        self.play(Write(formula))
        arc = ArcBetweenPoints(line1.get_end(), line2.get_end(), radius=2, color=YELLOW)
        self.play(Create(arc))
        explanation3 = Text("Mărimea unghiului θ este dată de amploarea rotației.", color=WHITE)
        explanation3.next_to(explanation2, DOWN, buff=0.5)
        self.play(Write(explanation3))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(explanation3),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(formula),
        FadeOut(dot_O),
        FadeOut(dot_A),
        FadeOut(dot_B),
        FadeOut(label_O),
        FadeOut(label_A),
        FadeOut(label_B),
        FadeOut(arc)
        )
