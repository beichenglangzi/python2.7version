# coding=utf-8
import turtle
import random

t = turtle.screensize() #返回默认大小(400, 300)
t = turtle.screensize(800, 600, "green")

turtle.down() #落下画笔,进行绘制
turtle.up() #抬起画笔,不进行绘制
turtle.pensize(12) #绘制时的宽度
turtle.color('red') #绘制时的颜色
turtle.fillcolor('red') #绘制的填充颜色
turtle.fill(t)
turtle.fill(t)
degree = 22
speed = 10
turtle.forward(degree) #向前移动距离degree代表距离
turtle.backward(degree) #向后移动距离degree代表距离
turtle.right(degree) #向右移动多少度
turtle.left(degree) #向左移动多少度
turtle.goto(20,40) #将画笔移动到坐标为x,y的位置
turtle.stamp() #复制当前图形
turtle.speed(speed) #画笔绘制的速度范围[0,10]整数
turtle.clear() #清空turtle画的笔迹
turtle.reset() #清空窗口，重置turtle状态为起始状态
turtle.undo()#撤销上一个turtle动作
turtle.isvisible()#返回当前turtle是否可见
turtle.stamp() #复制当前图形
turtle.write('string') #写字符串'string'

turtle.circle(10) #画一个R为10的圆形
turtle.circle(30, 270) #圆弧为270度
turtle.circle(20, steps=3) #画一个R为20的圆内切多边形


# line = 50
# for x in range(25):
#     if x % 5 ==0:
#         line += 20
#     turtle.forward(line)
#     turtle.right(144)
# turtle.exitonclick()