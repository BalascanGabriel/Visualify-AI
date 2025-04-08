from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene07_derivarea_functiilor_trigonometrice_(Scene):
    def construct(self):
        title = Text("Derivarea funcțiilor trigonometrice.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Vom deriva funcțiile sinus și cosinus folosind definiția limitei derivatei.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(1)
        formula_derivata = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")
        formula_derivata.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula_derivata))
        self.wait(2)
        formula_sinus = MathTex(r"\frac{d}{dx} \sin(x) = \lim_{h \to 0} \frac{\sin(x+h) - \sin(x)}{h}")
        formula_sinus.next_to(formula_derivata, DOWN, buff=1)
        self.play(Write(formula_sinus))
        self.wait(2)
        # Folosim identitatea trigonometrică pentru suma de unghiuri
        identitate_suma = MathTex(r"\sin(x+h) = \sin(x)\cos(h) + \cos(x)\sin(h)")
        identitate_suma.next_to(formula_sinus, DOWN, buff=1)
        self.play(Write(identitate_suma))
        self.wait(2)
        # Substituim în formula derivatei
        substitutie = MathTex(r"\lim_{h \to 0} \frac{\sin(x)\cos(h) + \cos(x)\sin(h) - \sin(x)}{h}")
        substitutie.next_to(identitate_suma, DOWN, buff=1)
        self.play(Write(substitutie))
        self.wait(2)
        # Simplificare
        simplificare = MathTex(r"\lim_{h \to 0} \left( \sin(x) \frac{\cos(h) - 1}{h} + \cos(x) \frac{\sin(h)}{h} \right)")
        simplificare.next_to(substitutie, DOWN, buff=1)
        self.play(Write(simplificare))
        self.wait(2)
        # Limite cunoscute
        limite = MathTex(r"\lim_{h \to 0} \frac{\cos(h) - 1}{h} = 0, \quad \lim_{h \to 0} \frac{\sin(h)}{h} = 1")
        limite.next_to(simplificare, DOWN, buff=1)
        self.play(Write(limite))
        self.wait(2)
        # Rezultat final pentru sinus
        rezultat_sinus = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)")
        rezultat_sinus.next_to(limite, DOWN, buff=1)
        self.play(Write(rezultat_sinus))
        self.wait(3)
        # Analog pentru cosinus (fara detalii complete)
        explanation_cosinus = Text("Similar, pentru cosinus se obține:", color=WHITE)
        explanation_cosinus.next_to(rezultat_sinus, DOWN, buff=1)
        self.play(Write(explanation_cosinus))
        rezultat_cosinus = MathTex(r"\frac{d}{dx} \cos(x) = -\sin(x)")
        rezultat_cosinus.next_to(explanation_cosinus, DOWN, buff=1)
        self.play(Write(rezultat_cosinus))
        self.wait(3)
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
