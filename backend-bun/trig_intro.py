from manim import *

class TrigonometrieIntro(Scene):
    def clean_slate(self):
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

    def construct(self):
        # Titlu principal
        title = Text("Introducere în Trigonometrie", font_size=48)
        self.play(FadeIn(title))
        self.wait(1)
        self.clean_slate()

        # === Subcapitol 1 ===
        sc1 = Text("Cum se utilizează acest manual", font_size=36)
        sc1_desc = Text("➡ Practica și exercițiile sunt cheia înțelegerii!", font_size=28).next_to(sc1, DOWN)
        self.play(Write(sc1))
        self.play(FadeIn(sc1_desc))
        self.wait(2)
        self.clean_slate()

        # === Subcapitol 2: Conversie radiani/grade ===
        sc2 = Text("Conversia dintre radiani și grade", font_size=36)
        self.play(FadeIn(sc2.to_edge(UP)))

        circle = Circle(radius=2, color=BLUE)
        r1 = Line(ORIGIN, [2, 0, 0], color=WHITE)
        r2 = Line(ORIGIN, [2 * np.cos(PI/3), 2 * np.sin(PI/3), 0], color=WHITE)
        arc = Arc(radius=2, start_angle=0, angle=PI/3, color=GREEN)
        deg = MathTex("60^\\circ").next_to([2, 0, 0], DOWN)
        rad = MathTex("\\frac{\\pi}{3}~rad").next_to([2 * np.cos(PI/3), 2 * np.sin(PI/3), 0], UP)

        self.play(Create(circle), Create(r1), Create(r2), Create(arc))
        self.play(Write(deg), Write(rad))
        self.wait(2)
        self.clean_slate()

        # === Subcapitol 3: Graficul sinus ===
        sc3 = Text("Graficul funcției sinus", font_size=36)
        self.play(Write(sc3.to_edge(UP)))

        axes = Axes(
            x_range=[0, 2 * PI, PI / 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=3,
            axis_config={"color": WHITE},
        ).to_edge(DOWN)
        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        label = axes.get_graph_label(sin_graph, label="\\sin(x)")

        self.play(Create(axes), Create(sin_graph), Write(label))
        self.wait(2)
        self.clean_slate()

        # === Subcapitol 4: Derivarea sinusului ===
        sc4 = Text("Derivarea funcției sinus", font_size=36)
        formula = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)").scale(1.5)
        self.play(FadeIn(sc4.to_edge(UP)))
        self.play(Write(formula))
        self.wait(2)
        self.clean_slate()

        # === Subcapitol 5: Funcții inverse ===
        sc5 = Text("Funcțiile trigonometrice inverse", font_size=36)
        inv = MathTex(r"\arcsin(x),\quad \arccos(x),\quad \arctan(x)").scale(1.2)
        self.play(FadeIn(sc5.to_edge(UP)))
        self.play(Write(inv))
        self.wait(2)
        self.clean_slate()

        # === Final ===
        final = Text("Bravo! Ai parcurs conceptele-cheie din Introducere! 🎉", font_size=32, color=YELLOW)
        self.play(Write(final))
        self.wait(3)
