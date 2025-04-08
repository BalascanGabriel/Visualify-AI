from manim import *

class Scene04_unitati_de_masura_grade_si_radiani(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Unități de măsură: Grade și Radiani", color=BLUE)
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
        "Gradele și radianii sunt unități de măsură pentru unghiuri.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Grade: Un cerc complet are 360 de grade.", font_size=32),
        Text("• Radiani: Un radian este unghiul subtins de un arc de cerc cu lungimea egală cu raza cercului.", font_size=32),
        Text("• Relația: 2π radiani = 360 grade (1 radian ≈ 57.3 grade)", font_size=32)
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
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=YELLOW)
        arc.add_updater(lambda a: a.become(Arc(radius=2, start_angle=0, angle=self.time*PI/2, color=YELLOW)))
        radius_line = Line(circle.get_center(), circle.get_right())
        radius_line2 = Line(circle.get_center(), circle.point_at_angle(PI/2))
        formula = MathTex(r"1 \text{ radian} = \frac{\text{lungimea arcului}}{\text{raza}}")
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(radius_line), Create(radius_line2))
        self.play(Create(arc))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        degree_label = Text("90°", color=YELLOW)
        degree_label.next_to(arc, RIGHT)
        radian_label = Text(r"$\frac{\pi}{2}$ rad", color=YELLOW)
        radian_label.next_to(arc, UP)
        self.play(Write(degree_label))
        self.play(Write(radian_label))
        self.wait(2)
        self.play(Uncreate(arc), FadeOut(radius_line), FadeOut(radius_line2)) # curatam arcul animat
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Gradele și radianii descriu unghiuri.", color=GREEN_B, font_size=32),
        Text("✓ Radianii sunt mai convenabili în matematică și fizică.", color=GREEN_B, font_size=32),
        Text("✓  Înțelegerea conversiei între grade și radiani este esențială.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(formula),
        FadeOut(degree_label),
        FadeOut(radian_label)
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