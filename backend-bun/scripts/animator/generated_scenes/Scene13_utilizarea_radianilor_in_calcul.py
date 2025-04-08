from manim import *

class Scene13_utilizarea_radianilor_in_calcul(Scene):
    def construct(self):
        def construct(self):
        # Scena 1: Introducere
        title = Text("Utilizarea Radianilor în Calcul", color=BLUE)
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
        "Radianii simplifică calculul derivatelor și integralelor funcțiilor trigonometrice.",
        font_size=36,
        color=WHITE
        ).next_to(title, DOWN, buff=1.5)
        bullet_points = VGroup(
        Text("• **Derivate mai simple:**  Derivatele funcțiilor trigonometrice (sin x, cos x, etc.) sunt mult mai simple când unghiul este exprimat în radiani.", font_size=30),
        Text("• **Relații naturale:** Radianii reflectă relația naturală dintre lungimea arcului și raza cercului.  1 radian = lungimea arcului egală cu raza.", font_size=30),
        Text("• **Formula lui Taylor:** Expansiunile în serie Taylor pentru funcțiile trigonometrice sunt mult mai elegante și ușor de utilizat cu radiani.", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
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
        demo_title = Text("Demonstrație: Derivarea lui sin(x)", color=BLUE_C)
        demo_title.next_to(title, DOWN, buff=1.5)
        circle = Circle(radius=2, color=BLUE)
        circle.shift(DOWN)
        arc = Arc(radius=2, start_angle=0, angle=PI/2, color=YELLOW)
        arc.set_stroke(width=5)
        text_arc = MathTex(r"\frac{\pi}{2}").next_to(arc, UP, buff=0.5)
        formula1 = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)").scale(1.2).to_edge(LEFT, buff=1)
        formula2 = MathTex(r"\text{ (în radiani)}").scale(0.7).next_to(formula1, DOWN)
        formula_group = VGroup(formula1, formula2)
        self.play(Write(demo_title))
        self.play(Create(circle), Create(arc), Write(text_arc))
        self.play(Write(formula_group))
        self.wait(2)
        # Scena 4: Concluzie
        conclusion = Text(
        "Concluzie: Radianii sunt esențiali",
        color=GREEN,
        font_size=36
        ).next_to(title, DOWN, buff=1.5)
        final_points = VGroup(
        Text("✓ Simplifică calculele în analiză matematică.", color=GREEN_B, font_size=32),
        Text("✓ Fac formulele mai elegante și ușor de înțeles.", color=GREEN_B, font_size=32),
        Text("✓ Reprezintă o relație naturală geometrică.", color=GREEN_B, font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        final_points.next_to(conclusion, DOWN, buff=1)
        self.play(
        FadeOut(demo_title),
        FadeOut(circle),
        FadeOut(arc),
        FadeOut(text_arc),
        FadeOut(formula_group)
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