from manim import *



class Intro(Scene):
    def construct(self):
        banner = ManimBanner()
        self.play(banner.create())
        self.wait(1)


class Definition(Scene):
    def construct(self):
        rd = MathTex(r'0.3333...')
        rd2 = MathTex(r'0.\overline{3}')
        rd3 = MathTex(r'0.2\overline{18}')
        xn = MathTex(r'x_n:=').shift(DOWN, LEFT * 2)
        rdef = MathTex(r'\sum^{n}', r'_{i=1}', r'3\cdot10', r'^{-i}').shift(DOWN, LEFT * 0.9)
        rdefedit = MathTex(r'\sum^{\infty}', r'_{i=1}', r'3\cdot10', r'^{-i}').shift(DOWN, LEFT * 0.9)
        rdefeditshift = MathTex(r'\sum^{\infty}', r'_{i=1}', r'3\cdot10', r'^{-i}').shift(DOWN, LEFT)
        equalsign = MathTex(r'=').shift(DOWN, RIGHT * 0.5)
        rdef2 = MathTex(r"3\cdot10^{-1}").shift(DOWN, LEFT * 0.9, RIGHT * 2.5)
        rdef2edit = MathTex(r"3\cdot\frac{1}{10}").shift(DOWN, LEFT * 0.9, RIGHT * 2.5)
        rdef2edit2 = MathTex(r"\frac{3}{10}").shift(DOWN, LEFT * 0.9, RIGHT * 2.5)
        rdef3 = MathTex(r"3\cdot10^{-2}").shift(DOWN, RIGHT*3)
        rdef3edit = MathTex(r"\frac{3}{100}").shift(DOWN, RIGHT*2.5)
        plus = MathTex(r'+')
        so_on = MathTex(r'+... = ?')
        other = MathTex(r'x_n:= 0.2 + \sum^{\infty}_{i=1}1.8 \times 100^{-i}')
        fractions = MathTex(r'\frac{2}{10} + \frac{18}{1000} + \frac{18}{100000} + ... = ?')
        group = VGroup(xn,
                       rdefeditshift.set_color_by_tex("-i", BLUE).set_color_by_tex("i=1", BLUE),
                       equalsign,
                       rdef2edit2,
                       plus.next_to(rdef2edit2),
                       rdef3edit,
                       so_on
                       )
        self.play(Write(rd))
        self.play(TransformMatchingTex(rd, rd2))
        self.play(ApplyMethod(rd2.shift, UP))
        self.play(Write(xn))
        self.play(ApplyMethod(xn.shift, LEFT))
        self.add(rdef)
        self.play(Write(rdef))
        self.play(TransformMatchingTex(rdef, rdefedit))
        self.play(Write(equalsign))
        self.play(Indicate(rdefedit[1]))
        self.play(Indicate(rdefedit[3]))
        self.play(TransformMatchingTex(rdefedit, rdefedit.set_color_by_tex("-i", BLUE).set_color_by_tex("i=1", BLUE)))
        self.play(ReplacementTransform(rdefedit.copy().shift(RIGHT * 3), rdef2))
        self.play(ReplacementTransform(rdef2, rdef2edit))
        self.play(ReplacementTransform(rdef2edit, rdef2edit2))
        self.play(ApplyMethod(rdef2edit2.shift, LEFT * 0.5))
        self.play(Write(plus.next_to(rdef2edit2)))
        self.play(ReplacementTransform(rdefedit.copy().shift(RIGHT * 4), rdef3))
        self.play(ReplacementTransform(rdef3, rdef3edit))
        self.play(Write(so_on.next_to(rdef3edit)))
        self.remove(rdefedit)
        self.play(group.animate.to_corner(UL))
        self.play(Write(other.shift(DOWN*2)))
        self.play(TransformMatchingTex(rd2, rd3))
        self.play(ApplyMethod(other.shift, LEFT*4))
        self.play(Write(equalsign.next_to(other)))
        self.play(Write(fractions.next_to(equalsign)))

