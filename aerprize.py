from manimlib.imports import *
import numpy as np

class OpeningScene(Scene):
    def construct(self):
        quote_part1 = TextMobject('``Without a standard there is no',
        tex_to_color_map={"no": GREEN}
        )
        quote_part1.to_edge(UP)
        quote_part1.scale(1.20)
        quote_part2 = TextMobject('logical basis for making a decision or taking action."',
        tex_to_color_map={"logical basis": GREEN}
        )
        quote_part2.scale(1.20)
        quote_part2.next_to(quote_part1, DOWN)
        author = TextMobject("- Joseph M. Juran", tex_to_color_map={"- Joseph M. Juran": BLUE})
        author.next_to(quote_part2, DOWN)
        author.shift(3 * RIGHT)

        self.play(FadeInFromDown(quote_part1),
            FadeInFromDown(quote_part2))
        self.wait(2)
        self.play(FadeInFromDown(author))
        self.wait(2)
        self.play(FadeOut(quote_part1),
        FadeOut(quote_part2),
        FadeOut(author))
        
        intro_title = TextMobject("The Atmosphere", tex_to_color_map={"The Atmosphere": GREEN})
        hyrdostatic = TexMobject("{\\partial p \\over \\partial z} = -\\rho \\* g")
        atmosphere = TextMobject("What is the Atmosphere?", tex_to_color_map={"What is the Atmosphere?": GREEN})
        atmosphere.scale(2)
        atmosphere.shift(3 * UP)

        group = VGroup(intro_title, hyrdostatic)
        group.arrange(DOWN)
        group.scale(3.5)

        self.play(
            FadeInFromDown(intro_title),
            run_time=3
        )
        self.play(
            Write(hyrdostatic),
            run_time=3
        )
        self.wait(3)
        self.play(
            Transform(intro_title, atmosphere),
            LaggedStart(*map(FadeOutAndShiftDown, hyrdostatic)),
        )

        # New bit: Graph of atmosphere.
        earth = Sphere()
        earth.set_fill(GREEN, opacity=0.5)
        earth.scale(4)
        earth.shift(4 * DOWN)
        earth_label = TextMobject("Earth", tex_to_color_map={"Earth": BLACK})
        earth_label.scale(2.5)
        earth_label.shift(2.5 * DOWN)

        atmos = Sphere()
        atmos.set_fill(BLUE, opacity=0.1)
        atmos.scale(6)
        atmos.shift(4 * DOWN)
        atmos_label = TextMobject("Atmosphere")
        atmos_label.set_opacity(0.0)
        atmos_label.scale(3)
        atmos_label.shift(UP)
        self.play(
            ApplyPointwiseFunction(
                lambda p: np.array([p[0], ((p[0] * np.tan(np.arccos(p[0] / (p[1] + 4)))) - 4), 0]),
                atmos_label,
                run_time=0.1
            )
        )

        self.add(atmos)
        self.play(ShowCreation(earth), run_time=6)
        self.play(FadeInFromDown(earth_label),
        )
        self.wait(1)
        atmos_label.set_opacity(0.5)
        self.wait(0.1)
        atmos_label.set_opacity(1)
        self.wait(3)
        
        self.play(
            FadeOutAndShiftDown(earth),
            FadeOutAndShiftDown(earth_label),
            LaggedStart(FadeOutAndShiftDown(atmos)),
            LaggedStart(FadeOutAndShiftDown(atmos_label)),
            run_time=2,
        )

