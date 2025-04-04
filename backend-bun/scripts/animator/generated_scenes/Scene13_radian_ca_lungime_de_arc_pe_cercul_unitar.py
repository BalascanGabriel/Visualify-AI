from manim import *

class Scene13_radian_ca_lungime_de_arc_pe_cercul_unitar(Scene):
    def construct(self):
        from manim import *
        
        class RadianExplanation(Scene):
            def construct(self):
                # Title
                title = Text("Radian ca lungime de arc pe cercul unitar", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanation text
                explanation = Tex(
                    "Un radian este unghiul la centru al unui cerc care interceptează un arc de lungime egală cu raza cercului.",
                    color=WHITE
                )
                explanation.to_edge(LEFT).shift(0.5*DOWN)
                self.play(Write(explanation))
        
                # Unit circle
                circle = Circle(radius=1, color=YELLOW)
                self.play(Create(circle))
        
                # Radius
                radius = Line(ORIGIN, RIGHT, color=RED)
                radius_label = Tex("r", color=WHITE).next_to(radius.get_end(), RIGHT)
                self.play(Create(radius), Write(radius_label))
        
                # Arc
                arc = Arc(radius=1, start_angle=0, angle=1, color=GREEN)
                arc_label = Tex("1 radian", color=WHITE).next_to(arc.point_from_proportion(0.5), UP)
                self.play(Create(arc), Write(arc_label))
        
                # Formula
                formula = MathTex("1\\text{ radian} = \\frac{\\text{lungimea arc} }{\\text{raza}}", color=WHITE)
                formula.next_to(circle, DOWN)
                self.play(Write(formula))
        
                # Highlight the arc length
                self.play(Indicate(arc, color=GREEN))
        
                # Animate full circle and radians
                full_circle_arc = Arc(radius=1, start_angle=0, angle=TAU, color=GREEN)
                full_circle_arc_label = MathTex("2\\pi \\text{ radiani}", color=WHITE).next_to(full_circle_arc.point_from_proportion(0.5), UP)
                self.play(Transform(arc, full_circle_arc), Transform(arc_label, full_circle_arc_label))
        
                self.wait(2)
