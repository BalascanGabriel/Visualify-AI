from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene22_derivatele_functiilor_cosinus_sinus_si_tangenta_ne(Scene):
    def construct(self):
        title = Text("Derivatele funcțiilor cosinus, sinus și tangentă (necesită cunoștințe de calcul diferențial)", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Derivatele funcțiilor trigonometrice sunt fundamentale în calcul.  Să explorăm derivatele lui sin(x), cos(x) și tan(x).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(FadeIn(explanation))
        sin_deriv = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)")
        sin_deriv.next_to(explanation, DOWN, buff=1)
        self.play(Write(sin_deriv))
        self.wait(1)
        cos_deriv = MathTex(r"\frac{d}{dx} \cos(x) = -\sin(x)")
        cos_deriv.next_to(sin_deriv, DOWN, buff=1)
        self.play(Write(cos_deriv))
        self.wait(1)
        tan_deriv = MathTex(r"\frac{d}{dx} \tan(x) = \sec^2(x)")
        tan_deriv.next_to(cos_deriv, DOWN, buff=1)
        self.play(Write(tan_deriv))
        self.wait(1)
        explanation2 = Text("Observați că derivata sinusului este cosinus, derivata cosinusului este minus sinus, iar derivata tangentei este secanta la pătrat.", color=WHITE)
        explanation2.next_to(tan_deriv, DOWN, buff=1)
        self.play(FadeIn(explanation2))
        self.wait(2)
        graph_explanation = Text("Aceste formule pot fi demonstrate geometric sau folosind definiția limitei derivatei.", color=WHITE)
        graph_explanation.next_to(explanation2, DOWN, buff=1)
        self.play(FadeIn(graph_explanation))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_deriv),
        FadeOut(cos_deriv),
        FadeOut(tan_deriv),
        FadeOut(explanation2),
        FadeOut(graph_explanation)
        )
