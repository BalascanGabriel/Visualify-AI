from manim import *

class Scene02_conversia_intre_radiani_si_grade(Scene):
    def construct(self):
        from manim import *
        
        class RadianDegreeConversion(Scene):
            def construct(self):
                # Title
                title = Text("Conversia între Radiani și Grade", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanatory Text
                explanation = Tex(r"$\text{180}^\circ = \pi \text{ radiani}$", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(Write(explanation))
        
                # Circle for visualization
                circle = Circle(radius=1, color=YELLOW)
                circle.move_to(ORIGIN)
                self.play(Create(circle))
        
                # Degree Arc
                degree_arc = Arc(radius=1, start_angle=0, angle=PI, color=RED)
                degree_text = Tex(r"$180^\circ$", color=RED)
                degree_text.next_to(degree_arc, DOWN)
        
                # Radian Arc
                radian_arc = Arc(radius=1, start_angle=0, angle=PI, color=GREEN)
                radian_text = Tex(r"$\pi$", color=GREEN)
                radian_text.next_to(radian_arc, UP)
        
                # Conversion Formula
                formula1 = MathTex(r"\text{Grade} = \frac{180^\circ}{\pi} \times \text{Radiani}", color=WHITE)
                formula2 = MathTex(r"\text{Radiani} = \frac{\pi}{180^\circ} \times \text{Grade}", color=WHITE)
                formula1.next_to(circle, DOWN)
                formula2.next_to(formula1, DOWN)
        
                # Animations
                self.play(Create(degree_arc), Write(degree_text))
                self.wait(1)
                self.play(Transform(degree_arc, radian_arc), Transform(degree_text, radian_text))
                self.wait(1)
                self.play(Write(formula1))
                self.wait(1)
                self.play(Write(formula2))
                self.wait(2)
        
        
                # Example conversion
                example = Tex(r"$\text{Convertim } 90^\circ \text{ în radiani:}$", color=WHITE)
                example.next_to(formula2, DOWN)
                self.play(Write(example))
                calculation = MathTex(r"\frac{\pi}{180^\circ} \times 90^\circ = \frac{\pi}{2}", color=WHITE)
                calculation.next_to(example, DOWN)
                self.play(Write(calculation))
                self.wait(2)
