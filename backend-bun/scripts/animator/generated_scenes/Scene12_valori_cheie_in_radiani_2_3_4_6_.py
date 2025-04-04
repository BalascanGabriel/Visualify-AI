from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene12_valori_cheie_in_radiani_2_3_4_6_(Scene):
    def construct(self):
        title = Text("Valori cheie în radiani (π/2, π/3, π/4, π/6)", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Aceste valori sunt importante în trigonometrie deoarece apar frecvent în probleme și au valori simple pentru funcțiile trigonometrice.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(FadeIn(explanation))
        formula1 = MathTex(r"\frac{\pi}{6} \approx 30^\circ")
        formula2 = MathTex(r"\frac{\pi}{4} \approx 45^\circ")
        formula3 = MathTex(r"\frac{\pi}{3} \approx 60^\circ")
        formula4 = MathTex(r"\frac{\pi}{2} \approx 90^\circ")
        formula1.next_to(explanation, DOWN, buff=1)
        formula2.next_to(formula1, DOWN, buff=0.5)
        formula3.next_to(formula2, DOWN, buff=0.5)
        formula4.next_to(formula3, DOWN, buff=0.5)
        self.play(Write(formula1))
        self.play(Write(formula2))
        self.play(Write(formula3))
        self.play(Write(formula4))
        table = MathTex(r"""
        \begin{array}{|c|c|c|c|}
        \hline
        \theta & \sin(\theta) & \cos(\theta) & \tan(\theta) \\
        \hline
        \frac{\pi}{6} & \frac{1}{2} & \frac{\sqrt{3}}{2} & \frac{\sqrt{3}}{3} \\
        \hline
        \frac{\pi}{4} & \frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 1 \\
        \hline
        \frac{\pi}{3} & \frac{\sqrt{3}}{2} & \frac{1}{2} & \sqrt{3} \\
        \hline
        \frac{\pi}{2} & 1 & 0 & \infty \\
        \hline
        \end{array}
        """)
        table.next_to(formula4, DOWN, buff=1)
        self.play(Write(table))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(formula1),
        FadeOut(formula2),
        FadeOut(formula3),
        FadeOut(formula4),
        FadeOut(table)
        )
