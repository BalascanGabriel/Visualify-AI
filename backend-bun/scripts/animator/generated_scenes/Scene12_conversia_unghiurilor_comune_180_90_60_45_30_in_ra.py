from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene12_conversia_unghiurilor_comune_180_90_60_45_30_in_ra(Scene):
    def construct(self):
        title = Text("Conversia unghiurilor comune: 180°, 90°, 60°, 45°, 30° în radiani", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Pentru a converti grade în radiani, folosim formula: Radiani = Grade * (π / 180°)", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        formulas = VGroup(
        MathTex(r"180^\circ = 180^\circ \times \frac{\pi}{180^\circ} = \pi \text{ radiani}"),
        MathTex(r"90^\circ = 90^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{2} \text{ radiani}"),
        MathTex(r"60^\circ = 60^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{3} \text{ radiani}"),
        MathTex(r"45^\circ = 45^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{4} \text{ radiani}"),
        MathTex(r"30^\circ = 30^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{6} \text{ radiani}"),
        )
        formulas.arrange(DOWN, buff=0.5).next_to(explanation, DOWN, buff=1)
        self.play(Write(formulas[0]))
        self.wait(1)
        self.play(Write(formulas[1]))
        self.wait(1)
        self.play(Write(formulas[2]))
        self.wait(1)
        self.play(Write(formulas[3]))
        self.wait(1)
        self.play(Write(formulas[4]))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formulas)
        )
