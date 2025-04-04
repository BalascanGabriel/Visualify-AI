from manim import *

class Scene09_unghiuri_pozitive_si_negative(Scene):
    def construct(self):
        from manim import *
        
        class UnghiuriPozitiveNegative(Scene):
            def construct(self):
                # Titlu
                title = Text("Unghiuri Pozitive și Negative", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(
                    "Unghiurile pozitive sunt măsurate în sens trigonometric pozitiv (contra-sensul acelor de ceasornic),"
                    "\\newline în timp ce unghiurile negative sunt măsurate în sens trigonometric negativ (sensul acelor de ceasornic)."
                , color=WHITE)
                explanation.to_edge(LEFT).shift(UP*0.5)
                self.play(FadeIn(explanation))
        
                # Axe de coordonate
                axes = Axes(
                    x_range=[-5, 5, 1],
                    y_range=[-5, 5, 1],
                    x_length=5,
                    y_length=5,
                )
                self.play(Create(axes))
        
                # Unghi pozitiv
                angle_pos = Angle(axes.get_vector([1,1]), axes.get_vector([0,0]), axes.get_vector([1,0]), radius=2, color=GREEN)
                arc_pos = angle_pos.get_arc()
                self.play(Create(angle_pos))
                text_pos = Tex("+θ", color=GREEN).next_to(arc_pos, UP)
                self.play(Write(text_pos))
        
                # Unghi negativ
                angle_neg = Angle(axes.get_vector([-1, -1]), axes.get_vector([0, 0]), axes.get_vector([1, 0]), radius=2, color=RED)
                arc_neg = angle_neg.get_arc()
                self.play(Create(angle_neg))
                text_neg = Tex("-θ", color=RED).next_to(arc_neg, DOWN)
                self.play(Write(text_neg))
        
                # Formule
                formula_pos = MathTex(r"\theta > 0", color=GREEN)
                formula_neg = MathTex(r"\theta < 0", color=RED)
                formula_pos.next_to(text_pos,DOWN)
                formula_neg.next_to(text_neg,DOWN)
                self.play(Write(formula_pos), Write(formula_neg))
        
                self.wait(2)
