from manim import *

class Scene12_relatia_intre_grade_si_radiani_2_radiani_360_(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Relația între grade și radiani: 2π radiani = 360°", color=BLUE)
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
        "Un cerc complet are 360 de grade.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Circumferința cercului este 2πr, unde r este raza.", font_size=32),
        Text("• Un radian este unghiul subtins de un arc cu lungimea egală cu raza.", font_size=32),
        Text("• Astfel, un cerc complet reprezintă 2π radiani.", font_size=32)
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
        formula = MathTex(r"2\pi \text{ radiani} = 360^\circ").scale(1.2)
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle))
        self.play(Create(arc))
        self.play(Write(formula))
        self.wait(2)
        #Animație rotirea cercului
        self.play(Rotate(arc, TAU, about_point=circle.get_center()), run_time=3)
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Relația fundamentală",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ 1 radian ≈ 57.3°", color=GREEN_B, font_size=32),
        Text("✓ Pentru conversie:  grade = radiani * (180/π)", color=GREEN_B, font_size=32),
        Text("✓ Pentru conversie:  radiani = grade * (π/180)", color=GREEN_B, font_size=32)
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