class Geometric(Scene):
    def construct(self):
        introtext = Text('Geometric Sequences', font="Times New Roman")
        explatext = Text('- Each term is the previous term multiplied by a common ratio').scale(0.5).shift(2 * UP)
        examplesequence = MathTex(r'2, 4').shift(UP, LEFT * 1.2)
        r2text = MathTex(r'4, 8').shift(UP, LEFT * 0.3)
        r3text = MathTex(r'e, e').shift(UP, RIGHT * 0.5)
        examplesequence2 = MathTex(r'2, 4, 8, 16, 32').shift(UP, LEFT * 0.3)
        r = BraceText(examplesequence, 'x2')
        r2 = BraceText(r2text, 'x2')
        r3 = BraceText(r3text, 'x2')
        geosequence = MathTex(r'a, ar, ar^2, ar^3, ar^4...').shift(DOWN)
        last_term = MathTex(r'a, ar, ar^2, ar^3, ar^{n-1}...').shift(DOWN)
        last_term2 = MathTex(r'a, ar, ar^2, ar^3, ar^{5-1}...').shift(DOWN)
        terminology = Text('a = first term').scale(0.5).shift(DOWN * 2)
        terminology2 = Text('r = common ratio').scale(0.5).shift(DOWN * 2.5)
        self.play(Write(introtext))
        self.play(ApplyMethod(introtext.shift, 3 * UP))
        self.play(Write(explatext))
        self.play(Write(examplesequence2))
        self.play(Create(r))
        self.play(Create(r2))
        self.play(Create(r3))
        self.play(Write(geosequence))
        self.play(Write(terminology))
        self.play(Write(terminology2))
        self.play(Transform(geosequence, last_term))
        self.play(ReplacementTransform(last_term, last_term2))
        self.play(ReplacementTransform(last_term2, geosequence))

class SumGeo(Scene):
    def construct(self):
        geosequence = MathTex(r'a, ar, ar^2, ar^3, ar^4...').shift(DOWN)
        terminology = Text('a = first term').scale(0.5).shift(DOWN * 2)
        terminology2 = Text('r = common ratio').scale(0.5).shift(DOWN * 2.5)
        geogroup = VGroup(geosequence,
                          terminology, terminology2)
        rect = SurroundingRectangle(geogroup)
        geogroup2 = VGroup(rect, geosequence,
                          terminology, terminology2)
        self.add(geogroup)
        self.play(Create(rect))
        self.play(geogroup2.animate.shift(UP*4))
        self.play(geogroup2.animate.scale(0.8))
        exp_property = MathTex(r'a^m\cdot a^n = a^{m+n}').shift(DOWN*3, RIGHT*4)
        S_n = MathTex(r'S_n =', r'a',r'+',r'ar',r'+', r'ar^2', r'+', r'ar^3', r'+...+', r'ar^{n-3}',r'+',r'ar^{n-2}',r'+',r'ar^{n-1}').shift(UR)
        onlyS_n = MathTex(r'S_n').shift(UP, LEFT*4.5)
        rS_n = MathTex(r'rS_n = r(a+ar+ar^2+ar^3+...+ar^{n-3}+ar^{n-2}+ar^{n-1})').shift(UR, DOWN, LEFT*0.5)
        rS_n2 = MathTex(r'rS_n = ar^{0+1} + ar^{1+1} + ar^{2+1} + ar^{3+1} + ... + ar^{n-3+1} + ar^{n-2+1} + ar^{n-1+1}').shift(UP,DOWN).scale(0.8)
        rS_n3 = MathTex(r'rS_n =', r'ar' r'+', r'ar^{2}', r'+', r'ar^{3}', r'+', r'ar^4', r'+ ...+', r'ar^{n-2}', r'+', r'ar^{n-1}', r'+', r'ar^{n}').shift(UP,DOWN)
        rS_n3edit = MathTex(r'rS_n = ', r'ar', r'+', r'ar^{2}', r'+', r'ar^{3}', r'+ ...+', r'ar^{n-3}', '+', r'ar^{n-2}', r'+', r'ar^{n-1}', r'+', r'ar^{n})').shift(UP, DOWN, RIGHT*0.9).scale(0.9)
        r_Sn4 = MathTex(r'-rS_n = -(', r'ar', r'+', r'ar^{2}', r'+', r'ar^{3}', r'+ ...+', r'ar^{n-3}', '+', r'ar^{n-2}', r'+', r'ar^{n-1}', r'+', r'ar^{n})').shift(UP, DOWN, RIGHT*0.9).scale(0.9)
        negrS_n = MathTex(r'-rS_n').shift(LEFT*4.3)
        negrS_n1 = MathTex(r'(1-r)').shift(LEFT*3.8, DOWN)
        equalsign = MathTex(r'=').next_to(negrS_n1)
        subtraction = MathTex(r'a-ar^n').next_to(equalsign)
        self.play(Write(S_n))
        self.play(Write(rS_n))
        self.play(Create(exp_property))
        self.play(ReplacementTransform(rS_n, rS_n2))
        self.play(Uncreate(exp_property))
        self.play(ReplacementTransform(rS_n2, rS_n3))
        self.wait(1)
        self.play(ReplacementTransform(rS_n3, rS_n3edit))
        self.wait(1)
        self.play(ReplacementTransform(rS_n3edit, r_Sn4))
        self.wait(1)
        r_Sn4_2 = r_Sn4[1:12]
        everyother = r_Sn4_2[::2]
        rS_n_2 = S_n[3:]
        everyother3 = rS_n_2[::2]
        Equation = VGroup(onlyS_n,
                          negrS_n1,
                          equalsign,
                          subtraction).shift(DL)
        equationedit = MathTex(r'\frac{S_n(1-r)}{1-r} = \frac{a-ar^n}{1-r}').shift(DOWN*3, LEFT*3)
        equationedit1 = MathTex(r'S_n = \frac{(a-ar^n)}{1-r}').shift(DOWN*3, LEFT*3)
        equationedit2 = MathTex(r'S_n = \frac{a(1-r^n)}{1-r}').shift(DOWN*3, LEFT*3)
        condition = MathTex(r'r\neq1').shift(DOWN*2,LEFT*3)
        ifr1 = MathTex(r'S_n = na').shift(RIGHT*2, DOWN*3)
        r1 = MathTex(r'r = 1').shift(RIGHT*2, DOWN*2)
        for i in range(len(everyother3)):
            self.play(Indicate(everyother3[i]))
            self.play(Indicate(everyother[i]))
        self.play(Create(SurroundingRectangle(S_n[1])))
        self.play(Create(SurroundingRectangle(rS_n3edit[13])))
        self.play(onlyS_n.animate.shift(DOWN*2))
        self.play(negrS_n.animate.next_to(onlyS_n))
        self.play(onlyS_n.animate.shift(LEFT*0.5))
        self.play(ReplacementTransform(negrS_n, negrS_n1))
        self.play(Write(equalsign))
        self.play(Write(subtraction))
        self.play(ReplacementTransform(Equation, equationedit))
        self.play(Write(condition))
        self.play(ReplacementTransform(equationedit, equationedit1))
        self.play(ReplacementTransform(equationedit1, equationedit2))
        self.play(Write(ifr1))
        self.play(Write(r1))

