from manim import *

class Scene03_unghiuri_pozitive_rotatie_antiorara_si_negative_ro(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Unghiuri pozitive (rotație antiorară) și negative (rotație orar)", color=BLUE)
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
        "Un unghi este măsurat prin rotația unei semi-drepte în jurul unui punct.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Rotație antiorară = unghi pozitiv (+)", font_size=32),
        Text("• Rotație orar = unghi negativ (-)", font_size=32),
        Text("• Măsura unghiului se dă în grade sau radiani.", font_size=32)
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
        origin = Dot(color=YELLOW)
        line = Line(origin.get_center(), 2*RIGHT, color=GREEN)
        angle_arc_pos = Arc(radius=2, start_angle=0, angle=PI/2, color=RED)
        angle_arc_neg = Arc(radius=2, start_angle=0, angle=-PI/2, color=RED)
        angle_text_pos = MathTex(r"+90^\circ").next_to(angle_arc_pos.get_center(), RIGHT)
        angle_text_neg = MathTex(r"-90^\circ").next_to(angle_arc_neg.get_center(), LEFT)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(origin), Create(line))
        self.play(Create(angle_arc_pos), Write(angle_text_pos))
        self.wait(1)
        self.play(Transform(angle_arc_pos, angle_arc_neg), Transform(angle_text_pos, angle_text_neg))
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Unghiurile pozitive reprezintă rotații antiorare.", color=GREEN_B, font_size=32),
        Text("✓ Unghiurile negative reprezintă rotații orare.", color=GREEN_B, font_size=32),
        Text("✓ Semnul unghiului indică direcția de rotație.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(origin),
        FadeOut(line),
        FadeOut(angle_arc_neg),
        FadeOut(angle_text_neg)
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