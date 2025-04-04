from manim import *

class Scene11_masurarea_in_radiani(Scene):
    def construct(self):
        from manim import *
        
        class Radiani(Scene):
            def construct(self):
                # Titlu
                title = Text("Măsurarea în Radiani", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Un radian este unghiul subtins la centru de un arc de cerc cu lungimea egală cu raza cercului.", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(FadeIn(explanation))
        
                # Cerc
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Rază
                radius = Line(circle.get_center(), circle.point_at_angle(0), color=RED)
                radius_label = Tex("r", color=RED).next_to(radius.get_center(), RIGHT)
                self.play(Create(radius), Write(radius_label))
        
                # Arc
                arc = Arc(radius=2, start_angle=0, angle=1, color=GREEN)
                arc_label = Tex("r", color=GREEN).next_to(arc.point_at_angle(0.5), UP)
        
                self.play(Create(arc), Write(arc_label))
        
                # Unghi
                angle = Angle(radius, arc, radius=0.5, color=BLUE)
                angle_label = Tex("1 radian", color=BLUE).next_to(angle, RIGHT)
                self.play(Create(angle), Write(angle_label))
        
        
                # Formula
                formula = MathTex(r"\theta = \frac{s}{r}", color=WHITE)
                formula.next_to(circle, DOWN)
                self.play(Write(formula))
        
                # Explicație formulă
                formula_explanation = Tex(r"unde $\theta$ este unghiul în radiani, s este lungimea arcului și r este raza.", color=WHITE)
                formula_explanation.next_to(formula, DOWN)
                self.play(Write(formula_explanation))
        
                self.wait(2)
