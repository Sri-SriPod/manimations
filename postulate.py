from manim import *


class Postulate(Scene):
    def construct(self):
        introt = Text("Euclid's 5th Postulate").shift(UP * 2)
        postulatetext1 = Tex(r"That, if a straight line falling on two straight lines,", " make the interior angles on the same side less than two right angles, " ,
                             "the two straight lines, if produced indefinitely, meet, on that side on which are the angles less than two right angles.").scale(0.7)
        rect = SurroundingRectangle(postulatetext1)
        group1 = VGroup(rect, postulatetext1)
        self.play(Create(introt))
        self.wait(1)
        self.play(Write(postulatetext1), run_time=7)
        self.wait(1)
        self.remove(introt)
        self.play(Create(rect))
        self.play(group1.animate.shift(UP * 2))
        yeet = postulatetext1.set_color_by_tex("That, if a straight line falling on two straight lines", BLUE)
        self.play(TransformMatchingTex(postulatetext1, yeet))
        yeet2 = postulatetext1.set_color_by_tex("make the interior angles on the same side less than two right angles", BLUE)
        yeet2 = yeet2.set_color_by_tex("That, if a straight line falling on two straight lines", WHITE)
        self.play(TransformMatchingTex(yeet, yeet2))
        yeet3 = postulatetext1.set_color_by_tex("the two straight lines, if produced indefinitely, meet, on that side on which are the angles less than two right angles", BLUE)
        yeet3 = yeet2.set_color_by_tex("make the interior angles on the same side less than two right angles", WHITE)
        self.play(TransformMatchingTex(yeet2, yeet3))
        self.wait(1)


class Graphings(Scene):
    def construct(self):
        plane = NumberPlane(
            axis_config={
                "label_direction": DL - (3 * LEFT / 4)
            },
            y_axis_config={
                "label_direction": DL
            },
            faded_line_ratio=2
        )
        plane.add_coordinates()
        self.add(plane)
        graph = plane.plot(lambda x: (x * (-1/6)) + 1/5 , x_range=[-6, 6], use_smoothing=False, color=RED)
        graph2 = plane.plot(lambda x: 0.2 * x - 2.3, x_range=[-6, 5], use_smoothing=False, color=BLUE)
        graph3 = plane.plot(lambda x: (4.467*x) + 0.2, x_range=[-6, 7], use_smoothing=False, color=GREEN)
        angle_func = lambda curve1, curve2: \
            Angle(TangentLine(curve1, alpha = (0.5)),
                  TangentLine(curve2, alpha = 0.5), quadrant=[-1, 1], color=YELLOW)
        angle = angle_func(graph3, graph)
        angle_label = MathTex(r"\alpha", color=YELLOW).next_to(angle).shift(DOWN*0.3, LEFT*0.2)
        self.play(Create(graph))
        self.play(Create(graph2))
        self.play(Create(graph3))
        self.play(Create(angle), Create(angle_label))
        angle_func2 = lambda curve1, curve2: \
            Angle(TangentLine(curve1, alpha=(0.5)),
                  TangentLine(curve2, alpha=0.5), color=RED)
        angle2 = angle_func2(graph2, graph3)
        angle_label2 = MathTex(r"\beta", color=RED).next_to(angle2)
        self.play(Create(angle2), Create(angle_label2))
        self.wait(2)
        groupalpha = VGroup(angle, angle_label)
        groupbeta = VGroup(angle2, angle_label2)
        groupalpha1 = MathTex(r'\angle \alpha', color=YELLOW)
        groupbeta1 = MathTex(r'+ \angle \beta', r'< 180^\circ', color=RED)
        groupbeta1.set_color_by_tex('< 180^\circ', WHITE)
        self.play(ReplacementTransform(groupalpha.copy(), groupalpha1.shift(UP*2, RIGHT*2)))
        self.play(ReplacementTransform(groupbeta.copy(), groupbeta1.next_to(groupalpha1)))
        graph1_1 = plane.plot(lambda x: (x * (-1 / 6)) + 1 / 5, x_range=[6, 7], use_smoothing=False, color=RED)
        graph2_2 = plane.plot(lambda x: 0.2 * x - 2.3, x_range=[5, 7], use_smoothing=False, color=BLUE)
        self.play(Create(graph1_1))
        self.play(Create(graph2_2))


#  manim -pqh postulate.py
