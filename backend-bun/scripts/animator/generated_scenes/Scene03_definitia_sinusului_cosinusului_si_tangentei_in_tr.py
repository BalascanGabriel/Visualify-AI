from manim import *

class Scene03_definitia_sinusului_cosinusului_si_tangentei_in_tr(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricFunctions(Scene):
            def construct(self):
                # Titlu
                title = Text("Definiția sinusului, cosinusului și tangentei în triunghiuri dreptunghice", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Triunghi dreptunghic
                triangle = Polygon(ORIGIN, 4*RIGHT, 4*RIGHT + 3*UP, color=YELLOW, fill_opacity=0.5)
                self.play(Create(triangle))
        
                # Etichete vârfuri
                A = Tex("A").next_to(triangle.get_vertices()[0], DOWN)
                B = Tex("B").next_to(triangle.get_vertices()[1], DOWN)
                C = Tex("C").next_to(triangle.get_vertices()[2], RIGHT)
                self.play(Write(A), Write(B), Write(C))
        
                # Lungimi laturi
                a = MathTex("a").next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[2]), RIGHT)
                b = MathTex("b").next_to(Line(triangle.get_vertices()[1], triangle.get_vertices()[2]), LEFT)
                c = MathTex("c").next_to(Line(triangle.get_vertices()[0], triangle.get_vertices()[1]), UP)
                self.play(Write(a), Write(b), Write(c))
        
                # Definiții
                sin_def = MathTex(r"\sin(\theta) = \frac{a}{c}").to_edge(LEFT).shift(2*UP)
                cos_def = MathTex(r"\cos(\theta) = \frac{b}{c}").to_edge(LEFT).shift(UP)
                tan_def = MathTex(r"\tan(\theta) = \frac{a}{b}").to_edge(LEFT)
                self.play(Write(sin_def), Write(cos_def), Write(tan_def))
        
        
                # Evidențiere unghi
                theta = MathTex("\\theta").next_to(triangle.get_vertices()[0], RIGHT)
                self.play(Write(theta))
        
                # Evidențiere laturi
                self.play( Indicate(Line(triangle.get_vertices()[0], triangle.get_vertices()[2]), color=RED) )
                self.play( Indicate(Line(triangle.get_vertices()[1], triangle.get_vertices()[2]), color=GREEN) )
                self.play( Indicate(Line(triangle.get_vertices()[0], triangle.get_vertices()[1]), color=BLUE) )
        
        
        
                self.wait(2)
