from manim import *


class ClimbingPowers(Scene):
    def construct(self):
        image = ImageMobject("climbing.png")
        image.scale(1.2)
        image.to_edge(RIGHT, buff=1)
        self.add(image)
        firsteq = MathTex(r'(\sqrt{2}^{\sqrt{2}})^{\sqrt{2}}').shift(UP*3, LEFT*4)
        self.play(Write(firsteq))
        law = MathTex(r'(a^m)^n = a^{mn}').shift(UP*2.5, RIGHT*3)
        self.play(Create(law))
        self.wait(1)
        firsteq1 = MathTex(r'(\sqrt{2}^{\sqrt{2}\cdot\sqrt{2}})').shift(UP*3, LEFT*4)
        self.play(ReplacementTransform(firsteq, firsteq1))
        self.wait(1)
        firsteq2 = MathTex(r'\sqrt{2}^2').shift(UP*3, LEFT*4)
        self.play(ReplacementTransform(firsteq1, firsteq2))
        self.wait(1)
        firsteq3 = MathTex(r'= 2').next_to(firsteq2)
        self.play(Write(firsteq3))
        self.wait(1)
        vs = Text('vs').shift(UP*2, LEFT*4)
        self.play(Write(vs))
        secondeq = MathTex(r'{{\sqrt{2}^{\sqrt{2}}}^{\sqrt{2}}}').shift(UP, LEFT*4)
        self.play(Write(secondeq))
        toinf = Text('to infinity').next_to(secondeq)
        self.play(Write(toinf))
        line = Line([-7,0,0], [2,0,0]).shift(LEFT)
        self.play(Create(line))
        solve = Text("let's first solve").scale(0.5).shift(DOWN*0.5,LEFT*4)
        self.play(Write(solve))
        x = MathTex(r'{{{x',r'^{x}}^{x}}}^x',r'... = 2').shift(DOWN*2, LEFT*4)
        self.play(Write(x))
        self.play(Indicate(x[1]))
        x.set_color_by_tex('^{x}}^{x}}}^x', BLUE)
        self.wait(1)
        blue = Text('since it goes on to infinity, the blue equals 2 as well').scale(0.4).shift(RIGHT*2, DOWN*3)
        self.play(Write(blue))
        x2 = MathTex(r'{{{x', r'^2', r'... = 2').shift(DOWN * 2, LEFT * 4)
        self.play(ReplacementTransform(x[1], x2[1]))
        x3 = MathTex(r'x = \sqrt{2}').shift(DOWN * 3, LEFT * 4)
        self.play(Write(x3))
        self.clear()
        code = '''a = 1
import math
for n in range(100): # loop
    # do this 100 times
    a = math.sqrt(2)**a
    print(a)'''
        codeblock = Code(code=code, tab_width=2, background="window",
                             language="Python", font="Monospace").scale(0.7)
        self.play(Write(codeblock))
        self.play(ApplyMethod(codeblock.shift, DL*2))
        explained = Text('This code runs square root of 2\n'
                         'to the power square root of 2, etc.').scale(0.8)
        self.play(Write(explained))
        output = ImageMobject('outputt.png').shift(DOWN, RIGHT*6)
        self.add(output)
        self.wait(1)
        self.clear()
        finaltext = Text('Therefore,')
        firsteq = MathTex(r'(\sqrt{2}^{\sqrt{2}})^{\sqrt{2}}').shift(DOWN)
        secondeq = MathTex(r'= {{\sqrt{2}^{\sqrt{2}}}^{\sqrt{2}}}...').next_to(firsteq)
        self.play(Write(finaltext))
        self.play(Write(firsteq))
        self.play(Write(secondeq))
        recgroup = VGroup(finaltext, firsteq, secondeq)
        rec = SurroundingRectangle(recgroup)
        self.play(Create(rec))

# manim -pql power_tower.py ClimbingPowers