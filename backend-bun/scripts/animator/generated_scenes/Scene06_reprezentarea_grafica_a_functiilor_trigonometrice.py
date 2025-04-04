from manim import *

class Scene06_reprezentarea_grafica_a_functiilor_trigonometrice(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricFunctions(Scene):
            def construct(self):
                # Title
                title = Text("Reprezentarea grafică a funcțiilor trigonometrice", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Axes
                axes = Axes(
                    x_range=[-2*PI, 2*PI, PI/2],
                    y_range=[-1.5, 1.5, 0.5],
                    axis_config={"include_numbers": True, "include_tip": True}
                )
                axes.to_edge(DOWN, buff=0.5)
                self.play(Create(axes))
        
                # Sinus Function
                sin_graph = axes.plot(lambda x: np.sin(x), color=RED)
                sin_label = MathTex(r"y = \sin(x)", color=RED).next_to(sin_graph.get_end(), UP, buff=0.2)
                self.play(Create(sin_graph), Write(sin_label))
        
                # Cosinus Function
                cos_graph = axes.plot(lambda x: np.cos(x), color=GREEN)
                cos_label = MathTex(r"y = \cos(x)", color=GREEN).next_to(cos_graph.get_start(), UP, buff=0.2)
                self.wait(0.5)
                self.play(Create(cos_graph), Write(cos_label))
        
                #Explanation Text
                explanation = Tex("Observăm că funcțiile sinus și cosinus sunt oscilatorii", color = WHITE).next_to(axes, UP, buff=1)
                self.play(Write(explanation))
        
        
                #Highlighting a point
                dot = Dot(color=YELLOW).move_to(axes.c2p(PI/2, np.sin(PI/2)))
                self.play(Create(dot))
                self.wait(1)
        
                #Fade out
                self.play(FadeOut(dot), FadeOut(explanation), FadeOut(sin_label), FadeOut(cos_label), FadeOut(sin_graph), FadeOut(cos_graph), FadeOut(title), FadeOut(axes))
