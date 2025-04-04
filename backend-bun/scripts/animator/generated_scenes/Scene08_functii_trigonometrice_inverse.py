from manim import *

class Scene08_functii_trigonometrice_inverse(Scene):
    def construct(self):
        from manim import *
        
        class InverseTrigonometricFunctions(Scene):
            def construct(self):
                # Titlu
                title = Text("Funcții trigonometrice inverse", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(
                    r"Funcțiile trigonometrice inverse (arcsin, arccos, arctan) returnează unghiul a cărui funcție trigonometrică este egală cu un anumit număr.",
                    color=WHITE
                )
                explanation.to_edge(LEFT, buff=1)
                self.play(FadeIn(explanation))
        
                # Unit Circle
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Axes
                axes = Axes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], x_length=4, y_length=4)
                axes.add_coordinates()
                self.play(Create(axes))
        
                # Arcsin Example
                arcsin_text = Tex(r"\arcsin(1/2) = ?", color=WHITE)
                arcsin_text.next_to(axes, DOWN, buff=1)
                self.play(Write(arcsin_text))
        
                # Point on Unit Circle
                point = Dot(np.array([1, np.sqrt(3) / 2, 0]), color=RED)
                self.play(Create(point))
        
                # Line from Origin to Point
                line = Line(ORIGIN, point.get_center(), color=RED)
                self.play(Create(line))
        
                # Angle Label
                angle = Angle(line, axes.get_x_axis(), radius=0.5, color=GREEN)
                angle_label = MathTex(r"\frac{\pi}{6}", color=GREEN)
                angle_label.next_to(angle, 0.5*UP)
                self.play(Create(angle), Write(angle_label))
        
                # Arcsin Result
                arcsin_result = MathTex(r"\frac{\pi}{6}", color=WHITE)
                arcsin_result.next_to(arcsin_text, RIGHT)
                self.play(Write(arcsin_result))
        
        
                # Arctan Example (similar animation can be added for arccos and other functions)
        
                self.wait(2)
        
        
                self.play(
                    FadeOut(explanation),
                    FadeOut(arcsin_text),
                    FadeOut(arcsin_result),
                    FadeOut(point),
                    FadeOut(line),
                    FadeOut(angle),
                    FadeOut(angle_label),
                )
        
                self.wait(1)