class DefineLayers(Scene):
    def construct(self):
        previous_title = TextMobject("What is the Atmosphere?", tex_to_color_map={"What is the Atmosphere?": GREEN})
        previous_title.scale(2)
        previous_title.shift(3 * UP)
        self.add(previous_title)

        title = TextMobject("Layers of the Atmosphere", tex_to_color_map={"Layers of the Atmosphere": GREEN})
        title.scale(2)
        title.shift(3 * UP)
        self.play(
            Transform(previous_title, title),
            run_time=2
        )
        self.wait(2)

        # Bullet Points (literal points)
        bullet_1 = Sphere()
        bullet_1.set_fill(BLUE)
        bullet_1.scale(0.1)
        bullet_2 = bullet_1.copy()
        bullet_3 = bullet_1.copy()
        bullet_4 = bullet_1.copy()
        bullet_5 = bullet_1.copy()

        # Bullet Points
        point_1 = TextMobject(
            "Troposphere (0 - 11 km)",
            tex_to_color_map={" (0 - 11 km)": BLUE}
        )
        point_2 = TextMobject(
            "Stratosphere (11 - 50 km)",
            tex_to_color_map={" (11 - 50 km)": BLUE}
        )
        point_3 = TextMobject(
            "Mesosphere (50 - 96 km)",
            tex_to_color_map={" (50 - 96 km)": BLUE}
        )
        point_4 = TextMobject(
            "Thermosphere (96 - 600 km)",
            tex_to_color_map={" (96 - 600 km)": BLUE}
        )
        point_5 = TextMobject(
            "Exosphere (600+ km)",
            tex_to_color_map={" (600+ km)": BLUE}
        )
        point_1.scale(2)
        point_2.scale(2)
        point_3.scale(2)
        point_4.scale(2)
        point_5.scale(2)

        bullet_1.shift(6 * LEFT + 2 * UP)
        bullet_2.shift(6 * LEFT + 1 * UP)
        bullet_3.shift(6 * LEFT + 0 * UP)
        bullet_4.shift(6 * LEFT + -1 * UP)
        bullet_5.shift(6 * LEFT + -2 * UP)

        point_1.next_to(bullet_1, RIGHT)
        point_2.next_to(bullet_2, RIGHT)
        point_3.next_to(bullet_3, RIGHT)
        point_4.next_to(bullet_4, RIGHT)
        point_5.next_to(bullet_5, RIGHT)

        bulletpoint_1 = VGroup(bullet_1, point_1)
        bulletpoint_2 = VGroup(bullet_2, point_2)
        bulletpoint_3 = VGroup(bullet_3, point_3)
        bulletpoint_4 = VGroup(bullet_4, point_4)
        bulletpoint_5 = VGroup(bullet_5, point_5)

        self.play(
            Write(bulletpoint_1),
            Write(bulletpoint_2),
        )
        self.play(
            Write(bulletpoint_3),
            Write(bulletpoint_4),
        )
        self.play(
            Write(bulletpoint_5),
        )

        self.wait(5)
        self.play(
            FadeOutAndShiftDown(bulletpoint_3),
            FadeOutAndShiftDown(bulletpoint_4),
            FadeOutAndShiftDown(bulletpoint_5),
        )

        self.wait(3)
        self.play(
            FadeOutAndShiftDown(bulletpoint_1),
            FadeOutAndShiftDown(bulletpoint_2),
        )

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

def troposphere(x):
    alt = (x - 288.185) / -0.0065
    
    alt /= 1000
    return alt

def stratosphere(x):
    if x < 228.65:
        alt = (x - 196.65) / 0.001
    else:
        alt = (x - 139.05) / 0.0028
    
    alt /= 1000
    return alt

