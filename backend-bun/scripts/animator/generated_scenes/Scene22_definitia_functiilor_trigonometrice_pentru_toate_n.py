from manim import *

class Scene22_definitia_functiilor_trigonometrice_pentru_toate_n(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricFunctions(Scene):
            def construct(self):
                # Title
                title = Text("Definiția funcțiilor trigonometrice pentru toate numerele reale", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanatory text
                explanation = Tex(r"Funcțiile trigonometrice (sinus, cosinus, tangentă) sunt definite inițial pentru unghiuri în triunghiuri dreptunghice.  Această definiție poate fi extinsă la toate numerele reale folosind cercul trigonometric.", color=WHITE)
                explanation.to_edge(LEFT).shift(UP * 0.5)
                self.play(FadeIn(explanation))
        
                # Circle
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Axes
                axes = Axes(
                    x_range=(-3.5, 3.5, 1),
                    y_range=(-2.5, 2.5, 1),
                    x_length=7,
                    y_length=5,
                    axis_config={"color": WHITE}
                )
                self.play(Create(axes))
        
                # Unit circle
                unit_circle = Circle(radius=1, color=GREEN)
                self.play(Create(unit_circle))
        
        
                # Point on circle
                dot = Dot(RIGHT, color=RED)
                self.play(Create(dot))
        
                # Angle
                angle = Angle(RIGHT, UP, radius=0.5, color=BLUE)
                self.play(Create(angle))
        
                # Line to x-axis
                line = Line(dot.get_center(), dot.get_center()[0]*RIGHT, color=RED)
                self.play(Create(line))
        
                # x and y coordinates
                x_coord = MathTex("x = \cos(\theta)", color=WHITE)
                y_coord = MathTex("y = \sin(\theta)", color=WHITE)
                x_coord.next_to(line, DOWN)
                y_coord.next_to(line, LEFT)
        
        
                self.play(Write(x_coord), Write(y_coord))
        
                # Animate rotation
                self.play(Rotate(dot, 2*PI, about_point=ORIGIN, rate_func=linear))
        
                #Extend the explanation
                extended_explanation = Tex(r"Prin rotația punctului pe cerc, putem defini valorile funcțiilor trigonometrice pentru orice unghi, reprezentat de un număr real.", color=WHITE)
                extended_explanation.next_to(explanation, DOWN)
                self.play(FadeIn(extended_explanation))
        
        
        
                self.wait(2)
