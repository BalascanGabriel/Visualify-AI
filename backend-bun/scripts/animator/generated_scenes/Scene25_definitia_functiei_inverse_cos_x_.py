from manim import *

class Scene25_definitia_functiei_inverse_cos_x_(Scene):
    def construct(self):
        from manim import *
        
        class InverseCosineDefinition(Scene):
            def construct(self):
                # Title
                title = Text("Definiția funcției inverse cos⁻¹(x)", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanatory text
                explanation = Tex(
                    "cos⁻¹(x) (arccos(x)) este funcția inversă a funcției cosinus.",
                    " Returnează unghiul \\(\\theta\\) (în radiani) pentru care \\(cos(\\theta) = x\\).",
                    color=WHITE
                )
                explanation.to_edge(LEFT).shift(0.5*UP)
                self.play(FadeIn(explanation))
        
                # Unit circle
                circle = Circle(radius=1, color=YELLOW)
                self.play(Create(circle))
        
                # Axes
                axes = Axes(
                    x_range=[-1.1, 1.1, 0.5],
                    y_range=[-1.1, 1.1, 0.5],
                    x_length=3,
                    y_length=3
                )
                axes.add_coordinates()
                self.play(Create(axes))
        
                # x-value
                x_value = 0.5
                x_line = Line([x_value, 0, 0], [x_value, 1, 0], color=RED)
                x_label = MathTex("x").next_to(x_line, UP, buff=0.1).set_color(RED)
        
                self.play(Create(x_line),Write(x_label))
        
                # Angle theta
                theta = np.arccos(x_value)
                angle = Angle(Line(ORIGIN, [1,0,0]),Line(ORIGIN,[np.cos(theta),np.sin(theta),0]),radius=0.5,color=GREEN)
                theta_label = MathTex("\\theta").next_to(angle,0.7*UP).set_color(GREEN)
        
                self.play(Create(angle), Write(theta_label))
        
        
                # Line to point on circle
                line_to_point = Line(ORIGIN, [x_value, np.sqrt(1 - x_value**2), 0], color=GREEN)
                point_on_circle = Dot([x_value, np.sqrt(1 - x_value**2), 0], color=GREEN)
        
                self.play(Create(line_to_point),Create(point_on_circle))
        
        
                # Formula
                formula = MathTex("cos^{-1}(x) = \\theta").next_to(axes, DOWN, buff=0.5).set_color(WHITE)
                self.play(Write(formula))
        
                self.wait(2)
