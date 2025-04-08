from manim import *

class Scene17_numere_reale_cu_diferenta_de_2_k_k_corespund_acelu(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Numere reale cu diferență de 2πk (k∈ℤ) corespund aceluiași punct", color=BLUE)
        title.scale(1.2).to_edge(UP, buff=1.5)
        subtitle = Text("Să înțelegem conceptul pas cu pas", color=BLUE_B)
        subtitle.next_to(title, DOWN, buff=0.8)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait()
        self.play(FadeOut(subtitle))
        # Scena 2: Explicație principală
        explanation = Text(
        "Funcțiile trigonometrice (sinus și cosinus) sunt periodice cu perioada 2π.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("•  sin(x + 2πk) = sin(x)", font_size=32),
        Text("•  cos(x + 2πk) = cos(x)", font_size=32),
        Text("•  k este un număr întreg (k ∈ ℤ)", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        bullet_points.next_to(explanation, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait()
        for point in bullet_points:
        self.play(Write(point))
        self.wait(0.5)
        self.wait()
        # Curățăm pentru următoarea scenă
        self.play(
        FadeOut(explanation),
        FadeOut(bullet_points)
        )
        # Scena 3: Demonstrație vizuală
        demo_title = Text("Demonstrație pe cerc trigonometric", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        # Adăugăm un punct pe cerc
        dot = Dot(radius=0.1, color=RED)
        dot.move_to(circle.point(0))
        # Adăugăm o linie de la origine la punct
        line = Line(ORIGIN, dot.get_center(), color=YELLOW)
        # Adăugăm un arc de cerc
        arc = Arc(radius=2, start_angle=0, angle=PI, color=GREEN)
        arc.shift(DOWN)
        formula = MathTex(r"x \equiv x + 2\pi k \pmod{2\pi}", font_size=36)
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(dot), Create(line))
        self.play(Write(formula))
        self.wait(1)
        self.play(Create(arc))
        self.wait(1)
        # Animatie miscare punct
        self.play(Rotate(dot, 2*PI, about_point=ORIGIN, rate_func=linear))
        self.play(Rotate(line, 2*PI, about_point=ORIGIN, rate_func=linear))
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Pe cercul trigonometric, unghiurile care diferă cu multipli de 2π corespund aceluiași punct.",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Aceasta este o consecință directă a periodicității funcțiilor trigonometrice.", color=GREEN_B, font_size=32),
        Text("✓ Conceptul este esențial în multe domenii, precum analiza Fourier și  electrotehnica.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(dot),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(formula)
        )
        self.play(Write(conclusion))
        self.play(Write(final_points))
        self.wait(2)
        # Final
        self.play(
        FadeOut(title),
        FadeOut(conclusion),
        FadeOut(final_points)
        )
        self.wait()