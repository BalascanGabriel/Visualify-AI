from manim import *

class Scene05_cercul_impartit_in_360_de_grade(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Cercul împărțit în 360 de grade", color=BLUE)
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
        "Un cerc complet reprezintă o rotație de 360 de grade.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Gradul este o unitate de măsură a unghiului.", font_size=32),
        Text("• 360 de grade corespund la o rotație completă.", font_size=32),
        Text("• Această împărțire este arbitrară, dar convenabilă.", font_size=32)
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
        arc = Arc(radius=2, start_angle=0, angle=360*DEGREES, color=YELLOW)
        arc.shift(DOWN)
        #Adăugăm marcaje pentru grade (simplificat)
        for i in range(0, 361, 45):
        line = Line(circle.point_at_angle(i*DEGREES), circle.point_at_angle(i*DEGREES) + 0.2*RIGHT)
        self.add(line)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(arc))
        self.wait(1)
        #Animatie de rotire (optional - necesita timp de renderizare mai mare)
        #self.play(Rotate(arc, 360*DEGREES, about_point=ORIGIN, run_time=3))
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: 360 de grade definesc un cerc complet.",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Conceptul este fundamental în geometrie și trigonometrie.", color=GREEN_B, font_size=32),
        Text("✓ Este utilizat în multe domenii, de la cartografie la programare.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(arc) #Stergem si arcul
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