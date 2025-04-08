from manim import *

class Scene16_asociaza_fiecare_numar_real_unui_punct_pe_cercul_u(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Asociază fiecare număr real unui punct pe cercul unitate", color=BLUE)
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
        "Fiecare număr real t corespunde unui punct pe cercul unitate.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• t reprezintă lungimea arcului de la punctul (1,0) în sens trigonometric pozitiv.", font_size=32),
        Text("• Dacă t este pozitiv, ne mișcăm în sens trigonometric pozitiv.", font_size=32),
        Text("• Dacă t este negativ, ne mișcăm în sens trigonometric negativ.", font_size=32),
        Text("•  2π reprezintă o rotație completă, deci t și t + 2kπ (k∈ℤ) corespund aceluiași punct.", font_size=32)
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
        circle = Circle(radius=1, color=BLUE)
        circle.shift(DOWN)
        dot = Dot(color=YELLOW).move_to(RIGHT)
        t_value = ValueTracker(0)
        angle = always_redraw(lambda: t_value.get_value() % (2*PI))
        point = always_redraw(lambda: circle.point_at_angle(angle))
        arc = always_redraw(lambda: Arc(radius=1, start_angle=0, angle=angle, color=YELLOW))
        self.play(Write(demo_title))
        self.play(Create(circle), Create(dot))
        self.play(Create(arc))
        self.play(t_value.animate.set_value(2*PI), run_time=3)
        self.play(t_value.animate.set_value(2*PI + PI/2), run_time=2)
        self.play(t_value.animate.set_value(2*PI + PI/2 - PI), run_time=2)
        self.play(t_value.animate.set_value(0), run_time=2)
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Funcția este periodică cu perioada 2π.", color=GREEN_B, font_size=32),
        Text("✓ Fiecare punct de pe cercul unitate corespunde unui număr infinit de valori reale.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(dot),
        FadeOut(arc)
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