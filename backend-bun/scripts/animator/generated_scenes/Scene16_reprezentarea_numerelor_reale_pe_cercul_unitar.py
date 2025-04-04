from manim import *

class Scene16_reprezentarea_numerelor_reale_pe_cercul_unitar(Scene):
    def construct(self):
        from manim import *
        
        class RealNumbersOnUnitCircle(Scene):
            def construct(self):
                # Title
                title = Text("Reprezentarea numerelor reale pe cercul unitar", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanation
                explanation = Tex(r"Fiecare număr real $x$ poate fi reprezentat ca un punct pe cercul unitar prin unghiul $\theta = x$ (în radiani).", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(FadeIn(explanation))
        
                # Unit Circle
                circle = Circle(radius=1, color=YELLOW)
                self.play(Create(circle))
        
                # Axes
                axes = Axes(
                    x_range=[-1.2, 1.2, 1],
                    y_range=[-1.2, 1.2, 1],
                    x_length=3,
                    y_length=3,
                )
                axes.set_color(WHITE)
                self.play(Create(axes))
        
                # Point on Circle
                dot = Dot(color=RED)
                dot.move_to(RIGHT)
                self.play(Create(dot))
        
                # Angle
                angle = Angle(axes.get_x_axis(), Line(ORIGIN, dot.get_center()), radius=0.5, color=GREEN)
                self.play(Create(angle))
        
                # Number line representation
                number_line = NumberLine(
                    x_range=[-2*PI, 2*PI, PI/2],
                    length=6,
                    include_numbers=True,
                    numbers_to_include = [-2*PI,-PI,0,PI,2*PI],
                    color=WHITE
                ).to_edge(DOWN, buff=0.5)
                self.play(Create(number_line))
        
                # Mapping
                x_value = ValueTracker(0)
                theta_text = DecimalNumber(0, num_decimal_places=2, color=WHITE)
                theta_text.add_updater(lambda x: x.set_value(x_value.get_value()))
                theta_text.next_to(number_line,UP)
                self.play(Create(theta_text))
        
                def update_dot(mobject):
                    x = x_value.get_value()
                    point = np.array([np.cos(x), np.sin(x), 0])
                    mobject.move_to(point)
        
                    angle.become(Angle(axes.get_x_axis(), Line(ORIGIN, point), radius=0.5, color=GREEN))
        
                dot.add_updater(update_dot)
                self.play(x_value.animate.set_value(2*PI), run_time=5, rate_func=linear)
        
        
                # Formula
                formula = MathTex(r"\theta = x", color=WHITE)
                formula.next_to(circle, DOWN)
                self.play(Write(formula))
        
                self.wait(1)
