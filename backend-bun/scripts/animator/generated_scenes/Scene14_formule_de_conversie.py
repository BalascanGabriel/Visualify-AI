from manim import *

class Scene14_formule_de_conversie(Scene):
    def construct(self):
        from manim import *
        
        class FormuleConversie(Scene):
            def construct(self):
                # Titlu
                title = Text("Formule de Conversie", color=BLUE, font_size=36)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Text("Conversia unităților de măsură este esențială în multe domenii.", color=WHITE, font_size=24)
                explanation.to_edge(LEFT).shift(UP*0.5)
                self.play(FadeIn(explanation))
        
                # Exemplul 1: Centimetri in Metri
                cm_to_m = MathTex("1 \\text{ cm} = 10^{-2} \\text{ m}", color=YELLOW)
                cm_to_m.next_to(explanation, RIGHT, buff=1)
                self.play(Write(cm_to_m))
        
                # Animație pentru conversie cm->m
                ruler = Line(start=ORIGIN, end=RIGHT*5)
                ruler.next_to(cm_to_m, DOWN)
                cm_marker = Line(start=ORIGIN, end=UP*0.5).next_to(ruler, UP)
                m_marker = Line(start=ORIGIN, end=UP*0.5).next_to(ruler, UP).shift(RIGHT*5*0.01)
        
                self.play(Create(ruler), Create(cm_marker))
                self.play(cm_marker.animate.shift(RIGHT*5*0.01))
                self.play(Transform(cm_marker, m_marker))
                self.wait(1)
        
                # Exemplul 2: Grade Celsius in Grade Fahrenheit
                c_to_f = MathTex("\\text{degreeF} = \\frac{9}{5} \\text{degreeC} + 32", color=GREEN)
                c_to_f.next_to(cm_to_m, DOWN, buff=1)
                self.play(Write(c_to_f))
        
                # Animație simplă pentru a sublinia transformarea
                temp_rect = SurroundingRectangle(c_to_f, color=GREEN)
                self.play(Create(temp_rect))
                self.play(Uncreate(temp_rect))
        
                # Exemplul 3: Kilometri in Mile
                km_to_miles = MathTex("1 \\text{ km} \\approx 0.621 \\text{ miles}", color=RED)
                km_to_miles.next_to(c_to_f, DOWN, buff=1)
                self.play(Write(km_to_miles))
        
                # Animație simplă de fading out
                self.play(FadeOut(explanation), FadeOut(cm_to_m), FadeOut(ruler), FadeOut(m_marker))
                self.wait(1)
        
                #Concluzie
                conclusion = Text("Aplicarea corectă a formulelor asigură acuratețea calculelor.", color=WHITE, font_size=24)
                conclusion.to_edge(DOWN)
                self.play(Write(conclusion))
                self.wait(2)
