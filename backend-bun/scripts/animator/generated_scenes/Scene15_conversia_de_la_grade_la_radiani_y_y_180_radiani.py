from manim import *

class Scene15_conversia_de_la_grade_la_radiani_y_y_180_radiani(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Conversia de la grade la radiani: y° = y * (π/180) radiani", color=BLUE)
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
        "Un cerc complet are 360° și 2π radiani.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Radianul este o unitate de măsură a unghiurilor bazată pe lungimea arcului de cerc.", font_size=32),
        Text("• Un radian este unghiul subîntins de un arc cu lungimea egală cu raza cercului.", font_size=32),
        Text("• Pentru a converti din grade în radiani, folosim raportul:  (π radiani / 180°).", font_size=32)
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
        demo_title = Text("Demonstrație: Conversia a 90° în radiani", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=YELLOW)
        arc.add_updater(lambda a: a.become(Arc(radius=2, start_angle=0, angle=self.get_angle(), color=YELLOW)))
        formula = MathTex(r"90^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{2} \text{ radiani}")
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(arc))
        self.play(Write(formula))
        self.wait(1)
        self.add(ValueTracker(0))
        self.play(self.get_angle().animate.set_value(PI/2), run_time=2)
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Conversia este simplă!",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Înmulțiți numărul de grade cu π/180.", color=GREEN_B, font_size=32),
        Text("✓ Rezultatul este unghiul în radiani.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
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
        def get_angle(self):
        return self.mobjects[1].get_value()