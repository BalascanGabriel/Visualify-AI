from manim import *

class Scene01_unghiul_ca_rotatie_intre_doua_linii_cu_un_punct_co(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Unghiul ca rotație între două linii cu un punct comun", color=BLUE)
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
        "Un unghi poate fi definit ca rotația unei linii în jurul unui punct fix până când atinge o a doua linie care trece prin același punct.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• Punctul comun este vârful unghiului.", font_size=32),
        Text("• Măsura unghiului reprezintă amplitudinea rotației.", font_size=32),
        Text("• Sensul de rotație (orar/antiorar) poate fi specificat.", font_size=32)
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
        origin = Dot(color=YELLOW)
        line1 = Line(start=ORIGIN, end=2*RIGHT, color=RED)
        line2 = Line(start=ORIGIN, end=2*UP, color=GREEN)
        arc = Arc(radius=1, start_angle=0, angle=PI/2, color=YELLOW)
        self.play(Write(demo_title), Create(origin), Create(line1))
        self.wait(0.5)
        self.play(Create(line2))
        self.wait(0.5)
        self.play(Create(arc))
        self.wait(1)
        #Animație rotație
        rotated_line = line1.copy()
        self.play(Rotate(rotated_line,PI/2, about_point=ORIGIN))
        self.wait(1)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie și puncte cheie",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Unghiul reprezintă o rotație definită de două linii.", color=GREEN_B, font_size=32),
        Text("✓ Măsura unghiului indică amplitudinea rotației.", color=GREEN_B, font_size=32),
        Text("✓ Punctul comun este esențial pentru definirea unghiului.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(line1),
        FadeOut(line2),
        FadeOut(arc),
        FadeOut(rotated_line),
        FadeOut(origin)
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