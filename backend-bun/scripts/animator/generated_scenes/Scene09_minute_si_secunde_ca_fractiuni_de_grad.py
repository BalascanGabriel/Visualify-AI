from manim import *

class Scene09_minute_si_secunde_ca_fractiuni_de_grad(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Minute și secunde ca fracțiuni de grad", color=BLUE)
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
        "Un grad este împărțit în 60 de minute ('), iar un minut este împărțit în 60 de secunde (\").",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• 1 minut = 1/60 de grad", font_size=32),
        Text("• 1 secundă = 1/3600 de grad", font_size=32),
        Text("• Conversia se face prin împărțire la 60 (minute) sau 3600 (secunde).", font_size=32)
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
        arc = Arc(radius=2, start_angle=0, angle=30 * DEGREES, color=YELLOW)
        arc.add_updater(lambda a: a.become(Arc(radius=2, start_angle=0, angle=30 * DEGREES)))
        circle.add(arc)
        formula = MathTex(r"30^\circ 15' 30'' = 30 + \frac{15}{60} + \frac{30}{3600} \approx 30.26^\circ")
        formula.next_to(circle, DOWN, buff=1)
        self.play(Write(demo_title))
        self.play(Create(circle))
        self.wait(1)
        self.play(Write(formula))
        self.wait(2)
        # Adăugăm o animație de marcare a arcului
        brace = Brace(arc, direction=DOWN)
        brace_text = brace.get_text("30°")
        self.play(GrowFromCenter(brace), Write(brace_text))
        self.wait(1)
        self.play(FadeOut(brace), FadeOut(brace_text))
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Minutele și secundele reprezintă fracțiuni zecimale de grad.", color=GREEN_B, font_size=32),
        Text("✓ Conversia este esențială pentru precizie în măsurători unghiulare.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
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