class Layers(GraphScene):
    CONFIG = {
        "y_max" : 55,
        "y_min" : 0,
        "x_max" : 400,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 100,
        "axes_color" : BLUE,
        "y_labeled_nums" :range(0,55,5),
        "x_labeled_nums" :range(0,400,50),
        "x_axis_label": "Temperature (K)",
        "y_axis_label": "Altitude (km)",
    }
    def construct(self):
        previous_title = TextMobject("Layers of the Atmosphere", tex_to_color_map={"Layers of the Atmosphere": GREEN})
        previous_title.scale(2)
        previous_title.shift(3 * UP)
        self.add(previous_title)
        
        title = TextMobject("Layers of the Atmosphere", tex_to_color_map={"Layers of the Atmosphere": GREEN})
        title.scale(1.25)
        title.shift(3.5 * DOWN)
        self.play(
            Transform(previous_title, title),
            run_time=2
        )
        
        self.setup_axes()
        
        layer_1 = TextMobject("Troposphere", tex_to_color_map={"Troposphere": ORANGE})
        layer_2 = TextMobject("Stratosphere", tex_to_color_map={"Stratosphere": ORANGE})
        layer_1.shift(2 * DOWN + 2 * LEFT)
        layer_2.shift(2 * LEFT)

        trop_graph = self.get_graph(
            troposphere, color=GREEN, x_max=288.185, x_min=216.65,
        )
        strat_graph = self.get_graph(
            stratosphere, color=GREEN, x_min=216.65, x_max=270.65
        )
        troppause_graph = self.get_graph(
            lambda x: 1e10 * x - 2166499999989.0, color=GREEN, x_min=216.65, x_max=216.6500000009
        )

        trop_line = self.get_graph(lambda x : 0 * x + 11, color=WHITE)
        strat_line = self.get_graph(lambda x : 0 * x + 47, color=WHITE)
        draw_tropline = DashedVMobject(trop_line)
        draw_stratline = DashedVMobject(strat_line)

        self.play(
            ShowCreation(trop_graph),
            run_time=10,
        )
        self.play(
            ShowCreation(draw_tropline),
            run_time=4,
        )
        self.play(
            Write(layer_1),
            run_time=3
        )
        self.wait(36)
        self.play(
            ShowCreation(troppause_graph),
            run_time=5
        )
        self.wait(5)
        self.play(
            ShowCreation(strat_graph),
            run_time=10
        )
        self.play(
            ShowCreation(draw_stratline),
            run_time=4,
        )
        self.play(
            Write(layer_2),
            run_time=2,
        )
        self.wait(14)
        self.play(
            FadeOutAndShift(trop_graph),
            FadeOutAndShift(strat_graph),
            FadeOutAndShift(troppause_graph),
            FadeOutAndShift(self.axes),
            FadeOutAndShift(draw_tropline),
            FadeOutAndShift(draw_stratline),
            FadeOutAndShift(layer_1),
            FadeOutAndShift(layer_2),
        )

class ISA(Scene):
    def construct(self):
        # Previous Title
        previous_title = TextMobject(
            "Layers of the Atmosphere", tex_to_color_map={"Layers of the Atmosphere": GREEN}
        )
        previous_title.scale(1.25)
        previous_title.shift(3.5 * DOWN)
        self.add(previous_title)

        # Title
        title = TextMobject(
            "International Standard Atmosphere", 
            tex_to_color_map={"International Standard Atmosphere": GREEN}
        )
        title.scale(1.75)
        title.shift(3 * UP)

        self.play(
            Transform(previous_title, title)
        )
        self.wait(3)

        # Bullet Points (literal points)
        bullet_1 = Sphere()
        bullet_1.set_fill(BLUE)
        bullet_1.scale(0.1)
        bullet_2 = bullet_1.copy()
        bullet_3 = bullet_1.copy()
        bullet_4 = bullet_1.copy()
        bullet_4.set_opacity(0)
        bullet_5 = bullet_1.copy()

        # Bullet Points
        point_1 = TextMobject(
            "Used to represent an average atmosphere",
            tex_to_color_map={"average atmosphere": BLUE}
        )
        point_2 = TextMobject(
            "Defined as a static atmospheric model",
            tex_to_color_map={"static atmospheric model": BLUE}
        )
        point_3 = TextMobject(
            "Assumes a linear distribution of temperature",
            tex_to_color_map={
                "linear distribution": BLUE,
                "temperature": BLUE
            }
        )
        point_4 = TextMobject("against altitude")
        point_5 = TextMobject(
            "Established as a common reference for temperature",
            tex_to_color_map={"temperature": BLUE}
        )

        bullet_1.shift(6 * LEFT + 2 * UP)
        bullet_2.shift(6 * LEFT + 1 * UP)
        bullet_3.shift(6 * LEFT + -1 * UP)
        bullet_4.shift(6 * LEFT + -1.5 * UP)
        bullet_5.shift(6 * LEFT + -0 * UP)

        point_1.next_to(bullet_1, RIGHT)
        point_2.next_to(bullet_2, RIGHT)
        point_3.next_to(bullet_3, RIGHT)
        point_4.next_to(bullet_4, RIGHT)
        point_5.next_to(bullet_5, RIGHT)

        bulletpoint_1 = VGroup(bullet_1, point_1)
        bulletpoint_2 = VGroup(bullet_2, point_2)
        bulletpoint_3 = VGroup(bullet_3, point_3)
        bulletpoint_4 = VGroup(bullet_4, point_4)
        bulletpoint_5 = VGroup(bullet_5, point_5)

        self.play(
            FadeInFromDown(bulletpoint_1),
        )
        self.wait(2)

        self.play(
            FadeInFromDown(bulletpoint_2),
        )
        self.wait(9)

        self.play(
            FadeInFromDown(bulletpoint_5),
        )
        self.wait(6)

        self.play(
            FadeInFromDown(bulletpoint_3),
            FadeInFromDown(bulletpoint_4),
        )
        self.wait(14)

        self.play(
            FadeOutAndShiftDown(bulletpoint_1),
            FadeOutAndShiftDown(bulletpoint_2),
            FadeOutAndShiftDown(bulletpoint_3),
            FadeOutAndShiftDown(bulletpoint_4),
            FadeOutAndShiftDown(bulletpoint_5),
        )

