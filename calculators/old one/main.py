import math 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.window import Window
from kivy.factory import Factory
#Window.size =(500,700)
math = ''

class mygrid(Widget):
	def cut(self):
		length = self.ids.calc.text
		length = length[:-1]
		self.ids.calc.text = length
	def checker(self):
		trump = self.ids.calc.text
		ran = self.ids.calc.text
		rop = float(ran)
		sera = float(0)
		if rop > 0:
			self.ids.calc.text = '-' + trump
		else:
			tk = trump.replace('-', '')
			self.ids.calc.text = tk	
	
	
	
	
	
	def clear(self):
		self.ids.calc.text= ''
		self.ids.test.text = ''
	def back(self):
		pass
	def nom(self,num):
		
		state = self.ids.calc.text
		if state == '0':
			self.ids.calc.text = ''
			self.ids.calc.text = num
		else:
			self.ids.calc.text=state + num
	def square(self):
		global math
		global vartiy
		
		sort = self.ids.calc.text
		vartiy = float(sort)
		math = 'square'
		
		self.ids.calc.text =f"√({sort})"	
		
				
	def result(self , sign):
		global math
		
		global one
		sre = self.ids.calc.text
		one = self.ids.calc.text
		float(one)
		if sign == "+":
			self.ids.calc.text = ''
			self.ids.test.text = sre + '+'
			math = 'addition' 
		if sign == "-":
			self.ids.calc.text =''
			self.ids.test.text = sre + '-'
			math = 'minus' 
		if sign == "*":
			self.ids.calc.text =  ''
			self.ids.test.text = sre + '*'
			math = 'multi' 
		if sign == "/":
			self.ids.calc.text = ''
			math = 'div'
			self.ids.test.text = sre + '/'
		if sign == ".":
			
			self.ids.calc.text = one +'.'
		if sign == "√":
			self.ids.calc.text =f"√({one})"	
			math = '√'	
	def equal(self):
		password = self.ids.calc.text
		
		if password == 'about':
			Factory.mypop().open()
			
		if math == 'addition':
			sec = self.ids.calc.text
			float(sec)
			nor = float(sec) + float(one)
			self.ids.test.text = ''
			inl = str(nor)
			self.ids.calc.text = inl 
			self.ids.test.text = ''
		if math == 'minus':
			self.ids.test.text = ''
			rango = self.ids.calc.text
			note = float(one) - float(rango)
			self.ids.calc.text = str(note)
			#self.ids.calc.text = inl
		if math == 'multi':
			self.ids.test.text = ''
			sec = self.ids.calc.text
			float(sec)
			nor = float(sec) * float(one)
			inl = str(nor)
			self.ids.calc.text = inl
		if math == 'div':
			self.ids.test.text = ''
			sec = self.ids.calc.text
			float(sec)
			nor = float(sec) / float(one)
			inl = str(nor)
			self.ids.calc.text = inl
		if math == 'square':
			n = vartiy ** 0.5
			print(n)
			self.ids.calc.text = str(n)
							
	
class joro(App):
	def build(self):
		Window.clearcolor = (0,0,0,.5)
		return mygrid()

joro().run()				