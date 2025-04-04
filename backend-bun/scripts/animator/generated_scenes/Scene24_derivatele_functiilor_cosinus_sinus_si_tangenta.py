from manim import *

class Scene24_derivatele_functiilor_cosinus_sinus_si_tangenta(Scene):
    def construct(self):
        from manim import *
        
        class DerivateTrigonometrice(Scene):
            def construct(self):
                # Titlu
                title = Text("Derivatele funcțiilor cosinus, sinus și tangentă", color=BLUE, font_size=30)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Explicație generală
                explanation = Tex(r"Derivata unei funcții reprezintă panta tangentei la graficul funcției într-un punct dat.", color=WHITE, font_size=24)
                explanation.to_edge(LEFT).shift(UP * 0.5)
                self.play(FadeIn(explanation))
        
                # Funcția sinus
                sin_graph = FunctionGraph(lambda x: np.sin(x), color=YELLOW, x_range=[-3*PI, 3*PI])
                sin_label = MathTex(r"f(x) = \sin(x)", color=WHITE)
                sin_deriv_label = MathTex(r"f'(x) = \cos(x)", color=GREEN)
                sin_group = VGroup(sin_graph, sin_label, sin_deriv_label)
                sin_group.arrange(DOWN, buff=0.5).to_edge(LEFT).shift(DOWN * 0.5)
                sin_label.shift(UP*0.2)
                sin_deriv_label.shift(DOWN*0.2)
        
                self.play(Create(sin_graph), Write(sin_label))
                self.wait(1)
                self.play(TransformMatchingTex(sin_label.copy(), sin_deriv_label))
        
        
                # Funcția cosinus
                cos_graph = FunctionGraph(lambda x: np.cos(x), color=RED, x_range=[-3*PI, 3*PI])
                cos_label = MathTex(r"g(x) = \cos(x)", color=WHITE)
                cos_deriv_label = MathTex(r"g'(x) = -\sin(x)", color=GREEN)
                cos_group = VGroup(cos_graph, cos_label, cos_deriv_label)
                cos_group.arrange(DOWN, buff=0.5).next_to(sin_group, RIGHT, buff=2)
                cos_label.shift(UP*0.2)
                cos_deriv_label.shift(DOWN*0.2)
        
        
                self.play(Create(cos_graph), Write(cos_label))
                self.wait(1)
                self.play(TransformMatchingTex(cos_label.copy(), cos_deriv_label))
        
        
                # Funcția tangentă
                tan_graph = FunctionGraph(lambda x: np.tan(x), color=BLUE, x_range=[-PI, PI])
                tan_label = MathTex(r"h(x) = \tan(x)", color=WHITE)
                tan_deriv_label = MathTex(r"h'(x) = \sec^2(x)", color=GREEN)
                tan_group = VGroup(tan_graph, tan_label, tan_deriv_label)
                tan_group.arrange(DOWN, buff=0.5).next_to(cos_group, RIGHT, buff=2)
                tan_label.shift(UP*0.2)
                tan_deriv_label.shift(DOWN*0.2)
        
        
                self.play(Create(tan_graph), Write(tan_label))
                self.wait(1)
                self.play(TransformMatchingTex(tan_label.copy(), tan_deriv_label))
                self.wait(2)