class InfiniteGeoSum(Scene):
    def construct(self):
        equationedit2 = MathTex(r'S_n = \frac{a(1-r^n)}{1-r}').shift(DOWN * 3, LEFT * 3)
        condition = MathTex(r'r\neq1').shift(DOWN * 2, LEFT * 3)
        ifr1 = MathTex(r'S_n = na').shift(RIGHT * 2, DOWN * 3)
        r1 = MathTex(r'r = 1').shift(RIGHT * 2, DOWN * 2)
        infogroup = VGroup(equationedit2,
                           condition,
                           ifr1,
                           r1)
        inforectangle = SurroundingRectangle(infogroup)
        infogroup2 = VGroup(equationedit2,
                            condition,
                            ifr1,
                            r1,
                            inforectangle)
        self.add(infogroup2)
        self.play(Create(inforectangle))
        self.play(infogroup2.animate.move_to(UP*3, RIGHT*3).scale(0.7))
        liminfty = MathTex(r'\lim_{n\to\infty}')
        ngeo = MathTex(r'a(1-',r'r^n',r')\over{1-r}').next_to(liminfty)
        equals_zero = MathTex(r'=0')
        rcondition = MathTex(r'-1<r<1')
        self.play(Write(liminfty))
        self.play(Write(ngeo))
        self.remove(ngeo)
        self.play(ngeo[1].animate.scale(3))
        self.play(liminfty.animate.scale(3))
        self.play(Write(equals_zero.next_to(ngeo)))
        self.play(Write(rcondition.next_to(ngeo).shift(DOWN)))

