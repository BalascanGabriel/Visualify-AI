from manim import *

class Scene20_cateta_adiacenta(Scene):
    def construct(self):
        from manim import *
        
        class CatetAdiacenta(Scene):
            def construct(self):
                # Titlu
                title = Text("Catetă Adiacentă", color=BLUE, font_size=48)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Catetă adiacentă: latura unui triunghi dreptunghic care este alăturată unui unghi.", color=WHITE, font_size=36)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(FadeIn(explanation))
        
                # Desenarea triunghiului
                triangle = Polygon(
                    [0, 0, 0],
                    [4, 0, 0],
                    [4, 3, 0],
                    stroke_color=YELLOW,
                    fill_color=YELLOW,
                    fill_opacity=0.5
                )
                self.play(Create(triangle))
        
        
                # Evidențierea catetei adiacente
                adjacent_side = Line([4,0,0],[4,3,0], stroke_color=RED, stroke_width=6)
                self.play(Create(adjacent_side))
        
                # Etichetarea unghiului
                angle_label = MathTex(r"\theta", color=GREEN)
                angle_label.next_to(triangle.get_vertices()[0], RIGHT, buff=0.2)
                self.play(Write(angle_label))
        
                # Etichetarea catetei adiacente
                adjacent_label = Text("Catetă adiacentă", color=RED, font_size=24)
                adjacent_label.next_to(adjacent_side, RIGHT, buff=0.3)
                self.play(Write(adjacent_label))
        
                # Formula
                formula = MathTex(r"\text{cos}(\theta) = \frac{\text{Catetă adiacentă}}{\text{Hipotenuză}}", color=WHITE, font_size=36)
                formula.next_to(triangle, DOWN, buff=1)
                self.play(Write(formula))
        
                self.wait(2)
