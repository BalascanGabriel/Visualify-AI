from manim import *

class Scene23_reprezentarea_grafica_a_functiilor_trigonometrice(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricFunctions(Scene):
            def construct(self):
                # Titlu
                title = Text("Reprezentarea grafică a funcțiilor trigonometrice", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Text("Vom vizualiza funcțiile sinus și cosinus.", color=WHITE)
                explanation.to_edge(LEFT).shift(UP*0.5)
                self.play(FadeIn(explanation))
        
        
                # Axe
                axes = Axes(
                    x_range=[-3*PI, 3*PI, PI/2],
                    y_range=[-1.5, 1.5, 0.5],
                    axis_config={"include_numbers": True, "include_ticks": True}
                )
                axes.to_edge(DOWN, buff=0.5)
                self.play(Create(axes))
        
        
                # Funcția Sinus
                sin_graph = axes.plot(lambda x: np.sin(x), x_range=[-3*PI, 3*PI], color=RED)
                sin_label = MathTex(r"\sin(x)", color=RED).next_to(sin_graph.get_end(), UR, buff=0.2)
                self.play(Create(sin_graph), Write(sin_label))
        
        
                # Funcția Cosinus
                cos_graph = axes.plot(lambda x: np.cos(x), x_range=[-3*PI, 3*PI], color=GREEN)
                cos_label = MathTex(r"\cos(x)", color=GREEN).next_to(cos_graph.get_start(), UR, buff=0.2)
                self.play(Create(cos_graph), Write(cos_label))
        
                # Punct pe graficul sinus
                dot_sin = Dot(axes.c2p(PI/2, np.sin(PI/2)), color=RED)
                self.play(Create(dot_sin))
        
                # Punct pe graficul cosinus
                dot_cos = Dot(axes.c2p(0, np.cos(0)), color=GREEN)
                self.play(Create(dot_cos))
        
                # Formula generală
                formula = MathTex(r"f(x) = A\sin(Bx + C) + D", color=YELLOW).to_edge(DOWN)
                self.play(Write(formula))
        
                self.wait(2)
