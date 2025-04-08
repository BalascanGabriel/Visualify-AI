from manim import *

class Scene18_reprezentarea_unghiurilor_pozitive_si_negative_pe_(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Reprezentarea unghiurilor pozitive și negative pe cercul unitate", color=BLUE)
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
        "Unghiurile pozitive sunt măsurate în sens antiorar, începând de la axa x pozitivă.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        explanation2 = Text(
        "Unghiurile negative sunt măsurate în sens orar, începând de la axa x pozitivă.",
        font_size=36,
        color=WHITE
        ).next_to(explanation, DOWN, buff=1)
        bullet_points = VGroup(
        Text("• Un unghi de 90° este reprezentat pe axa y pozitivă.", font_size=32),
        Text("• Un unghi de -90° este reprezentat pe axa y negativă.", font_size=32),
        Text("• Unghiurile de 0° și 360° coincid cu axa x pozitivă.", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        bullet_points.next_to(explanation2, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(1)
        self.play(Write(explanation2))
        self.wait(1)
        for point in bullet_points:
        self.play(Write(point))
        self.wait(0.5)
        self.wait()
        # Curățăm pentru următoarea scenă
        self.play(
        FadeOut(explanation),
        FadeOut(explanation2),
        FadeOut(bullet_points)
        )
        # Scena 3: Demonstrație vizuală
        demo_title = Text("Demonstrație", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        axes = Axes(x_range=(-2.5, 2.5, 1), y_range=(-2.5, 2.5, 1), axis_config={"include_numbers": True})
        axes.shift(DOWN)
        dot = Dot(color=RED)
        dot.move_to(circle.get_center() + RIGHT*2)
        line = Line(ORIGIN, dot.get_center())
        line.set_color(YELLOW)
        angle_arc = Arc(radius=0.5, start_angle=0, angle=PI/2, color=GREEN)
        angle_arc.next_to(ORIGIN, RIGHT)
        angle_arc_neg = Arc(radius=0.5, start_angle=0, angle=-PI/2, color=PURPLE)
        angle_arc_neg.next_to(ORIGIN, RIGHT)
        angle_text_pos = MathTex(r"+90^\circ").next_to(angle_arc, RIGHT, buff=0.2)
        angle_text_neg = MathTex(r"-90^\circ").next_to(angle_arc_neg, RIGHT, buff=0.2)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(axes))
        self.play(Create(line), Create(dot))
        self.play(Create(angle_arc), Write(angle_text_pos))
        self.wait(1)
        self.play(Transform(angle_arc, angle_arc_neg), Transform(angle_text_pos, angle_text_neg))
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Unghiurile pozitive și negative definesc direcția de rotație pe cercul unitate.", color=GREEN_B, font_size=32),
        Text("✓ Reprezentarea pe cercul unitate permite vizualizarea trigonometrică a unghiurilor.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(line),
        FadeOut(dot),
        FadeOut(angle_arc),
        FadeOut(angle_text_neg),
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