class InfiniteGeoSum2(Scene):
    def construct(self):
        equationedit2 = MathTex(r'S_n = \frac{a(1-r^n)}{1-r}').shift(DOWN * 3, LEFT * 3)
        condition = MathTex(r'r\neq1').shift(DOWN * 2, LEFT * 3)
        ifr1 = MathTex(r'S_n = na').shift(RIGHT * 2, DOWN * 3)
        r1 = MathTex(r'r = 1').shift(RIGHT * 2, DOWN * 2)
        infogroup = VGroup(equationedit2,
                           condition,
                           ifr1,
                           r1)
        inforectangle = SurroundingRectangle(infogroup)
        infogroup2 = VGroup(equationedit2,
                            condition,
                            ifr1,
                            r1,
                            inforectangle).shift(UP*5, LEFT*3).scale(0.7)
        self.add(infogroup2)
        limsumgeo = MathTex(r'\lim_{n\to\infty}\frac{a(1-r^n)}{1-r}')
        infsumgeo = MathTex(r'\frac{a(1-0)}{1-r}')
        infsumgeo2 = MathTex(r'\frac{a}{1-r}')
        infsum = MathTex(r'S_{\infty} = ').shift(LEFT*1.5)
        self.play(Write(limsumgeo))
        self.play(ReplacementTransform(limsumgeo, infsumgeo))
        rcondition2 = MathTex(r', \space -1<r<1')
        self.play(Write(rcondition2.next_to(limsumgeo)))
        self.play(ReplacementTransform(infsumgeo, infsumgeo2))
        self.play(Write(infsum))
        infsumgroup = VGroup(infsum, infsumgeo2, rcondition2)
        rect = SurroundingRectangle(infsumgroup)
        self.play(Create(rect))

class RightTriangle(Scene):
    def construct(self):
        sq = Square(side_length=3).shift(RIGHT * 3.5 + DOWN * 1.5)
        triangle = Polygon([-3, -3, 0], [0, -3, 0], [0, 3, 0]).shift(RIGHT * 5)
        triangle2 = Polygon([-3, -3, 0], [-3, 0, 0], [-1.5, 0, 0], stroke_color=ORANGE).shift(RIGHT * 5)
        orangetriangle = Polygon([-3, -3, 0], [0, -3, 0], [0, 3, 0], stroke_color=GREEN).shift(RIGHT * 5)
        bracelabel_h = BraceLabel(triangle, 'S', RIGHT)
        bracelabel_s = BraceLabel(sq, 'a', LEFT)
        bracelabel_d = BraceLabel(sq, 'a', DOWN)
        tex = MathTex(r'ar').shift(RIGHT * 4.3, UP * 0.2)
        tex2 = MathTex(r'a-ar').shift(RIGHT * 2.7, UP * 0.2)
        text = MathTex(r'ar^2').shift(RIGHT * 4.5, UP * 0.8)
        text2 = MathTex(r'ar^3').shift(RIGHT * 4.6, UP * 1.5)
        START = (3.75, 0, 0)
        END = (5, 0, 0)
        START1 = (4, 0, 0)
        END1 = (5, 0, 0)
        line = Line(START, END).shift(UP * 0.5)
        line2 = Line(START1, END1).shift(UP * 1.1)
        first = MathTex(r'\frac{S}{a} = \frac{a}{a-ar} \\ ').shift(RIGHT * -2, UP * 2)
        second = MathTex(r'S = a(\frac{a}{a-ar})').shift(RIGHT * -2, UP)
        secondedit = MathTex(r'S = \frac{a^2}{a-ar}').shift(RIGHT * -2)
        third = MathTex(r'S = \frac{a^2}{a(1-r)}').shift(RIGHT * -2, DOWN * 2)
        lasttex = MathTex(r'S = \frac{a}{1-r}').shift(RIGHT * -2, DOWN * 2)
        self.play(Create(triangle))
        self.wait(1)
        self.play(Create(sq))
        self.play(Create(bracelabel_s))
        self.play(Create(bracelabel_d))
        self.play(Write(tex))
        self.play(Write(tex2))
        self.play(Create(line))
        self.play(Write(text))
        self.play(Create(line2))
        self.play(Write(text2))
        self.play(Create(bracelabel_h))
        self.wait(2)
        self.play(Indicate(triangle2))
        self.wait(1)
        self.play(Indicate(orangetriangle))
        self.wait(1)
        self.play(Write(first))
        self.wait(1)
        self.play(Write(second))
        self.wait(2)
        self.play(TransformMatchingTex(second, secondedit))
        self.wait(3)
        self.play(Write(third))
        self.wait(2)
        self.play(TransformMatchingTex(third, lasttex))
        self.wait(1)

