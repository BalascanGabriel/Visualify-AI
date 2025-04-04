from manim import *

class Scene17_revolutii_complete_si_fractiuni_ale_acestora(Scene):
    def construct(self):
        from manim import *
        
        class RevolutiiComplete(Scene):
            def construct(self):
                # Titlu
                title = Text("Revoluții complete și fracțiuni ale acestora", color=BLUE, font_size=30)
                title.to_edge(UP)
                self.play(Write(title))
        
                # Text explicativ
                explanation = Tex(r"O revoluție completă reprezintă o rotație de $360^\circ$ sau $2\pi$ radiani.", color=WHITE, font_size=24)
                explanation.to_edge(LEFT).shift(UP*0.5)
                self.play(FadeIn(explanation))
        
                # Cerc pentru animație
                circle = Circle(radius=1, color=YELLOW)
                circle.move_to(ORIGIN)
        
                # Punct pe cerc
                dot = Dot(color=RED)
                dot.move_to(circle.get_right())
        
                # Animație revoluție completă
                self.play(Create(circle))
                self.play(Create(dot))
                self.play(Rotate(dot, 2*PI, about_point=ORIGIN), run_time=2)
        
                # Text pentru revoluție completă
                full_rotation = Tex(r"$2\pi$ radiani", color=GREEN, font_size=24)
                full_rotation.next_to(circle, DOWN)
                self.play(Write(full_rotation))
        
                # Animație fracțiune de revoluție
                self.wait(1)
                self.play(Rotate(dot, PI/2, about_point=ORIGIN), run_time=1)
        
                # Text pentru fracțiune de revoluție
                fractional_rotation = Tex(r"$\frac{\pi}{2}$ radiani", color=GREEN, font_size=24)
                fractional_rotation.next_to(circle, DOWN)
                fractional_rotation.align_to(full_rotation, LEFT)
                self.play(Transform(full_rotation, fractional_rotation))
        
        
                # Adăugare explicație fracțiune
                explanation2 = Tex(r"O fracțiune de revoluție este o rotație mai mică de $2\pi$ radiani.", color=WHITE, font_size=24)
                explanation2.next_to(explanation, DOWN)
                self.play(FadeIn(explanation2))
        
        
                self.wait(2)
