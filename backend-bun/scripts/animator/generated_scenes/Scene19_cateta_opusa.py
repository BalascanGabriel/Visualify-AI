from manim import *

class Scene19_cateta_opusa(Scene):
    def construct(self):
        from manim import *
        
        class CatetaOpusa(Scene):
            def construct(self):
                # Titlu
                title = Text("Catetă Opusă", color=BLUE, font_size=48)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Triunghi dreptunghic
                triangle = Polygon(LEFT*3, ORIGIN, RIGHT*3+UP*2, color=YELLOW, fill_opacity=0.5)
                self.play(Create(triangle))
        
                # Etichetarea vârfurilor
                A = Text("A", color=WHITE, font_size=36).next_to(triangle.get_vertices()[0], UL)
                B = Text("B", color=WHITE, font_size=36).next_to(triangle.get_vertices()[1], DOWN)
                C = Text("C", color=WHITE, font_size=36).next_to(triangle.get_vertices()[2], UR)
                self.play(Write(A), Write(B), Write(C))
        
                # Evidențierea catetei opuse
                opposite_side = Line(triangle.get_vertices()[0], triangle.get_vertices()[2], color=RED, stroke_width=6)
                self.play(Create(opposite_side))
        
                # Text explicativ
                explanation = Text("Catetă opusă (a) este latura opusă unghiului considerat (în acest caz, unghiul B).", color=WHITE, font_size=24)
                explanation.next_to(triangle, DOWN, buff=1)
                self.play(Write(explanation))
        
                # Formula
                formula = MathTex(r"a = \text{cateta opusă}", color=WHITE, font_size=36)
                formula.next_to(explanation, DOWN, buff=0.5)
                self.play(Write(formula))
        
                # Unghiul
                angle_B = Angle(Line(triangle.get_vertices()[0],triangle.get_vertices()[1]),Line(triangle.get_vertices()[1],triangle.get_vertices()[2]),radius=0.5,color=GREEN)
                self.play(Create(angle_B))
                
        
                self.wait(2)