class Derive_ISA_I(Scene):
    def construct(self):
        # Previous Title
        previous_title = TextMobject(
            "International Standard Atmosphere", 
            tex_to_color_map={"International Standard Atmosphere": GREEN}
        )
        previous_title.scale(1.75)
        previous_title.shift(3 * UP)
        self.add(previous_title)

        # Title
        title_of_scene = TextMobject(
            "Derivation of the Barometric Formula for Pressure", 
            tex_to_color_map={"Derivation": GREEN, "Barometric Formula for Pressure": BLUE},
        )
        title_of_scene.scale(1.25)
        title_of_scene.shift(3 * UP)

        self.play(
            Transform(previous_title, title_of_scene)
        )

        # Ideal Gas Law part.
        ideal = TexMobject("pV = n R T")

        n = TexMobject("n = {m \\over M}")
        part_1 = TexMobject("\\therefore pV = {m \\over M} R T")
        part_2 = TexMobject("\Rightarrow p = {m \\over V M} R T")
        part_3 = TexMobject("\Rightarrow p = {m \\over V} {1 \\over M} R T")
        part_4 = TexMobject("\Rightarrow p = {\\rho \\over M} R T")
        part_5 = TexMobject("\Rightarrow {p \\over R T} = {\\rho \\over M}")
        part_6 = TexMobject("\Rightarrow {p M \\over R T} = \\rho")

        # Hydrostatic Balance Part.
        hyrdostatic = TexMobject("{\\partial p \\over \\partial z} = -\\rho g")
        part_A = TexMobject("\Rightarrow {\\Delta p \\over \\Delta z} = -\\rho g")

        left = VGroup(ideal, n, part_1, part_2, part_3)
        left.arrange(DOWN)
        left.shift(3 * LEFT + 0.5 * DOWN)
        right = VGroup(part_4, part_5, part_6, hyrdostatic, part_A)
        right.arrange(DOWN)
        right.shift(3 * RIGHT + 0.5 * DOWN)

        self.play(
            Write(left),
            run_time=2,
        )
        self.wait(0.5)
        self.play(
            Write(right),
            run_time=2,
        )
        self.wait(1)
        self.play(
            FadeOut(left),
            FadeOut(right),
        )

