from manim import *

class Scene15_utilizarea_calculatorului(Scene):
    def construct(self):
        from manim import *
        
        class UtilizareaCalculatorului(Scene):
            def construct(self):
                # Titlu
                title = Text("Utilizarea Calculatorului", color=BLUE, font_size=40)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Calculatorul este un instrument util pentru efectuarea de calcule matematice.", color=WHITE, font_size=24)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(FadeIn(explanation))
        
                # Animație: Calculator simplu
                calculator = SVGMobject("calculator").scale(1.5)
                calculator.set_color(YELLOW)
                calculator.move_to(ORIGIN)
                self.play(Create(calculator))
        
                # Ecran calculator
                screen = Rectangle(height=1.5, width=2, color=GREY)
                screen.next_to(calculator, RIGHT, buff=0.2)
                self.play(Create(screen))
        
        
                # Exemplu de calcul
                problem = MathTex("2 + 2 = ?", color=WHITE, font_size=30)
                problem.next_to(screen, DOWN, buff=0.5)
                self.play(Write(problem))
        
                # Rezultat
                result = MathTex("4", color=GREEN, font_size=30)
                result.next_to(problem, RIGHT, buff=0.3)
                self.wait(1)
                self.play(Write(result))
        
                # Animație: Introducere date
                input_num1 = Tex("2", color=RED, font_size=36)
                input_num1.move_to(screen.get_center()+LEFT*0.5)
                input_num2 = Tex("2", color=RED, font_size=36)
                input_num2.move_to(screen.get_center()+RIGHT*0.5)
                op = Tex("+", color=RED, font_size=36)
                op.move_to(screen.get_center())
                self.play(Write(input_num1),Write(op),Write(input_num2))
                self.wait(1)
        
        
                # Mai multe operații
                more_ops = Tex(r"Poate efectua diverse operații: +,-,*,/, √, ...", color=WHITE, font_size=24)
                more_ops.next_to(explanation, DOWN, buff=0.5)
                self.play(FadeIn(more_ops))
        
                self.wait(2)
