from manim import *

class Introduction(Scene):
    def construct(self):
        # Title
        title = Text("Introduction to Electromagnetism", color=BLUE).scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Concept 1: Physical Theories
        theory_text = Text("Theories: Models of Nature", color=GREEN).scale(0.7)
        self.play(Write(theory_text))
        self.wait(1)
        self.play(FadeOut(theory_text))

        # Concept 2: Mathematics
        math_text = Text("Mathematics: Abstract Tool for Reasoning", color=YELLOW).scale(0.7)
        self.play(Write(math_text))
        self.wait(1)
        self.play(FadeOut(math_text))

        # Concept 3: Measurement
        measurement_text = Text("Measurement: Associating Properties with Numbers", color=ORANGE).scale(0.7)
        self.play(Write(measurement_text))
        self.wait(1)
        self.play(FadeOut(measurement_text))

        # Concept 4: Physical Quantities
        quantity_text = Text("Physical Quantities: Primitive and Derived", color=PURPLE).scale(0.7)
        self.play(Write(quantity_text))
        self.wait(1)
        self.play(FadeOut(quantity_text))
        
        # Formula 1: Velocity
        velocity_formula = MathTex(r"v = \frac{ds}{dt}", color=RED)
        self.play(Write(velocity_formula))
        self.wait(2)
        self.play(FadeOut(velocity_formula))

        # Concept 5: Laws and Theorems
        laws_text = Text("Laws: Inductively Established Connections", color=TEAL).scale(0.7)
        theorems_text = Text("Theorems: Deductively Derived Connections", color=PINK).scale(0.7)
        self.play(Write(laws_text))
        self.play(Write(theorems_text))
        self.wait(1)
        self.play(FadeOut(laws_text))
        self.play(FadeOut(theorems_text))

        # Concept 6: Multiple Theories
        multiple_theories_text = Text("Multiple Theories for a Domain", color=GOLD).scale(0.7)
        self.play(Write(multiple_theories_text))
        self.wait(1)
        self.play(FadeOut(multiple_theories_text))

        self.wait(1)

class ElectricField(Scene):
    def construct(self):
        #Point P0 with Field E0
        point_P0 = Dot([-3, 0, 0], color=RED)
        label_P0 = MathTex("P_0", color=RED).next_to(point_P0, DOWN)
        field_E0 = Arrow([-4, 0, 0], [-3, 0, 0], color=BLUE)
        label_E0 = MathTex("E_0", color=BLUE).next_to(field_E0, UP)
        force_F0 = Arrow([-4, 0.5, 0], [-3, 0.5, 0], color=GREEN)
        label_F0 = MathTex("F_0", color=GREEN).next_to(force_F0, UP)

        #Point P with Field E
        point_P = Dot([3, 0, 0], color=RED)
        label_P = MathTex("P", color=RED).next_to(point_P, DOWN)
        field_E = Arrow([2, 0, 0], [3, 0, 0], color=BLUE)
        label_E = MathTex("E", color=BLUE).next_to(field_E, UP)
        force_F = Arrow([2, 0.5, 0], [3, 0.5, 0], color=GREEN)
        label_F = MathTex("F", color=GREEN).next_to(force_F, UP)
        
        self.play(Create(point_P0), Write(label_P0), Create(field_E0), Write(label_E0), Create(force_F0), Write(label_F0))
        self.play(Create(point_P), Write(label_P), Create(field_E), Write(label_E), Create(force_F), Write(label_F))
        self.wait(1)

        #Formula for E
        formula_E = MathTex("E = \\frac{F}{F_0}E_0", color=BLACK).to_edge(DOWN)
        self.play(Write(formula_E))
        self.wait(2)
        self.play(FadeOut(point_P0), FadeOut(label_P0), FadeOut(field_E0), FadeOut(label_E0), FadeOut(force_F0), FadeOut(label_F0))
        self.play(FadeOut(point_P), FadeOut(label_P), FadeOut(field_E), FadeOut(label_E), FadeOut(force_F), FadeOut(label_F), FadeOut(formula_E))
        self.wait(1)

class ElectricCharge(Scene):
    def construct(self):
        #Electric Field E
        field_E = Arrow([-4, 0, 0], [-2, 0, 0], color=BLUE)
        label_E = MathTex("E", color=BLUE).next_to(field_E, UP)

        #Charged particle
        charged_particle = Dot([-2, 0, 0], color=YELLOW)
        label_particle = Text("Charged Particle", color=YELLOW).next_to(charged_particle, DOWN)

        #Force on particle
        force_F = Arrow([-2, 0, 0], [-1, 0, 0], color=GREEN)
        label_F = MathTex("F", color=GREEN).next_to(force_F, UP)

        #Formula for Force
        formula_F = MathTex("F = qE", color=BLACK).to_edge(DOWN)

        self.play(Create(field_E), Write(label_E))
        self.play(Create(charged_particle), Write(label_particle))
        self.play(Create(force_F), Write(label_F))
        self.play(Write(formula_F))
        self.wait(2)
        self.play(FadeOut(field_E), FadeOut(label_E), FadeOut(charged_particle), FadeOut(label_particle), FadeOut(force_F), FadeOut(label_F), FadeOut(formula_F))
        self.wait(1)

class ChargeDensity(Scene):
    def construct(self):
        #Volume Charge Density
        volume = Circle(radius=2, color=RED)
        label_volume = Text("Volume \\u03A9", color=RED).next_to(volume, UP)

        #Small volume element
        small_volume = Circle(radius=0.5, color=BLUE).move_to([1, 0, 0])
        label_small_volume = MathTex("\\Delta v_k", color=BLUE).next_to(small_volume, DOWN)

        #Formula for charge in volume
        formula_charge = MathTex("\\Delta q_k \\approx \\rho_v \\Delta v_k", color=BLACK).to_edge(DOWN)

        #Summation
        summation = MathTex("\\sum_{k} \\Delta q_k = \\sum_{k} \\rho_v \\Delta v_k", color=BLACK).to_edge(DOWN)
        integral = MathTex("q = \\int_{\\Omega} \\rho_v dv", color=BLACK).to_edge(DOWN)

        self.play(Create(volume), Write(label_volume))
        self.play(Create(small_volume), Write(label_small_volume))
        self.play(Write(formula_charge))
        self.wait(2)
        self.play(Transform(formula_charge, summation))
        self.wait(2)
        self.play(Transform(formula_charge, integral))
        self.wait(2)
        self.play(FadeOut(volume), FadeOut(label_volume), FadeOut(small_volume), FadeOut(label_small_volume), FadeOut(formula_charge))
        self.wait(1)