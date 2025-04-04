from manim import *

class Scene18_unghiuri_negative(Scene):
    def construct(self):
        from manim import *
        
        class UnghiuriNegative(Scene):
            def construct(self):
                # Titlu
                title = Text("Unghiuri Negative", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Un unghi negativ este măsurat în sensul invers acelor de ceasornic.", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(FadeIn(explanation))
        
                # Axele de coordonate
                axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], axis_config={"include_numbers": True})
                self.play(Create(axes))
        
                # Unghiul pozitiv (de referință)
                angle_pos = Angle(axes.get_x_axis(), Line(axes.c2p(0,0), axes.c2p(2,2)), radius=1, other_angle=False, color=GREEN)
                angle_pos_arc = angle_pos.get_arc()
                angle_pos_label = Tex(r"+45$^\circ$").next_to(angle_pos_arc, RIGHT)
                self.play(Create(angle_pos), Write(angle_pos_label))
        
                # Unghiul negativ
                angle_neg = Angle(axes.get_x_axis(), Line(axes.c2p(0,0), axes.c2p(2,-2)), radius=1, other_angle=False, color=RED)
                angle_neg_arc = angle_neg.get_arc()
                angle_neg_label = Tex(r"-45$^\circ$").next_to(angle_neg_arc, RIGHT)
                self.play(Create(angle_neg), Write(angle_neg_label))
        
                # Măsurarea unghiului negativ
                arc_neg = Arc(start_angle = 0, angle = -PI/4, radius = 1, color = RED)
                arc_neg.next_to(axes.c2p(0,0), RIGHT)
                self.play(Create(arc_neg))
        
                # Explicație finală
                final_explanation = Tex(r"Observăm că unghiul negativ se măsoară în sens invers acelor de ceasornic, față de unghiul pozitiv de referință.", color=WHITE)
                final_explanation.next_to(explanation, DOWN, buff=1)
                self.play(Write(final_explanation))
        
                self.wait(2)