class Derive_ISA_II(Scene):
    def construct(self):
        # Title
        title_of_scene = TextMobject(
            "Derivation of the Barometric Formula for Pressure", 
            tex_to_color_map={"Derivation": GREEN, "Barometric Formula for Pressure": BLUE},
        )
        title_of_scene.scale(1.25)
        title_of_scene.shift(3 * UP)
        self.add(title_of_scene)

        part_B = TexMobject("\Rightarrow \\Delta p = -\\rho g \\Delta z")
        part_C = TexMobject("\\therefore \\Delta p = -{p M \\over R T} g \\Delta z")
        part_D = TexMobject("\Rightarrow {\\Delta p \\over p} = -{M g \\over R T} \\Delta z")
        part_E = TexMobject(
            "\\lim_{\\Delta p \\to 0} and \\lim_{\\Delta z \\to 0}",
        )
        part_F = TexMobject("\\therefore {\\partial p \\over p} = -{M g \\over R T} \\partial z")

        # Integration Part
        part_alpha = TexMobject("\\int {\\partial p \\over p} = - \\int {M g \\over R T} \\partial z")
        part_beta = TexMobject("\Rightarrow \\ln p = -{M g \\over R T} z + \\ln{C}")
        part_gamma = TexMobject("\Rightarrow \\ln p - \\ln C = -{M g \\over R T} z")

        left = VGroup(part_B, part_C, part_D, part_E)
        left.arrange(DOWN)
        left.shift(3 * LEFT)

        right = VGroup(part_F, part_alpha, part_beta, part_gamma)
        right.arrange(DOWN)
        right.shift(3 * RIGHT)

        self.play(
            Write(left),
            run_time=2,
        )
        self.wait(0.5)
        self.play(
            Write(right),
            run_time=2,
        )
        self.wait(1)
        self.play(
            FadeOut(left),
            FadeOut(right),
        )

class Derive_ISA_III(Scene):
        def construct(self):
            # Title
            title_of_scene = TextMobject(
                "Derivation of the Barometric Formula for Pressure", 
                tex_to_color_map={"Derivation": GREEN, "Barometric Formula for Pressure": BLUE},
            )
            title_of_scene.scale(1.25)
            title_of_scene.shift(3 * UP)

            # Continue
            part_delta = TexMobject("\Rightarrow \\ln {p \\over C} = -{M g \\over R T} z")
            part_epsilon = TexMobject("a^x = y \\iff log_a y = x")
            part_zeta = TexMobject("\\therefore {p \\over C} = \\exp -{M g \\over R T} z")
            part_iota = TexMobject("\\Rightarrow p = C \\exp (-{M g \\over R T} z)")
            part_kappa = TexMobject("p(z=0) = p_0")
            part_lambda = TexMobject("\\therefore p = p_0 \\exp (-{M g \\over R T} z)")
            text_1 = TextMobject(
                "The constant of integration C can be determined",
                tex_to_color_map={"C": GREEN},
            )
            text_2 = TextMobject(
                "from the initial condition, and can be replaced",
                tex_to_color_map={"initial condition": BLUE},
            )
            text_3 = TextMobject(
                "by the average sea level atmospheric pressure",
                tex_to_color_map={"average sea level atmospheric pressure": GREEN},
            )

            left = VGroup(part_delta, part_epsilon, part_zeta)
            left.arrange(DOWN)
            left.shift(3 * LEFT + 0.5 * UP)
            right = VGroup(part_iota, part_kappa, part_lambda)
            right.arrange(DOWN)
            right.shift(3 * RIGHT + 0.5 * UP)
            text = VGroup(text_1, text_2, text_3)
            text.arrange(DOWN)
            text.shift(2.5 * DOWN)
            text.scale(1.10)

            self.add(title_of_scene)
            self.play(
                Write(left),
                run_time=2,
            )
            self.wait(0.5)
            self.play(
                Write(right),
                run_time=2,
            )
            self.wait(0.25)
            self.play(
                Write(text),
                run_time=2.5,
            )
            self.wait(2)
            self.play(
                FadeOut(left),
                FadeOut(right),
                FadeOut(text)
            )

def pressure_to_alt(x):
    x *= 100
    y = np.log(x / 101325) / (-(0.02896 * 9.807) / (8.3143 * 288.15))
    y /= 1000
    return y

