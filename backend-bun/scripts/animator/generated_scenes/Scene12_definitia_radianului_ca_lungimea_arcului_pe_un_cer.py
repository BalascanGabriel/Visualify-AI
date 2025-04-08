from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene12_definitia_radianului_ca_lungimea_arcului_pe_un_cer(Scene):
    def construct(self):
        # Titlu
        title = Text("Definiția radianului ca lungimea arcului pe un cerc unitate.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        # Explicație
        explanation = Text("Un radian este unghiul central care intersectează un arc de lungime egală cu raza cercului.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        # Cerc unitate
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        # Raza
        radius = Line(ORIGIN, RIGHT, color=RED)
        self.play(Create(radius))
        # Arc
        arc = Arc(radius=1, start_angle=0, angle=1, color=GREEN)
        self.play(Create(arc))
        # Formula
        formula = MathTex(r"1 \text{ radian} = \frac{\text{lungimea arcului}}{\text{raza}} = \frac{r}{r} = 1")
        formula.next_to(explanation, DOWN)
        self.play(Write(formula))
        # Explicație formulă
        formula_explanation = Text("Dacă lungimea arcului este egală cu raza (r=1), atunci unghiul este de 1 radian.", color=WHITE)
        formula_explanation.next_to(formula, DOWN)
        self.play(Write(formula_explanation))
        #Alt exemplu cu un unghi de 2 radiani
        explanation2 = Text("Exemplu: Un unghi de 2 radiani.", color=WHITE)
        explanation2.next_to(formula_explanation, DOWN)
        self.play(FadeIn(explanation2))
        arc2 = Arc(radius=1, start_angle=0, angle=2, color=PURPLE)
        self.play(Create(arc2))
        formula2 = MathTex(r"2 \text{ radiani} = \frac{2r}{r} = 2")
        formula2.next_to(explanation2,DOWN)
        self.play(Write(formula2))
        self.wait(2)
        # Final
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula),
        FadeOut(circle),
        FadeOut(radius),
        FadeOut(arc),
        FadeOut(explanation2),
        FadeOut(formula2),
        FadeOut(formula_explanation),
        FadeOut(arc2)
        )
