from manim import *

class Scene10_radianul_ca_lungime_a_arcului_pe_cercul_unitate(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Radianul ca lungime a arcului pe cercul unitate", color=BLUE)
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
        "Un radian este unghiul central care interceptează un arc cu lungimea egală cu raza cercului.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Cercul unitate are raza 1.", font_size=32),
        Text("• Un radian corespunde unui arc de lungime 1.", font_size=32),
        Text("• 2π radiani reprezintă o rotație completă (360°).", font_size=32)
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
        arc = Arc(radius=1, start_angle=0, angle=1, color=YELLOW)
        arc.shift(DOWN)
        radius1 = Line(ORIGIN, RIGHT, color=RED)
        radius1.shift(DOWN)
        radius2 = Line(RIGHT, RIGHT + UP, color=RED)
        radius2.shift(DOWN)
        radius2.rotate(1, about_point=ORIGIN)
        angle_label = Tex("1 radian").next_to(arc, RIGHT)
        self.play(Write(demo_title))
        self.play(Create(circle))
        self.play(Create(radius1))
        self.play(Create(arc), Create(radius2), Write(angle_label))
        self.wait(1)
        self.play(
        arc.animate.set_angle(TAU/4),
        radius2.animate.rotate(TAU/4-1, about_point=ORIGIN)
        )
        self.play(Transform(angle_label, Tex(r"$\frac{\pi}{2}$ radiani").next_to(arc, RIGHT)))
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Radianul simplifică calculele trigonometrice.", color=GREEN_B, font_size=32),
        Text("✓ Legătura directă între unghi și lungimea arcului.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(radius1),
        FadeOut(radius2),
        FadeOut(angle_label)
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