class Pressure(GraphScene):
    CONFIG = {
        "y_max" : 55,
        "y_min" : 0,
        "x_max" : 1100,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 100,
        "axes_color" : BLUE,
        "y_labeled_nums" :range(0,55,5),
        "x_labeled_nums" :range(0,1100,100),
        "x_axis_label": "Pressure (hPa)",
        "y_axis_label": "Altitude (km)",
    }
    def construct(self):
        # Previous title
        previous_title = TextMobject(
            "Derivation of the Barometric Formula for Pressure", 
            tex_to_color_map={"Derivation": GREEN, "Barometric Formula for Pressure": BLUE},
        )
        previous_title.scale(1.25)
        previous_title.shift(3 * UP)

        # Title
        title = TextMobject("Atmospheric Pressure", tex_to_color_map={"Atmospheric Pressure": GREEN})
        title.scale(1.25)
        title.shift(3.5 * DOWN)
        self.play(
            Transform(previous_title, title),
            run_time=2
        )
        
        self.setup_axes()
        
        layer_1 = TextMobject("Troposphere", tex_to_color_map={"Troposphere": ORANGE})
        layer_2 = TextMobject("Stratosphere", tex_to_color_map={"Stratosphere": ORANGE})
        layer_1.shift(2 * DOWN + 2 * LEFT)
        layer_2.shift(2 * LEFT)

        pressure = self.get_graph(
            pressure_to_alt, color=GREEN, x_min=2.75, x_max=1000,
        )

        trop_line = self.get_graph(lambda x : 0 * x + 11, color=WHITE)
        strat_line = self.get_graph(lambda x : 0 * x + 47, color=WHITE)
        draw_tropline = DashedVMobject(trop_line)
        draw_stratline = DashedVMobject(strat_line)

        self.play(
            ShowCreation(draw_tropline),
            Write(layer_1),
            run_time=5
        )
        self.play(
            ShowCreation(draw_stratline),
            Write(layer_2),
            run_time=5
        )
        self.play(
            ShowCreationThenDestruction(pressure),
            run_time=25,
        )
        self.wait(2.5)
        self.play(
            FadeOutAndShift(self.axes),
            FadeOutAndShift(draw_tropline),
            FadeOutAndShift(draw_stratline),
            FadeOutAndShift(layer_1),
            FadeOutAndShift(layer_2),
        )

