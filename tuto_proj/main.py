from manim import *
from manim_slides import Slide

class BasicNetworking(Slide):
    def construct(self):
        self.play(Write(Text("Basic Networking", color=WHITE, font_size=50)))
        
        self.next_slide()

        self.clear()

        # Withe rectangle with lable "Computer" in the center of rectangle appearing from center
        computer = Rectangle(width=4, height=3, color=WHITE)
        computer_label = Text("Computer", color=WHITE).scale(0.7)
        computer_label.move_to(computer.get_center())
        self.play(Create(computer), Write(computer_label))

        self.next_slide()

        computer = VGroup(computer, computer_label)

        # Computer splits on two and move to the left and right
        computer_left = computer.copy()
        computer_right = computer.copy()
        computer_left.shift(LEFT*4+DOWN*2).scale(0.5)
        computer_right.shift(RIGHT*4+DOWN*2).scale(0.5)
        self.play(Transform(computer.copy(), computer_left), Transform(computer, computer_right))

        self.next_slide()

        # Package box apears from the top of the screen and moves to the center of the screen
        data = Rectangle(width=3, height=2, color=WHITE, fill_opacity=1)
        data_label = Text("Hello Networking", color=BLACK).scale(0.5)
        data_label.move_to(data.get_center())
        data = VGroup(data, data_label)
        data.move_to(UP*6)
        self.add(data)
        self.play(data.animate.shift(DOWN*5), run_time=1)

        self.next_slide()

        # lable "Hello Networking" changes to "Data" 
        new_label = Text("Data", color=BLACK).scale(0.4).move_to(data.get_center())
        self.play(Transform(data[1], new_label))

        self.next_slide()

        # Data box shrinks and turns to the question mark
        self.play(Transform(data, Text("?", color=WHITE).scale(3).move_to(data.get_center())))
        text = Text("How can I transfer it?", color=WHITE, font_size=30)
        self.play(Write(text))

        self.next_slide()

        # Text and question mark transforms to the arrow between two computers
        arrow = Arrow(start=computer_left.get_right(), end=computer_right.get_left(), color=WHITE)
        data = VGroup(text, data)
        self.play(Transform(data, arrow))

        # blue small filled data rectangle appears on top of the arrow and moves to the left end of the arrow
        data = Rectangle(width=0.7, height=0.7, color=BLUE, fill_opacity=1)
        data.move_to(arrow.get_start()+UP*0.5+RIGHT*0.5)

        label = Text("Data", color=BLUE).scale(0.5)
        label.next_to(data, UP)
        self.play(FadeIn(data), Write(label))

        # Label "Data" moves to the center of the data rectangle and changes color to black
        new_label = Text("Data", color=BLACK).scale(0.4).move_to(data.get_center())
        self.play(Transform(label, new_label))
        data = VGroup(data, label)

        # Draw the data rectangle on the left end of the arrow and move it to the right end of the arrow
        self.play(data.animate.shift(RIGHT*4.5), run_time=2, rate_functions=linear)
        self.play(FadeOut(data), run_time=0.3)
        data.move_to(arrow.get_start()+UP*0.5+RIGHT*0.5)
        self.play(FadeIn(data), run_time=0.3)

        text = Text("It's called the \"Physical Layer\"", color=WHITE, font_size=30)
        text[13:28].set_color(RED)
        self.play(Write(text)) 

        self.next_slide()

        self.play(Transform(text, Text("But what if there more computers?", color=WHITE, font_size=30)))

        self.next_slide()

        # Everything except computers disappears
        self.play(FadeOut(*self.mobjects[2:]), run_time=0.3)

        # Align computers to the center of the screen
        computer_left = self.mobjects[0]
        computer_right = self.mobjects[1]
        top_copy = computer_right.copy().shift(UP*4)
        bottom_copy = computer_right.copy()
        self.play(Transform(computer_left, computer_left.copy().shift(UP*2)), Transform(computer_right, computer_right.copy().shift(UP*2)))
        self.play(Transform(computer_right.copy(), top_copy), Transform(computer_right.copy(), bottom_copy), run_time=2)

        # Draw the arrows and question mark ontop of them between computers
        arrow_mid = Arrow(start=computer_left.get_right(), end=computer_right.get_left(), color=WHITE)
        arrow_top = Arrow(start=computer_left.get_right(), end=top_copy.get_left(), color=WHITE)
        arrow_bottom = Arrow(start=computer_left.get_right(), end=bottom_copy.get_left(), color=WHITE)
        question_mark = Text("?", color=RED).scale(3).move_to(arrow_mid.get_center())
        self.play(Create(arrow_mid), Create(arrow_top), Create(arrow_bottom), Write(question_mark), run_time=2)

        self.next_slide()

        # Uncreate everything 
        self.play(FadeOut(*self.mobjects), run_time=0.3)

        text = Text("Introducing the \"IP Layer\"\n", color=WHITE, font_size=30)
        text[14:23].set_color(RED)
        self.play(Write(text), run_time=0.5)

        self.next_slide()
        self.play(FadeOut(text[:14]), Transform(text[14:23], text[15:22].copy().move_to(UP*3).set_color(WHITE)), run_time=2)

        # White box appears in the middle of the screen, there two lables: source and destination and after that there is a ip addresses
        ip = Rectangle(width=5, height=3, color=WHITE, fill_opacity=1).move_to(RIGHT*2+DOWN*1)
        self.play(FadeIn(ip), run_time=2)

        source = Text("Source: 192.168.103.2", color=BLACK).scale(0.5)
        source.move_to(ip.get_center()+UP*0.5+LEFT*0.5)
        destination = Text("Destination: 192.168.103.3", color=BLACK).scale(0.5)
        destination.move_to(ip.get_center()+DOWN*0.5)
        self.play(Write(source), Write(destination), run_time=1)
        
        ip_layer = VGroup(ip, source, destination)

        self.wait(0.1)

        
        self.next_slide()

        # Draw rectangle with two rectangles in it. 
        # One is red and one is blue, they are on top of each other.
        computer = Rectangle(width=3, height=4, color=WHITE)

        ip = Rectangle(width=2, height=1, color=BLUE, fill_opacity=1)
        label = Text("IP Layer", color=BLACK).scale(0.5)
        label.move_to(ip.get_center())
        ip = VGroup(ip, label)
        ip.move_to(computer.get_center()+UP*1)

        physical = Rectangle(width=2, height=1, color=RED, fill_opacity=1)
        label2 = Text("Physical", color=BLACK).scale(0.5)
        label2.move_to(physical.get_center())
        physical = VGroup(physical, label2)
        physical.move_to(computer.get_center()+DOWN*1)

        computer = VGroup(computer, ip, physical)
        # move to the left and scale computer
        computer.move_to(LEFT*4)
        computer.scale(0.8)

        self.play(Create(computer[0]), FadeIn(computer[-1]))
        self.play(Transform(ip_layer, computer[1]), run_time=1)
        
        self.next_slide()

        # Create copy of the computer and move it to the right
        computer2 = computer.copy().move_to(RIGHT*4)
        self.play(Transform(computer.copy(), computer2))

        text = text[14:23]
        
        # creates switch and moves it to the middle of the screen
        switch = computer.copy().move_to(ORIGIN)
        self.play(Transform(text, switch))

        # Add labels
        label = Text("Switch", color=WHITE).scale(0.7)
        label.next_to(switch, UP)
        switch.add(label)

        label2 = Text("192.168.103.2", color=WHITE).scale(0.6)
        label2.next_to(computer, UP)
        computer.add(label2)

        label3 = Text("192.168.103.3", color=WHITE).scale(0.6)
        label3.next_to(computer2, UP)
        computer2.add(label3)

        self.play(Write(label), Write(label2), Write(label3))

        # Create arrows between computers and switch

        arrow1 = DoubleArrow(start=computer.get_right(), end=switch.get_left(), color=WHITE)
        arrow2 = DoubleArrow(start=computer2.get_left(), end=switch.get_right(), color=WHITE)

        self.play(FadeIn(arrow1), FadeIn(arrow2))

        self.next_slide()

        # Fading it out and showind package with destination and source ip + data
        mobjects = self.mobjects
        self.play(FadeOut(*mobjects), run_time=0.3)

        
        #### PACKAGE ####
        
        package = Rectangle(width=6, height=4, color=WHITE, fill_opacity=1).move_to(ORIGIN)
        package.label = Text("Package", color=WHITE).scale(0.7)
        package.label.next_to(package, UP)
        package.add(package.label)
        
        ip = Rectangle(width=5, height=1, color=BLUE, fill_opacity=1)
        label = Text("Source: 192.168.103.2", color=BLACK).scale(0.4)
        label2 = Text("Destination: 192.168.103.3", color=BLACK).scale(0.4)
        label.move_to(ip.get_center()+UP*0.3)
        label2.move_to(ip.get_center()+DOWN*0.3)
        ip = VGroup(ip, label, label2)
        ip.move_to(package.get_center())

        data = Rectangle(width=5, height=1, color=RED, fill_opacity=1)
        label3 = Text("Data: Hello Networking!", color=BLACK).scale(0.5)
        label3.move_to(data.get_center())
        data = VGroup(data, label3)
        data.next_to(ip, -UP*0.5)

        package = VGroup(package, ip, data)

        #### END OF PACKAGE ####

        self.play(FadeIn(package), run_time=1)

        self.next_slide()


        #### COMPUTERS ####

        computers = VGroup(computer, computer2, switch, arrow1, arrow2)

        self.play(FadeOut(package), run_time=0.3)
        
        package.scale(0.3).move_to(computer[-2].get_center())
        self.play(FadeIn(computers), run_time=0.2)
        self.play(FadeIn(package), run_time=0.5)

        self.wait(0.3)
        self.play(Transform(package, package.copy().move_to(switch[-2].get_center())), run_time=1)
        
        self.wait(0.3)

        package_new = package.copy()
        computers = computers.add(package)
        self.play(Transform(package_new, package_new.copy().scale(1.5).shift(LEFT*3)), Transform(computers, computers.copy().scale(0.6).shift(UP*2)), run_time=1)

        # move ip_layer in package to the right
        ip = package_new[1]
        ip_layer = ip.copy().move_to(RIGHT*2.5+DOWN*1).scale(1.5)
        self.play(Transform(computers[-1], computers[-1].copy().move_to(computers[2].get_center()+UP*0.5)), run_time=1)
        self.play(Transform(ip, ip_layer), run_time=0.5)

        # paint destanation text in ip_layer in red and back to black
        for i in range(2):
            self.play(ip[2].animate.set_color(RED), computers[-2].animate.set_color(RED), run_time=0.5)
            self.play(ip[2].animate.set_color(BLACK), run_time=0.5)
        self.play(ip[2].animate.set_color(RED), run_time=0.5)

        arrow = Arrow(start=ip.get_top(), end=computers[-2].get_bottom(), color=WHITE)
        self.play(Create(arrow))
        
        self.next_slide()

        # pack ip_laayer back to package_new and move it all to the package
        self.play(ip[2].animate.set_color(BLACK), computers[-2].animate.set_color(WHITE), FadeOut(arrow), run_time=0.5)

        self.play(Transform(ip, ip.copy().scale(1/1.5).next_to(package_new[-1], UP*0.5)), run_time=0.5)
        self.play(Transform(package_new, package))
        self.play(FadeOut(package_new), run_time=0.5)
        
        self.next_slide()

        # return computers to their original size and position
        self.play(Transform(computers, computers.copy().scale(1/0.6).shift(DOWN*2)), run_time=1)

        # move package to the data layer of the switch
        package = computers[-1]
        self.play(Transform(package, package.copy().move_to(computers[2][2].get_center())), run_time=1)
        
        # move package to the destination computer
        self.play(Transform(package, package.copy().move_to(computers[1][2].get_center())), run_time=1)

        # move package from the data layer to the ip layer
        self.play(Transform(package, package.copy().move_to(computers[1][1].get_center())), run_time=1)

        self.next_slide()

        # Squish computers again and move copy of package to the left bottom corner
        self.play(Transform(computers, computers.copy().scale(0.6).shift(UP*2)), run_time=1)
        package_new = computers[-1].copy()
        self.play(Transform(package_new, package_new.copy().scale(1/0.6*1.5).move_to(LEFT*3+DOWN*2)), run_time=1)

        ip = package_new[1]
        ip_layer = Text("Oh, This is for me!", color=WHITE).scale(1).move_to(RIGHT*2+DOWN*1)
        self.play(Transform(ip, ip_layer), FadeOut(package[1]) ,run_time=1)

        self.next_slide()

        self.play(FadeOut(package_new), FadeOut(ip_layer), FadeOut(ip), run_time=0.1)


