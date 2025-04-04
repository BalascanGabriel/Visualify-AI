from manim import *

class Scene07_derivarea_functiilor_trigonometrice(Scene):
    def construct(self):
        from manim import *
        
        class DerivateTrigonometrice(Scene):
            def construct(self):
                # Titlu
                title = Text("Derivarea Funcțiilor Trigonometrice", color=BLUE)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"Vom demonstra derivatele pentru $\sin(x)$ și $\cos(x)$ folosind definiția limitei.", color=WHITE)
                explanation.to_edge(LEFT).shift(DOWN)
                self.play(Write(explanation))
        
        
                # Sin(x)
                sin_text = MathTex(r"\frac{d}{dx} \sin(x) = \lim_{h \to 0} \frac{\sin(x+h) - \sin(x)}{h}", color=YELLOW)
                sin_text.next_to(explanation, DOWN, buff=1)
                self.play(Write(sin_text))
        
                sin_formula = MathTex(r"= \lim_{h \to 0} \frac{\sin(x)\cos(h) + \cos(x)\sin(h) - \sin(x)}{h}", color=YELLOW)
                sin_formula.next_to(sin_text, DOWN)
                self.play(TransformMatchingTex(sin_text, sin_formula))
        
                sin_formula2 = MathTex(r"= \lim_{h \to 0} \frac{\sin(x)(\cos(h)-1) + \cos(x)\sin(h)}{h}", color=YELLOW)
                sin_formula2.next_to(sin_formula, DOWN)
                self.play(TransformMatchingTex(sin_formula, sin_formula2))
        
                sin_formula3 = MathTex(r"= \sin(x) \lim_{h \to 0} \frac{\cos(h)-1}{h} + \cos(x) \lim_{h \to 0} \frac{\sin(h)}{h}", color=YELLOW)
                sin_formula3.next_to(sin_formula2, DOWN)
                self.play(TransformMatchingTex(sin_formula2, sin_formula3))
        
                sin_result = MathTex(r"= \cos(x)", color=GREEN)
                sin_result.next_to(sin_formula3, DOWN)
                self.play(Write(sin_result))
        
        
        
                # Cos(x)
                cos_text = MathTex(r"\frac{d}{dx} \cos(x) = \lim_{h \to 0} \frac{\cos(x+h) - \cos(x)}{h}", color=RED)
                cos_text.next_to(sin_result, DOWN, buff=1)
                self.play(Write(cos_text))
        
                cos_formula = MathTex(r"= \lim_{h \to 0} \frac{\cos(x)\cos(h) - \sin(x)\sin(h) - \cos(x)}{h}", color=RED)
                cos_formula.next_to(cos_text, DOWN)
                self.play(TransformMatchingTex(cos_text, cos_formula))
        
                cos_formula2 = MathTex(r"= \cos(x) \lim_{h \to 0} \frac{\cos(h)-1}{h} - \sin(x) \lim_{h \to 0} \frac{\sin(h)}{h}", color=RED)
                cos_formula2.next_to(cos_formula, DOWN)
                self.play(TransformMatchingTex(cos_formula, cos_formula2))
        
                cos_result = MathTex(r"= -\sin(x)", color=GREEN)
                cos_result.next_to(cos_formula2, DOWN)
                self.play(Write(cos_result))
        
                self.wait(2)
