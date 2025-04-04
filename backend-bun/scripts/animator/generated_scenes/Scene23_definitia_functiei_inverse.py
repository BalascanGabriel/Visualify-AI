from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene23_definitia_functiei_inverse(Scene):
    def construct(self):
        title = Text("Definiția funcției inverse", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Fie f: A → B o funcție bijectivă (injectivă și surjectivă).  Funcția inversă f⁻¹: B → A este definită astfel încât pentru orice x ∈ A, f⁻¹(f(x)) = x și pentru orice y ∈ B, f(f⁻¹(y)) = y.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formula1 = MathTex(r"f: A \to B", r"\quad", r"f^{-1}: B \to A")
        formula1.next_to(explanation, DOWN, buff=1)
        self.play(Write(formula1))
        formula2 = MathTex(r"f(x) = y", r"\implies", r"f^{-1}(y) = x")
        formula2.next_to(formula1, DOWN, buff=0.5)
        self.play(Write(formula2))
        example_text = Text("Exemplu: f(x) = 2x + 1", color=WHITE)
        example_text.next_to(formula2, DOWN, buff=1)
        self.play(Write(example_text))
        example_inverse_text = Text("Funcția inversă este f⁻¹(x) = (x - 1)/2", color=WHITE)
        example_inverse_text.next_to(example_text, DOWN, buff=0.5)
        self.play(Write(example_inverse_text))
        verification = MathTex(r"f(f^{-1}(x)) = 2\left(\frac{x-1}{2}\right) + 1 = x", r"\quad", r"f^{-1}(f(x)) = \frac{(2x+1)-1}{2} = x")
        verification.next_to(example_inverse_text, DOWN, buff=1)
        self.play(Write(verification))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(example_text),
        FadeOut(example_inverse_text),
        FadeOut(verification)
        )
