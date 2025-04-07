from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene13_reprezentarea_unghiurilor_pozitive_si_negative_pe_(Scene):
    def construct(self):
        title = Text("Reprezentarea unghiurilor pozitive și negative pe cercul unitar", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Unghiurile pozitive sunt măsurate în sens trigonometric pozitiv (antiorar), iar unghiurile negative în sens trigonometric negativ (orar).", color=WHITE)
        explanation.next_to(title, DOWN, buff=1)
        self.play(Write(explanation))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        # Punctul de origine
        origin_point = Dot(color=RED)
        self.play(Create(origin_point))
        # Unghi pozitiv
        angle_positive = ValueTracker(0)
        line_positive = Line(start=ORIGIN, end=[1,0,0])
        line_positive.add_updater(lambda l: l.become(Line(start=ORIGIN, end=[np.cos(angle_positive.get_value()), np.sin(angle_positive.get_value()), 0])))
        arc_positive = Arc(radius=1, start_angle=0, angle=angle_positive.get_value(), color=GREEN)
        arc_positive.add_updater(lambda a: a.become(Arc(radius=1, start_angle=0, angle=angle_positive.get_value(), color=GREEN)))
        self.play(Create(line_positive), Create(arc_positive))
        self.play(angle_positive.animate.set_value(np.pi/3))
        positive_angle_label = MathTex(r"\theta").next_to(arc_positive, RIGHT)
        positive_angle_label.add_updater(lambda m: m.next_to(arc_positive, RIGHT))
        self.play(Write(positive_angle_label))
        self.wait()
        positive_angle_text = Text("Unghi pozitiv", color=GREEN).next_to(arc_positive, DOWN)
        self.play(Write(positive_angle_text))
        # Unghi negativ
        angle_negative = ValueTracker(0)
        line_negative = Line(start=ORIGIN, end=[1,0,0])
        line_negative.add_updater(lambda l: l.become(Line(start=ORIGIN, end=[np.cos(angle_negative.get_value()), np.sin(angle_negative.get_value()), 0])))
        arc_negative = Arc(radius=1, start_angle=0, angle=angle_negative.get_value(), color=RED)
        arc_negative.add_updater(lambda a: a.become(Arc(radius=1, start_angle=0, angle=angle_negative.get_value(), color=RED)))
        self.play(Create(line_negative), Create(arc_negative))
        self.play(angle_negative.animate.set_value(-np.pi/4))
        negative_angle_label = MathTex(r"-\theta").next_to(arc_negative, RIGHT)
        negative_angle_label.add_updater(lambda m: m.next_to(arc_negative, RIGHT))
        self.play(Write(negative_angle_label))
        self.wait()
        negative_angle_text = Text("Unghi negativ", color=RED).next_to(arc_negative, DOWN)
        self.play(Write(negative_angle_text))
        # Formule
        formula_sin = MathTex(r"\sin(\theta) = y").next_to(negative_angle_text,DOWN)
        formula_cos = MathTex(r"\cos(\theta) = x").next_to(formula_sin,DOWN)
        self.play(Write(formula_sin),Write(formula_cos))
        self.wait()
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(circle),
        FadeOut(origin_point),
        FadeOut(line_positive),
        FadeOut(arc_positive),
        FadeOut(positive_angle_label),
        FadeOut(positive_angle_text),
        FadeOut(line_negative),
        FadeOut(arc_negative),
        FadeOut(negative_angle_label),
        FadeOut(negative_angle_text),
        FadeOut(formula_sin),
        FadeOut(formula_cos)
        )
