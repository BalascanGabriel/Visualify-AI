from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene22_derivatele_functiilor_cosinus_sinus_si_tangenta_ne(Scene):
    def construct(self):
        title = Text("Derivatele funcțiilor cosinus, sinus și tangentă", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Derivatele sunt o măsură a ratei de schimbare a unei funcții.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula_sin = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)")
        formula_sin.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_sin))
        self.wait(1)
        formula_cos = MathTex(r"\frac{d}{dx} \cos(x) = -\sin(x)")
        formula_cos.next_to(formula_sin, DOWN, buff=1)
        self.play(Write(formula_cos))
        self.wait(1)
        formula_tan = MathTex(r"\frac{d}{dx} \tan(x) = \sec^2(x)")
        formula_tan.next_to(formula_cos, DOWN, buff=1)
        self.play(Write(formula_tan))
        self.wait(1)
        explanation2 = Text("Aceste formule sunt fundamentale în calcul și au aplicații largi în fizică și inginerie.", color=WHITE)
        explanation2.next_to(formula_tan, DOWN, buff=1)
        self.play(Write(explanation2))
        self.wait(2)
        #Demonstrație grafică (opțional - necesită mai mult cod)
        #Aici puteți adăuga animații care să ilustreze grafic derivatele.
        #Exemplu simplu (necesită ajustări):
        #graph_sin = FunctionGraph(lambda x: np.sin(x), color=YELLOW)
        #self.play(Create(graph_sin))
        #self.wait(2)
        self.wait(1)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula_sin),
        FadeOut(formula_cos),
        FadeOut(formula_tan),
        FadeOut(explanation2)
        )
