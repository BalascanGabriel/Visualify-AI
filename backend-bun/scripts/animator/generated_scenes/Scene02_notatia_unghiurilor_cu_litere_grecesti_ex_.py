from manim import *

class Scene02_notatia_unghiurilor_cu_litere_grecesti_ex_(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Notația unghiurilor cu litere grecești (ex: θ)", color=BLUE)
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
        "Unghiurile sunt adesea notate cu litere grecești pentru a le distinge de alte variabile.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• θ (theta) este frecvent utilizat.", font_size=32),
        Text("• α (alfa), β (beta), γ (gamma) sunt, de asemenea, comune.", font_size=32),
        Text("• Alegerea literei depinde de contextul problemei.", font_size=32)
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
        # Elemente vizuale
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        line1 = Line(ORIGIN, 2*RIGHT)
        line2 = Line(ORIGIN, 2*UP)
        line1.set_color(YELLOW)
        line2.set_color(YELLOW)
        angle = Angle(line1,line2,radius=0.7, color=RED)
        theta = MathTex(r"\theta").scale(1.5).next_to(angle, RIGHT)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(line1), Create(line2), Create(angle))
        self.play(Write(theta))
        self.wait(2)
        self.play(
        Transform(theta, MathTex(r"\alpha").scale(1.5).next_to(angle,RIGHT))
        )
        self.wait(1)
        self.play(
        Transform(theta, MathTex(r"\beta").scale(1.5).next_to(angle,RIGHT))
        )
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Literele grecești îmbunătățesc claritatea în ecuații.", color=GREEN_B, font_size=32),
        Text("✓ Utilizarea lor este o convenție matematică standard.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(angle),
        FadeOut(theta)
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