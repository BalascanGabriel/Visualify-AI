from manim import *

class Scene11_unghi_complet_2_radiani(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Unghi complet: 2π radiani", color=BLUE)
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
        "Un unghi complet reprezintă o rotație completă în jurul unui punct.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• O rotație completă corespunde la 360°.", font_size=32),
        Text("• În radiani, aceasta este echivalentă cu 2π.", font_size=32),
        Text("• 2π reprezintă circumferința unui cerc cu raza 1.", font_size=32)
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
        demo_title = Text("Demonstrație", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        arc = Arc(radius=2, start_angle=0, angle=TAU, color=YELLOW)
        arc.shift(DOWN)
        formula = MathTex(r"2\pi \text{ radiani} = 360^\circ")
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle))
        self.play(Create(arc))
        self.play(Write(formula))
        self.wait(2)
        #Adăugăm o săgeată care se rotește
        arrow = Arrow(ORIGIN,2*RIGHT, buff=0)
        arrow.shift(DOWN)
        self.play(Rotate(arrow, TAU, about_point=circle.get_center()), run_time=3)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Un unghi complet reprezintă o rotație de 360° sau 2π radiani.", color=GREEN_B, font_size=32),
        Text("✓ 2π radiani corespund la circumferința unui cerc cu raza 1.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(formula),
        FadeOut(arc),
        FadeOut(arrow)
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