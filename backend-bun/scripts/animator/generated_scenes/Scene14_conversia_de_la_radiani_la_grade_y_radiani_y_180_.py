from manim import *

class Scene14_conversia_de_la_radiani_la_grade_y_radiani_y_180_(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Conversia de la radiani la grade: y rad = y * (180/π)°", color=BLUE)
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
        "Un radian este unghiul sub care un arc de cerc are lungimea egală cu raza cercului.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Circumferința cercului este 2πr.", font_size=32),
        Text("• Unghiul complet (360°) corespunde la 2π radiani.", font_size=32),
        Text("• Deci, 1 radian ≈ 57.3° (180°/π).", font_size=32)
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
        demo_title = Text("Demonstrație: Conversia lui π/2 radiani", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=YELLOW)
        arc.shift(DOWN)
        formula = MathTex(r"\frac{\pi}{2} \text{ rad} = \frac{\pi}{2} \times \frac{180^\circ}{\pi} = 90^\circ")
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle),Create(arc))
        self.play(Write(formula))
        self.wait(2)
        #Scena 3.1:  Evidentiere  π/2
        brace = Brace(arc, RIGHT)
        brace_text = brace.get_text(r"$\frac{\pi}{2}$ radiani")
        self.play(GrowFromCenter(brace), Write(brace_text))
        self.wait(1)
        self.play(FadeOut(brace), FadeOut(brace_text))
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Formula de conversie este esențială pentru trecerea între sistemele de măsurare a unghiurilor.",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓  Folosiți formula pentru orice valoare în radiani.", color=GREEN_B, font_size=32),
        Text("✓  Asigurați-vă că calculați corect folosind valoarea lui π.", color=GREEN_B, font_size=32)
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