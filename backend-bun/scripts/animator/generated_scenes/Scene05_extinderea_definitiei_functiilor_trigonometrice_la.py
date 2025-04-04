from manim import *

class Scene05_extinderea_definitiei_functiilor_trigonometrice_la(Scene):
    def construct(self):
        from manim import *
        
        class TrigonometricExtension(Scene):
            def construct(self):
                # Titlu
                title = Text("Extinderea definiției funcțiilor trigonometrice la numere reale", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Funcțiile trigonometrice sunt inițial definite pentru unghiuri în triunghiuri dreptunghice.", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(Write(explanation))
        
                # Cerc trigonometric
                circle = Circle(radius=2, color=YELLOW)
                self.play(Create(circle))
        
                # Punct pe cerc
                dot = Dot(color=RED)
                dot.move_to(circle.point(0))
                self.play(Create(dot))
        
                # Segment de la origine la punct
                line = Line(ORIGIN, dot.get_center(), color=GREEN)
                self.play(Create(line))
        
                # Unghi
                arc = Arc(radius=0.5, start_angle=0, angle=PI/4, color=BLUE)
                arc.move_to(ORIGIN)
                self.play(Create(arc))
        
                # Text unghi
                angle_text = MathTex(r"\theta", color=WHITE)
                angle_text.next_to(arc, RIGHT)
                self.play(Write(angle_text))
        
                # Explicație extindere
                extension_explanation = Tex(r"Definim aceste funcții pentru orice număr real $x$ folosind cercul trigonometric. $x$ reprezintă lungimea arcului de cerc.", color=WHITE)
                extension_explanation.next_to(explanation, DOWN, buff=1)
                self.play(Write(extension_explanation))
        
        
                # Animație mișcare punct pe cerc
                self.play(
                    MoveAlongPath(dot, circle),
                    UpdateFromFunc(line, lambda l: l.become(Line(ORIGIN, dot.get_center(), color=GREEN))),
                    run_time=5
                )
        
        
                # Formulă sin x
                sin_formula = MathTex(r"\sin(x) = \frac{y}{r}", color=WHITE)
                sin_formula.next_to(circle, DOWN, buff=1)
                self.play(Write(sin_formula))
        
                # Formulă cos x
                cos_formula = MathTex(r"\cos(x) = \frac{x}{r}", color=WHITE)
                cos_formula.next_to(sin_formula, DOWN, buff=0.5)
                self.play(Write(cos_formula))
        
                # Explicație r=1
                r_explanation = Tex(r"Pentru simplitate, considerăm $r=1$ (cerc unitate).", color=WHITE)
                r_explanation.next_to(cos_formula, DOWN, buff=0.5)
                self.play(Write(r_explanation))
        
                self.wait(2)
