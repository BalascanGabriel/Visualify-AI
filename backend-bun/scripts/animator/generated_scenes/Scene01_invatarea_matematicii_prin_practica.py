from manim import *

class Scene01_invatarea_matematicii_prin_practica(Scene):
    def construct(self):
        from manim import *
        
        class LearningMathByPractice(Scene):
            def construct(self):
                # Titlu
                title = Text("Învățarea matematicii prin practică", color=BLUE, font_size=36)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ în stânga
                explanation = Tex(r"Practica este cheia înțelegerii conceptelor matematice.", color=WHITE, font_size=24)
                explanation.to_edge(LEFT).shift(UP*0.5)
                self.play(FadeIn(explanation))
        
                # Animație 1: Exemplu de problemă
                problem = Tex(r"2 + 2 = ?", color=YELLOW, font_size=36)
                problem.move_to(ORIGIN).shift(UP*1)
                self.play(Write(problem))
        
                # Animație 2: Rezolvare pas cu pas
                step1 = Tex(r"2 + 2 = 4", color=GREEN, font_size=36)
                step1.next_to(problem, DOWN)
                self.play(Write(step1))
        
                #Animație 3: Exemplu mai complex
                problem2 = MathTex(r"\int_0^1 x^2 \, dx", color=YELLOW, font_size=36)
                problem2.next_to(step1, DOWN)
                self.play(Write(problem2))
        
        
                #Animație 4: Rezolvare pas cu pas
                step2_1 = MathTex(r"\left[ \frac{x^3}{3} \right]_0^1", color=GREEN, font_size=30)
                step2_2 = MathTex(r"= \frac{1}{3} - 0 = \frac{1}{3}", color=GREEN, font_size=30)
                step2_1.next_to(problem2, DOWN)
                step2_2.next_to(step2_1, DOWN)
                self.play(Write(step2_1))
                self.play(Write(step2_2))
        
        
                #Concluzie
                conclusion = Tex(r"Prin rezolvarea de probleme, înțelegi mai bine conceptele.", color=WHITE, font_size=24)
                conclusion.next_to(step2_2, DOWN)
                self.play(Write(conclusion))
        
                self.wait(2)
