from manim import *

class Scene08_unghi_intins_180_(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Unghi întins: 180°", color=BLUE)
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
        "Un unghi întins este un unghi format din două raze opuse care formează o linie dreaptă.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Măsoară exact 180 de grade.", font_size=32),
        Text("• Razele sunt coliniare (se află pe aceeași linie).", font_size=32),
        Text("• Este un unghi plat.", font_size=32)
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
        line = Line([-4,0,0],[4,0,0], stroke_width=6, color=YELLOW)
        arc = Arc(radius=2, start_angle=0, angle=PI, color=RED)
        arc_label = MathTex(r"180^\circ").next_to(arc.get_center(), UP)
        self.play(Write(demo_title))
        self.play(Create(line))
        self.play(Create(arc), Write(arc_label))
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Un unghi de 180° formează o linie dreaptă.", color=GREEN_B, font_size=32),
        Text("✓ Este esențial în geometria plană.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(line),
        FadeOut(arc),
        FadeOut(arc_label)
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