from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene10_minute_si_secunde(Scene):
    def construct(self):
        title = Text("Minute și secunde", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Un minut are 60 de secunde.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula1 = MathTex(r"1 \text{ minut} = 60 \text{ secunde}")
        formula1.next_to(explanation, DOWN)
        self.play(Write(formula1))
        explanation2 = Text("Putem converti minute în secunde prin înmulțire cu 60.", color=WHITE)
        explanation2.next_to(formula1, DOWN)
        self.play(FadeIn(explanation2))
        formula2 = MathTex(r"x \text{ minute} = x \times 60 \text{ secunde}")
        formula2.next_to(explanation2, DOWN)
        self.play(Write(formula2))
        example = Text("Exemplu: 3 minute = 3 \\times 60 = 180 secunde", color=WHITE)
        example.next_to(formula2, DOWN)
        self.play(Write(example))
        explanation3 = Text("Și invers, putem converti secunde în minute prin împărțire la 60.", color=WHITE)
        explanation3.next_to(example, DOWN)
        self.play(FadeIn(explanation3))
        formula3 = MathTex(r"y \text{ secunde} = \frac{y}{60} \text{ minute}")
        formula3.next_to(explanation3, DOWN)
        self.play(Write(formula3))
        example2 = Text("Exemplu: 300 secunde = \\frac{300}{60} = 5 minute", color=WHITE)
        example2.next_to(formula3, DOWN)
        self.play(Write(example2))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(explanation2),
        FadeOut(formula2),
        FadeOut(example),
        FadeOut(explanation3),
        FadeOut(formula3),
        FadeOut(example2)
        )
