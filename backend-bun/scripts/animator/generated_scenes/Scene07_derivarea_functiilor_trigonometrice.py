from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene07_derivarea_functiilor_trigonometrice(Scene):
    def construct(self):
        title = Text("Derivarea funcțiilor trigonometrice", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Vom demonstra derivatele funcțiilor sinus și cosinus.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        sin_derivation = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)")
        sin_derivation.next_to(explanation, DOWN, buff=1)
        self.play(Write(sin_derivation))
        cos_derivation = MathTex(r"\frac{d}{dx} \cos(x) = -\sin(x)")
        cos_derivation.next_to(sin_derivation, DOWN, buff=1)
        self.play(Write(cos_derivation))
        explanation2 = Text("Demonstrația utilizează definiția derivatei și limite.", color=WHITE)
        explanation2.next_to(cos_derivation, DOWN, buff=1)
        self.play(Write(explanation2))
        limit_definition = MathTex(r"\frac{d}{dx}f(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")
        limit_definition.next_to(explanation2, DOWN, buff=1)
        self.play(Write(limit_definition))
        sin_limit = MathTex(r"\lim_{h \to 0} \frac{\sin(x+h) - \sin(x)}{h}")
        sin_limit.next_to(limit_definition, DOWN, buff=1)
        self.play(Write(sin_limit))
        sin_identity = MathTex(r"\sin(x+h) = \sin(x)\cos(h) + \cos(x)\sin(h)")
        sin_identity.next_to(sin_limit, DOWN, buff=1)
        self.play(Write(sin_identity))
        simplified_limit = MathTex(r"\lim_{h \to 0} \frac{\sin(x)\cos(h) + \cos(x)\sin(h) - \sin(x)}{h}")
        simplified_limit.next_to(sin_identity, DOWN, buff=1)
        self.play(Write(simplified_limit))
        final_step = MathTex(r"= \cos(x) \lim_{h \to 0} \frac{\sin(h)}{h} + \sin(x) \lim_{h \to 0} \frac{\cos(h)-1}{h} = \cos(x)")
        final_step.next_to(simplified_limit, DOWN, buff=1)
        self.play(Write(final_step))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(sin_derivation),
        FadeOut(cos_derivation),
        FadeOut(limit_definition),
        FadeOut(sin_limit),
        FadeOut(sin_identity),
        FadeOut(simplified_limit),
        FadeOut(final_step)
        )
