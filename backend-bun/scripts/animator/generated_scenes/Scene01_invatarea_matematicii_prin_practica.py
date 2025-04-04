from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene01_invatarea_matematicii_prin_practica(Scene):
    def construct(self):
        title = Text("Învățarea matematicii prin practică", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Cea mai bună metodă de a învăța matematică este prin rezolvarea de probleme.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        example1 = Text("Exemplu:  Află aria unui dreptunghi cu laturile a=5 și b=3.", color=WHITE)
        example1.next_to(explanation, DOWN, buff=1)
        self.play(Write(example1))
        formula1 = MathTex(r"Aria = a \times b")
        formula1.next_to(example1, DOWN, buff=0.5)
        self.play(Write(formula1))
        solution1 = MathTex(r"Aria = 5 \times 3 = 15")
        solution1.next_to(formula1, DOWN, buff=0.5)
        self.play(Write(solution1))
        example2 = Text("Exemplu: Rezolvă ecuația  2x + 5 = 11", color=WHITE)
        example2.next_to(solution1, DOWN, buff=1)
        self.play(Write(example2))
        formula2 = MathTex(r"2x + 5 = 11")
        formula2.next_to(example2, DOWN, buff=0.5)
        self.play(Write(formula2))
        steps = BulletedList(
        "Scădem 5 din ambele părți: 2x = 6",
        "Împărțim la 2: x = 3",
        color=WHITE
        )
        steps.next_to(formula2, DOWN, buff=0.5)
        self.play(Write(steps))
        conclusion = Text("Prin practică, înțelegi conceptele și devii mai sigur pe tine!", color=GREEN)
        conclusion.next_to(steps, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(example1),
        FadeOut(formula1),
        FadeOut(solution1),
        FadeOut(example2),
        FadeOut(formula2),
        FadeOut(steps),
        FadeOut(conclusion)
        )
