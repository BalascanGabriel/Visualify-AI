from manim import *

class Scene10_masurarea_in_grade(Scene):
    def construct(self):
        from manim import *
        
        class MasurareaInGrade(Scene):
            def construct(self):
                # Titlu
                title = Text("Măsurarea în Grade", color=BLUE, font_size=48)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Un cerc complet are 360 de grade.", color=WHITE)
                explanation.to_edge(LEFT, buff=1)
                self.play(Write(explanation))
        
                # Cerc
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Punct central
                center_dot = Dot(color=RED)
                self.play(Create(center_dot))
        
                # Raze
                radius1 = Line(center_dot.get_center(), circle.get_right(), color=GREEN)
                radius2 = Line(center_dot.get_center(), circle.get_top(), color=GREEN)
                self.play(Create(radius1), Create(radius2))
        
                # Arc de 90 de grade
                arc = Arc(radius=2, start_angle=0, angle=PI/2, color=BLUE)
                self.play(Create(arc))
        
                # Text 90 de grade
                degree_text = Tex(r"$90^\circ$", color=WHITE, font_size=36)
                degree_text.next_to(arc, RIGHT, buff=0.5)
                self.play(Write(degree_text))
        
                # Arc de 180 de grade
                arc2 = Arc(radius=2, start_angle=0, angle=PI, color=BLUE)
                degree_text2 = Tex(r"$180^\circ$", color=WHITE, font_size=36)
                degree_text2.next_to(arc2, DOWN, buff=0.5)
        
                self.play(Transform(arc, arc2), Transform(degree_text, degree_text2))
        
                # Arc de 360 de grade
                arc3 = Arc(radius=2, start_angle=0, angle=TAU, color=BLUE)
                degree_text3 = Tex(r"$360^\circ$", color=WHITE, font_size=36)
                degree_text3.next_to(arc3, DOWN, buff=0.5)
                
                self.play(Transform(arc, arc3), Transform(degree_text, degree_text3))
        
                self.wait(1)
