from manim import *

class Scene04_calculul_sinusului_cosinusului_si_tangentei_pentru(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricFunctions(Scene):
            def construct(self):
                # Title
                title = Text("Calculul sinusului, cosinusului și tangentei pentru unghiuri specifice (π/6, π/4, π/2)", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explanation
                explanation = Tex(r"Vom vizualiza valorile trigonometrice pentru unghiurile $\frac{\pi}{6}$, $\frac{\pi}{4}$ și $\frac{\pi}{2}$ folosind un cerc trigonometric.", color=WHITE)
                explanation.to_edge(LEFT, buff=1)
                self.play(FadeIn(explanation))
        
                # Circle
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Axes
                axes = Axes(
                    x_range=[-2.5, 2.5, 1],
                    y_range=[-2.5, 2.5, 1],
                    axis_config={"include_tip": False}
                )
                axes.set_stroke(width=2)
        
                self.play(Create(axes))
        
                # Angles and values
                angles = [PI/6, PI/4, PI/2]
                colors = [RED, GREEN, BLUE]
                labels = [r"\frac{\pi}{6}", r"\frac{\pi}{4}", r"\frac{\pi}{2}"]
        
                for i, angle in enumerate(angles):
                    line = Line(ORIGIN, 2*np.array([np.cos(angle), np.sin(angle), 0]))
                    arc = Arc(radius=2, start_angle=0, angle=angle, color=colors[i])
                    angle_label = Tex(labels[i]).next_to(arc.get_center(), (np.cos(angle/2), np.sin(angle/2),0))
        
                    sin_val = MathTex(f"sin({labels[i]}) = {round(np.sin(angle), 2)}").next_to(line.get_end(), RIGHT)
                    cos_val = MathTex(f"cos({labels[i]}) = {round(np.cos(angle), 2)}").next_to(sin_val, DOWN)
                    tan_val = MathTex(f"tan({labels[i]}) = {round(np.tan(angle), 2)}").next_to(cos_val, DOWN)
                  
        
                    self.play(Create(arc),Create(line), Write(angle_label),Write(sin_val), Write(cos_val),Write(tan_val))
                    self.wait(1)
        
        
                self.wait(2)