class Appliciations(Scene):
    def construct(self):
        # Previous Title
        previous_title = TextMobject(
            "Atmospheric Pressure", tex_to_color_map={"Atmospheric Pressure": GREEN}
        )
        previous_title.scale(1.25)
        previous_title.shift(3.5 * DOWN)
        self.add(previous_title)

        # Title
        title = TextMobject(
            "Appliciations", 
            tex_to_color_map={"Appliciations": GREEN}
        )
        title.scale(2)
        title.shift(3 * UP)

        self.play(
            Transform(previous_title, title)
        )
        self.wait(6)

        # Bullet Points (literal points)
        bullet_1 = Sphere()
        bullet_1.set_fill(BLUE)
        bullet_1.scale(0.1)
        bullet_2 = bullet_1.copy()
        bullet_3 = bullet_1.copy()
        bullet_4 = bullet_1.copy()
        bullet_4.set_opacity(0)
        bullet_5 = bullet_1.copy()
        bullet_5.set_opacity(0)
        bullet_6 = bullet_1.copy()
        bullet_7 = bullet_1.copy()
        bullet_7.set_opacity(0)

        # Bullet Points
        point_1 = TextMobject(
            "Aviation standards and flying rules are based on the ISA",
            tex_to_color_map={
                "Aviation standards": BLUE,
                "flying rules": BLUE,
                "based on the ISA": BLUE
            }
        )
        point_2 = TextMobject(
            "Allows for a reproducible engineering reference",
            tex_to_color_map={"reproducible engineering reference": BLUE}
        )
        point_3 = TextMobject(
            "Density altitude is used to assess an aircraft's",
            tex_to_color_map={
                "Density altitude": BLUE,
                "aircraft's aerodynamic": BLUE
            }
        )
        point_4 = TextMobject(
            "aerodynamic performance under certain weather",
            tex_to_color_map={
                "aerodynamic performance": BLUE,
                "certain weather conditions": BLUE
            }
        )
        point_5 = TextMobject("conditions", tex_to_color_map={"conditions": BLUE,})
        point_6 = TextMobject(
            "Power delivered by the aircraft's engine is affected by",
            tex_to_color_map={
                "Power delivered": BLUE,
                "aircraft's engine": BLUE,
                "affected by": BLUE
            }
        )
        point_7 = TextMobject(
            "by the density and composition of the atmosphere",
            tex_to_color_map={
                "density": BLUE,
                "composition of": BLUE,
                "atmosphere": BLUE
            }
        )

        bullet_1.shift(6 * LEFT + 2 * UP)
        bullet_2.shift(6 * LEFT + 1 * UP)
        bullet_3.shift(6 * LEFT + 0 * UP)
        bullet_4.shift(6 * LEFT + -0.5 * UP)
        bullet_5.shift(6 * LEFT + -1 * UP)
        bullet_6.shift(6 * LEFT + -2 * UP)
        bullet_7.shift(6 * LEFT + -2.5 * UP)

        point_1.next_to(bullet_1, RIGHT)
        point_2.next_to(bullet_2, RIGHT)
        point_3.next_to(bullet_3, RIGHT)
        point_4.next_to(bullet_4, RIGHT)
        point_5.next_to(bullet_5, RIGHT)
        point_6.next_to(bullet_6, RIGHT)
        point_7.next_to(bullet_7, RIGHT)

        bulletpoint_1 = VGroup(bullet_1, point_1)
        bulletpoint_2 = VGroup(bullet_2, point_2)
        bulletpoint_3 = VGroup(bullet_3, point_3)
        bulletpoint_4 = VGroup(bullet_4, point_4)
        bulletpoint_5 = VGroup(bullet_5, point_5)
        bulletpoint_6 = VGroup(bullet_6, point_6)
        bulletpoint_7 = VGroup(bullet_7, point_7)

        self.play(
            FadeInFromDown(bulletpoint_1),
        )
        self.wait(14)

        self.play(
            FadeInFromDown(bulletpoint_2),
        )
        self.wait(5)

        self.play(
            FadeInFromDown(bulletpoint_3),
            FadeInFromDown(bulletpoint_4),
            FadeInFromDown(bulletpoint_5),
        )
        self.wait(16)

        self.play(
            FadeInFromDown(bulletpoint_6),
            FadeInFromDown(bulletpoint_7),
        )
        self.wait(2)

        self.play(
            FadeOutAndShiftDown(bulletpoint_1),
            FadeOutAndShiftDown(bulletpoint_2),
            FadeOutAndShiftDown(bulletpoint_3),
            FadeOutAndShiftDown(bulletpoint_4),
            FadeOutAndShiftDown(bulletpoint_5),
            FadeOutAndShiftDown(bulletpoint_6),
            FadeOutAndShiftDown(bulletpoint_7),
        )

class ClosingScene(Scene):
    def construct(self):
        # Previous Title
        previous_title = TextMobject(
            "Appliciations", 
            tex_to_color_map={"Appliciations": GREEN}
        )
        previous_title.scale(2)
        previous_title.shift(3 * UP)
        self.add(previous_title)

        # Thanks
        thanks = TextMobject(
            "Thanks for Watching!",
            tex_to_color_map={"Thanks for Watching!": ORANGE}
        )
        thanks.scale(2.5)
        thanks.shift(UP)
        
        self.play(
            Transform(previous_title, thanks),
            run_time=2
        )

        for i in range(26):
            i = 26 - (i + 1)
            time_left = TextMobject(str(i), tex_to_color_map={str(i): BLUE})
            time_left.shift(DOWN)
            time_left.scale(2)

            if i == 0:
                time_left.set_opacity(0)

            self.play(
                Write(time_left)
            )
            self.remove(time_left) 
