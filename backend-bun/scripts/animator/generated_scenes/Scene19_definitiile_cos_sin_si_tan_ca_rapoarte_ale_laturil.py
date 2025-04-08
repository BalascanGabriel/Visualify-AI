from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene19_definitiile_cos_sin_si_tan_ca_rapoarte_ale_laturil(Scene):
    def construct(self):
        title = Text("Definițiile cosθ, sinθ și tanθ ca rapoarte ale laturilor unui triunghi dreptunghic.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Considerăm un triunghi dreptunghic cu unghiul θ.", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        triangle = Polygon([0,0,0], [4,0,0], [4,3,0], color=YELLOW)
        self.play(Create(triangle))
        #Adăugăm etichetele la vârfuri
        A = Dot([0,0,0])
        B = Dot([4,0,0])
        C = Dot([4,3,0])
        self.play(Create(A), Create(B), Create(C))
        label_A = Text("A", color=WHITE).next_to(A, UP)
        label_B = Text("B", color=WHITE).next_to(B, DOWN)
        label_C = Text("C", color=WHITE).next_to(C, RIGHT)
        self.play(Write(label_A), Write(label_B), Write(label_C))
        #Adăugăm etichetele laturilor
        a = MathTex(r"a", color=WHITE).move_to(triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2
        b = MathTex(r"b", color=WHITE).next_to(triangle.get_center() , LEFT, buff = 0.5)
        c = MathTex(r"c", color=WHITE).move_to(triangle.get_vertices()[0] + triangle.get_vertices()[2]) / 2
        self.play(Write(a), Write(b), Write(c))
        #Formulele
        sin_formula = MathTex(r"\sin(\theta) = \frac{a}{c} = \frac{\text{latura opusă}}{\text{ipotenuză}}")
        cos_formula = MathTex(r"\cos(\theta) = \frac{b}{c} = \frac{\text{latura adiacentă}}{\text{ipotenuză}}")
        tan_formula = MathTex(r"\tan(\theta) = \frac{a}{b} = \frac{\text{latura opusă}}{\text{latura adiacentă}}")
        sin_formula.next_to(explanation, DOWN, buff=1)
        cos_formula.next_to(sin_formula, DOWN, buff=0.5)
        tan_formula.next_to(cos_formula, DOWN, buff=0.5)
        self.play(Write(sin_formula))
        self.play(Write(cos_formula))
        self.play(Write(tan_formula))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(sin_formula),
        FadeOut(cos_formula),
        FadeOut(tan_formula),
        FadeOut(triangle),
        FadeOut(A),
        FadeOut(B),
        FadeOut(C),
        FadeOut(label_A),
        FadeOut(label_B),
        FadeOut(label_C),
        FadeOut(a),
        FadeOut(b),
        FadeOut(c)
        )
