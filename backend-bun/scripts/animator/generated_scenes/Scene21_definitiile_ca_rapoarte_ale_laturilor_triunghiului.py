from manim import *

class Scene21_definitiile_ca_rapoarte_ale_laturilor_triunghiului(Scene):
    def construct(self):
        from manim import *
        
        class TriangleRatios(Scene):
            def construct(self):
                # Titlu
                title = Text("Definițiile Trigonometrice ca Rapoarte ale Laturilor Triunghiului", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Triunghi dreptunghic
                triangle = Triangle(color=YELLOW).scale(2)
                triangle.set_fill(YELLOW, opacity=0.5)
                triangle.rotate(-PI/6)
                self.play(Create(triangle))
        
                # Etichetarea vârfurilor
                A = triangle.get_vertices()[0]
                B = triangle.get_vertices()[1]
                C = triangle.get_vertices()[2]
                
                A_label = Tex("A").next_to(A, UP+LEFT, buff=0.1)
                B_label = Tex("B").next_to(B, DOWN, buff=0.1)
                C_label = Tex("C").next_to(C, RIGHT, buff=0.1)
        
                self.play(Write(A_label), Write(B_label), Write(C_label))
        
                # Etichetarea laturilor
                a = Line(B,C).get_length()
                b = Line(A,C).get_length()
                c = Line(A,B).get_length()
        
                a_label = Tex("a").next_to(Line(B,C), DOWN, buff=0.1).scale(0.8)
                b_label = Tex("b").next_to(Line(A,C), LEFT, buff=0.1).scale(0.8)
                c_label = Tex("c").next_to(Line(A,B), UP, buff=0.1).scale(0.8)
        
                self.play(Write(a_label), Write(b_label), Write(c_label))
        
                # Definiții trigonometrice
                sinA_formula = MathTex(r"\sin A = \frac{a}{c}", color=GREEN)
                cosA_formula = MathTex(r"\cos A = \frac{b}{c}", color=RED)
                tanA_formula = MathTex(r"\tan A = \frac{a}{b}", color=BLUE)
        
                formulas = VGroup(sinA_formula, cosA_formula, tanA_formula)
                formulas.arrange(DOWN, buff=0.5).next_to(triangle, DOWN, buff=1)
        
                self.play(Write(sinA_formula), Write(cosA_formula), Write(tanA_formula))
        
                #Explicație
                explanation = Tex("Rapoartele laturilor triunghiului definesc funcțiile trigonometrice.", color = WHITE)
                explanation.to_edge(LEFT).shift(UP)
                self.play(FadeIn(explanation))
        
                self.wait(2)
