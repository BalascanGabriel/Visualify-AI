from manim import *

class Scene12_conversia_grade_radiani(Scene):
    def construct(self):
        from manim import *
        
        class GradeRadiani(Scene):
            def construct(self):
                # Titlu
                title = Text("Conversia Grade - Radiani", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"$\text{180}^{\circ} = \pi \text{ radiani}$", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(Write(explanation))
        
                # Cerc unitate
                circle = Circle(radius=1, color=YELLOW)
                self.play(Create(circle))
        
                # Marcarea unui unghi de 30 grade
                angle_30 = Angle(Line(ORIGIN, RIGHT), Line(ORIGIN, RIGHT, stroke_width=2), radius=0.5, color=RED)
                angle_30_label = MathTex("30^\circ", color=RED)
                angle_30_label.next_to(angle_30, UP)
                self.play(Create(angle_30), Write(angle_30_label))
        
        
                #Conversie in radiani
                conversion_text = MathTex(r"30^\circ \times \frac{\pi}{180^\circ} = \frac{\pi}{6} \text{ radiani}", color=GREEN)
                conversion_text.next_to(explanation, DOWN)
                self.play(Write(conversion_text))
        
        
                # Arc corespunzator
                arc = Arc(start_angle=0, angle=PI/6, radius=1, color=GREEN)
                self.play(Create(arc))
        
                # Explicatie arc lungime
                arc_length_text = MathTex(r"\text{Lungime arc} = r \theta", color=WHITE)
                arc_length_text.next_to(conversion_text, DOWN)
                self.play(Write(arc_length_text))
        
                # Exemplu numeric
                numeric_example = MathTex(r"\text{Lungime arc} = 1 \times \frac{\pi}{6} = \frac{\pi}{6}", color=WHITE)
                numeric_example.next_to(arc_length_text, DOWN)
                self.play(Write(numeric_example))
        
        
        
                self.wait(2)
