from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene02_conversia_intre_radiani_si_grade_(Scene):
    def construct(self):
        title = Text("Conversia între radiani și grade.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Radiani și grade sunt două unități de măsură pentru unghiuri.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        formula1 = MathTex(r"180^\circ = \pi \text{ radiani}")
        formula1.next_to(explanation, DOWN)
        self.play(Write(formula1))
        explanation2 = Text("Pentru a converti din grade în radiani:", color=WHITE)
        explanation2.next_to(formula1, DOWN)
        self.play(FadeIn(explanation2))
        formula2 = MathTex(r"\text{Radiani} = \frac{\pi}{180^\circ} \times \text{Grade}")
        formula2.next_to(explanation2, DOWN)
        self.play(Write(formula2))
        explanation3 = Text("Pentru a converti din radiani în grade:", color=WHITE)
        explanation3.next_to(formula2, DOWN)
        self.play(FadeIn(explanation3))
        formula3 = MathTex(r"\text{Grade} = \frac{180^\circ}{\pi} \times \text{Radiani}")
        formula3.next_to(explanation3, DOWN)
        self.play(Write(formula3))
        example1 = Text("Exemplu: Convertiți 90 grade în radiani:", color=WHITE)
        example1.next_to(formula3, DOWN)
        self.play(FadeIn(example1))
        formula4 = MathTex(r"\text{Radiani} = \frac{\pi}{180^\circ} \times 90^\circ = \frac{\pi}{2}")
        formula4.next_to(example1, DOWN)
        self.play(Write(formula4))
        example2 = Text("Exemplu: Convertiți \\frac{\pi}{2} radiani în grade:", color=WHITE)
        example2.next_to(formula4, DOWN)
        self.play(FadeIn(example2))
        formula5 = MathTex(r"\text{Grade} = \frac{180^\circ}{\pi} \times \frac{\pi}{2} = 90^\circ")
        formula5.next_to(example2, DOWN)
        self.play(Write(formula5))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(explanation2),
        FadeOut(formula2),
        FadeOut(explanation3),
        FadeOut(formula3),
        FadeOut(example1),
        FadeOut(formula4),
        FadeOut(example2),
        FadeOut(formula5)
        )
