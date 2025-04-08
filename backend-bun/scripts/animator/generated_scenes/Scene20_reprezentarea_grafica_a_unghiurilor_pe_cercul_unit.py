from manim import *

class Scene20_reprezentarea_grafica_a_unghiurilor_pe_cercul_unit(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Reprezentarea grafică a unghiurilor pe cercul unitate", color=BLUE)
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
        "Cercul unitate este un cerc cu raza 1 centrat în originea sistemului de coordonate.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Unghiul este măsurat în radiani, de la axa x pozitivă.", font_size=32),
        Text("• Coordonatele punctului de intersecție dintre unghi și cerc reprezintă cosinusul și sinusul unghiului.", font_size=32),
        Text("•  Aceasta oferă o reprezentare vizuală a funcțiilor trigonometrice.", font_size=32)
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
        circle.set_stroke(width=2)
        axes = Axes(
        x_range=[-1.5, 1.5, 1],
        y_range=[-1.5, 1.5, 1],
        x_length=3,
        y_length=3,
        )
        axes.set_color(GRAY)
        # Punctul mobil
        dot = Dot(color=YELLOW)
        dot.move_to(RIGHT)
        # Linie către origine
        line = Line(ORIGIN, RIGHT)
        line.set_color(GREEN)
        angle = Angle(line, RIGHT, radius=0.5, other_angle=False)
        angle.set_color(RED)
        self.play(Create(axes), Create(circle))
        self.play(Write(demo_title))
        self.play(Create(dot), Create(line), Create(angle))
        self.play(Rotate(line, PI/2, about_point=ORIGIN), Rotate(angle, PI/2, about_point=ORIGIN), run_time=2, rate_func=smooth)
        self.play(Rotate(line, PI/2, about_point=ORIGIN), Rotate(angle, PI/2, about_point=ORIGIN), run_time=2, rate_func=smooth)
        self.play(Rotate(line, PI/2, about_point=ORIGIN), Rotate(angle, PI/2, about_point=ORIGIN), run_time=2, rate_func=smooth)
        self.play(Rotate(line, PI/2, about_point=ORIGIN), Rotate(angle, PI/2, about_point=ORIGIN), run_time=2, rate_func=smooth)
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Cercul unitate oferă o vizualizare clară a funcțiilor trigonometrice.", color=GREEN_B, font_size=32),
        Text("✓  Unghiul și coordonatele punctului corespunzător definesc sinusul și cosinusul.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(line),
        FadeOut(angle),
        FadeOut(dot),
        FadeOut(circle),
        FadeOut(axes)
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