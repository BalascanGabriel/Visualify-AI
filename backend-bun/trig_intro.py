from manim import *

class TrigonometrieIntro(Scene):
    def construct(self):
        # Titlu general
        title = Title("Introducere în Trigonometrie", include_underline=True)
        self.play(Write(title))
        self.wait(1)

        # Subcapitol: Cum se utilizează acest manual
        sub1 = Text("Cum se utilizează acest manual", font_size=36).next_to(title, DOWN)
        concept1 = Text("→ Practica și exercițiile sunt cheia înțelegerii!", font_size=28).next_to(sub1, DOWN)
        self.play(Write(sub1))
        self.play(FadeIn(concept1, shift=RIGHT))
        self.wait(2)
        self.play(FadeOut(sub1), FadeOut(concept1))

        # Subcapitol: Obiectivele
        sub2 = Text("Obiectivele acestui capitol", font_size=36).next_to(title, DOWN)
        self.play(Write(sub2))
        self.wait(1)

        # ===== Concept 1: Conversia dintre radiani și grade =====
        conversie = Text("Conversia dintre radiani și grade", font_size=30).to_edge(UP)
        self.play(Transform(sub2, conversie))

        # Cercul trigonometric
        circle = Circle(radius=2, color=BLUE)
        radius1 = Line(ORIGIN, [2, 0, 0], color=WHITE)
        radius2 = Line(ORIGIN, [2 * np.cos(PI / 3), 2 * np.sin(PI / 3), 0], color=WHITE)
        arc = Arc(radius=2, start_angle=0, angle=PI/3, color=GREEN)
        deg_label = MathTex("60^\\circ").next_to([2, 0, 0], DOWN)
        rad_label = MathTex("\\frac{\\pi}{3}~rad").next_to([2 * np.cos(PI/3), 2 * np.sin(PI/3), 0], UP)

        self.play(Create(circle))
        self.play(Create(radius1), Create(radius2))
        self.play(Create(arc))
        self.play(Write(deg_label), Write(rad_label))
        self.wait(3)
        self.play(*[FadeOut(m) for m in [circle, radius1, radius2, arc, deg_label, rad_label]])

        # ===== Concept 2: Graficul funcției sinus =====
        titlu_sin = Text("Graficul funcției sinus", font_size=30).to_edge(UP)
        self.play(Transform(sub2, titlu_sin))

        axes = Axes(
            x_range=[0, 2 * PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=3,
            axis_config={"color": WHITE},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="sin(x)")

        sin_graph = axes.plot(lambda x: np.sin(x), color=YELLOW)
        graph_label = axes.get_graph_label(sin_graph, label="\\sin(x)")

        self.play(Create(axes), Write(labels))
        self.play(Create(sin_graph), Write(graph_label))
        self.wait(3)
        self.play(*[FadeOut(m) for m in [axes, sin_graph, graph_label, labels]])

        # ===== Concept 3: Derivarea funcției sinus =====
        titlu_deriv = Text("Derivarea funcției sinus", font_size=30).to_edge(UP)
        self.play(Transform(sub2, titlu_deriv))

        deriv_text = MathTex(r"\frac{d}{dx} \sin(x) = \cos(x)").scale(1.5)
        self.play(Write(deriv_text))
        self.wait(2)
        self.play(FadeOut(deriv_text))

        # ===== Concept 4: Funcții trigonometrice inverse =====
        titlu_inv = Text("Funcțiile trigonometrice inverse", font_size=30).to_edge(UP)
        self.play(Transform(sub2, titlu_inv))

        inverse_text = MathTex(r"\arcsin(x),~\arccos(x),~\arctan(x)").scale(1.2)
        self.play(Write(inverse_text))
        self.wait(2)

        # Încheiere
        recap = Text("Acestea sunt conceptele cheie din introducere!", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(Write(recap))
        self.wait(3)