class Convert(Scene):
    def construct(self):
        lasttex = MathTex(r'S = \frac{a}{1-r}').shift(RIGHT * -2, DOWN * 2)
        rectlast = SurroundingRectangle(lasttex)
        self.add(lasttex)
        self.play(Create(rectlast))
        rectgroup = VGroup(rectlast, lasttex)
        self.play(rectgroup.animate.shift(UP*4, LEFT*3.5))
        rd2 = MathTex(r'0.\overline{3}').shift(DOWN,LEFT*3)
        equalsign = MathTex(r'=').next_to(rd2)
        self.play(Write(rd2))
        self.play(Write(equalsign))
        three = MathTex(r'\frac{3}{10} + \frac{3}{100} + \frac{3}{1000} + ...').next_to(equalsign)
        self.play(Write(three))
        a = MathTex(r'a = \frac{3}{10').shift(UP*1.5)
        r = MathTex(r'r = \frac{\frac{3}{100}}{\frac{3}{10}}')
        r2 = MathTex(r'r = \frac{1}{10}')
        self.play(Write(a))
        self.play(Write(r))
        self.play(ReplacementTransform(r, r2))
        substitute = MathTex(r'S = \frac{\frac{3}{10}}{1-\frac{1}{10}}').shift(RIGHT * -2, LEFT*3.5)
        substitute2 = MathTex(r'S = \frac{\frac{3}{10}}{\frac{9}{10}}').shift(RIGHT * -2, LEFT*3.5)
        substitute3 = MathTex(r'S = \frac{3}{9}').shift(RIGHT * -2, LEFT*3.5)
        self.play(Write(substitute))
        self.play(ReplacementTransform(substitute, substitute2))
        self.play(ReplacementTransform(substitute2, substitute3))
        three2 = MathTex(r'\frac{3}{9}').next_to(equalsign)
        self.play(ReplacementTransform(three, three2))
        self.remove(substitute3)
        self.remove(a)
        self.remove(r2)
        solutiongroup = VGroup(three2, equalsign, rd2)
        self.play(solutiongroup.animate.shift(UR*3))
        # ------------------------------------------
        twooneeight = MathTex(r'0.2\overline{18} = ', r'0.2 + 0.018 + 0.00018 + ...').shift(DOWN, LEFT*3)
        twooneeight2 = MathTex(r'0.2\overline{18} =', r'\frac{2}{10} + \frac{18}{1000} + \frac{18}{100000} + ...').shift(DOWN, LEFT*3)
        twooneeight3 = MathTex(r'0.2\overline{18} =',
                               r'\frac{2}{10} + (\frac{18}{1000} + \frac{18}{100000} + ...)').shift(DOWN, LEFT * 3)
        self.play(Write(twooneeight))
        self.play(TransformMatchingTex(twooneeight, twooneeight2))
        self.play(TransformMatchingTex(twooneeight2, twooneeight3))
        a2 = MathTex(r'a = \frac{18}{1000}').shift(DOWN*2.5, LEFT * 3)
        r2 = MathTex(r'r = \frac{\frac{18}{100000}}{\frac{18}{1000}}').shift(DOWN*2.5)
        r3 = MathTex(r'r = \frac{1}{100}').shift(DOWN*2.5)
        self.play(Write(a2))
        self.play(Write(r2))
        self.play(ReplacementTransform(r2, r3))
        S2 = MathTex(r'S = \frac{\frac{18}{1000}}{1-\frac{1}{100}}').shift(DR*3)
        S2edit = MathTex(r'S = \frac{\frac{18}{1000}}{\frac{99}{100}').shift(DR*3)
        S2edit2 = MathTex(r'S = \frac{18}{990}').shift(DR*3)
        S2edit3 = MathTex(r'S = \frac{1}{55}').shift(DR*3)
        self.play(Write(S2))
        self.play(ReplacementTransform(S2, S2edit))
        self.play(ReplacementTransform(S2edit, S2edit2))
        self.play(ReplacementTransform(S2edit2, S2edit3))
        twooneeight4 = MathTex(r'0.2\overline{18} =',
                               r'\frac{2}{10}+\frac{1}{55}').next_to(twooneeight3[0])
        simplify = MathTex(r'0.2\overline{18} =',
                               r'\frac{24}{110}').next_to(twooneeight3[0]).shift(LEFT*2)
        simplify2 = MathTex(r'0.2\overline{18} =',
                               r'\frac{12}{55}').next_to(twooneeight3[0]).shift(LEFT*2)
        self.play(ReplacementTransform(twooneeight3[1], twooneeight4[1].shift(LEFT*2)))
        self.play(ReplacementTransform(twooneeight4[1], simplify[1]))
        self.remove(S2edit3)
        self.remove(a2)
        self.remove(r3)
        self.play(ReplacementTransform(simplify[1], simplify2[1]))

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()

# manim -pql scene.py OpeningManim