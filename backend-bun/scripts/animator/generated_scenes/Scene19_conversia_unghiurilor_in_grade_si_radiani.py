from manim import *

class Scene19_conversia_unghiurilor_in_grade_si_radiani(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Conversia unghiurilor în grade și radiani", color=BLUE)
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
        "Un cerc complet are 360 de grade (360°) sau 2π radiani.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• 180° = π radiani", font_size=32),
        Text("• Pentru a converti grade în radiani:  x (grade) * π / 180", font_size=32),
        Text("• Pentru a converti radiani în grade: x (radiani) * 180 / π", font_size=32)
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
        angle_degrees = Angle(circle.get_arc(start_angle=0, angle=PI/2, radius=1.5), radius=0.5, other_angle=False)
        angle_radians = Angle(circle.get_arc(start_angle=0, angle=PI/2, radius=1.5), radius=0.5, other_angle=False)
        degrees_text = Tex("90°").next_to(angle_degrees, RIGHT, buff=0.5)
        radians_text = Tex(r"$\frac{\pi}{2}$ rad").next_to(angle_radians, RIGHT, buff=0.5)
        radians_text.shift(RIGHT)
        self.play(Write(demo_title), Create(circle))
        self.play(Create(angle_degrees), Write(degrees_text))
        self.wait(1)
        self.play(Transform(degrees_text, radians_text), Transform(angle_degrees, angle_radians))
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Conversia între grade și radiani este esențială în trigonometrie și alte domenii ale matematicii.",
        color=GREEN,
        font_size=32
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Folosiți formulele de conversie pentru a trece ușor între unități.", color=GREEN_B, font_size=30),
        Text("✓ Înțelegerea relației dintre grade și radiani este crucială pentru rezolvarea problemelor.", color=GREEN_B, font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(degrees_text)
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