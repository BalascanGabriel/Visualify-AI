from manim import *

config.tex_template.add_to_preamble(r"""
\usepackage{amsmath}
\usepackage{amssymb}
""")

class Scene16_unghiuri_pozitive_si_negative_ca_rotatii_pe_cercul(Scene):
    def construct(self):
        title = Text("Unghiuri pozitive și negative ca rotații pe cercul unitate.", color=BLUE_A)
        title.scale(1.2).to_edge(UP)
        self.play(Write(title))
        explanation = Text("Rotațiile pozitive sunt în sens invers acelor de ceasornic, iar rotațiile negative sunt în sensul acelor de ceasornic.", color=WHITE)
        explanation.next_to(title, DOWN)
        self.play(FadeIn(explanation))
        circle = Circle(radius=1, color=YELLOW)
        self.play(Create(circle))
        arrow = Arrow(ORIGIN, RIGHT, buff=0, color=RED)
        self.play(Create(arrow))
        theta_pos = MathTex(r"\theta^+")
        theta_pos.next_to(circle, RIGHT, buff=0.5)
        theta_pos.set_color(GREEN)
        theta_neg = MathTex(r"\theta^-")
        theta_neg.next_to(circle, LEFT, buff=0.5)
        theta_neg.set_color(PURPLE)
        arc_pos = Arc(radius=1, start_angle=0, angle=PI/3, color=GREEN)
        arc_neg = Arc(radius=1, start_angle=0, angle=-PI/3, color=PURPLE)
        self.play(Write(theta_pos))
        self.play(Create(arc_pos))
        self.wait()
        self.play(Write(theta_neg))
        self.play(Create(arc_neg))
        self.wait()
        point_pos = Dot(arc_pos.get_end(), color=GREEN)
        point_neg = Dot(arc_neg.get_end(), color=PURPLE)
        self.play(Create(point_pos))
        self.play(Create(point_neg))
        coords_pos = MathTex(r"\cos(\theta^+), \sin(\theta^+)")
        coords_pos.next_to(point_pos, RIGHT)
        coords_pos.set_color(GREEN)
        coords_neg = MathTex(r"\cos(\theta^-), \sin(\theta^-)")
        coords_neg.next_to(point_neg, LEFT)
        coords_neg.set_color(PURPLE)
        self.play(Write(coords_pos))
        self.play(Write(coords_neg))
        self.wait(2)
        self.play(
        FadeOut(title),
        FadeOut(explanation),
        FadeOut(circle),
        FadeOut(arrow),
        FadeOut(theta_pos),
        FadeOut(theta_neg),
        FadeOut(arc_pos),
        FadeOut(arc_neg),
        FadeOut(point_pos),
        FadeOut(point_neg),
        FadeOut(coords_pos),
        FadeOut(coords_neg)
        )
