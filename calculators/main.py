from kivy.lang.builder import Builder
import time
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
import math



class Main(MDApp):
	def type(self,x):
		self.root.ids.calc.text = 'str(x)'
	def view(self):
		#self.root.ids.screen_manage.current = '1'
		print('1234')
	def theme(self,color):
		if color == 'dark':
			self.theme_cls.theme_style = "Dark"
			self.root.ids.a.md_bg_color =  (0,0,0,.65)
			self.root.ids.b.md_bg_color =  (0,0,0,.65)
			self.root.ids.c.md_bg_color = (0,0,0,.65)
			self.root.ids.d.md_bg_color = (0,0,0,.65)
			self.root.ids.e.md_bg_color = (0,0,0,.65)
			self.root.ids.f.md_bg_color = (0,0,0,.65)
			self.root.ids.g.md_bg_color =  (0,0,0,.65)
			self.root.ids.h.md_bg_color = (0,0,0,.65)
			self.root.ids.i.md_bg_color =  (0,0,0,.65)
			self.root.ids.j.md_bg_color =  (0,0,0,.65)
			self.root.ids.k.md_bg_color =  (0,0,0,.65)
			self.root.ids.l.md_bg_color =  (0,0,0,.65)
			self.root.ids.m.md_bg_color =  (0,0,0,.65)
			self.root.ids.n.md_bg_color =  (0,0,0,.65)
			self.root.ids.o.md_bg_color =  (0,0,0,.65)
			self.root.ids.p.md_bg_color =  (0,0,0,.65)
			self.root.ids.q.md_bg_color = (0,0,0,.65)
			self.root.ids.r.md_bg_color =  (0,0,0,.65)
			self.root.ids.s.md_bg_color =  (0,0,0,.65)
			self.root.ids.t.md_bg_color =  (0,0,0,.65)	
		if color == 'light':
			self.theme_cls.theme_style = "Light"
			self.root.ids.a.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.b.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.c.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.d.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.e.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.f.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.g.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.h.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.i.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.j.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.k.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.l.md_bg_color = (235/255,231/255,233/255,0.8)	
			self.root.ids.m.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.n.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.o.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.p.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.q.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.r.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.s.md_bg_color = (235/255,231/255,233/255,0.8)
			self.root.ids.t.md_bg_color = (235/255,231/255,233/255,0.8)	

	def scre(self):
		self.root.ids.screen_manage.current = '1'
	def box(BoxLayout):
			pass	
	def build(self):
		man = Button(text='hello thee')
		#grid.add_widget(man)
		Builder.load_file('main.kv')
		self.theme_cls.theme_style = "Dark"
		#self.theme_cls.primary_palette = 'Gray'
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
		
		state = self.root.ids.calc.text
		if state == '0':
			self.root.ids.calc.text = ''
			self.root.ids.calc.text = num
		else:
			self.root.ids.calc.text=state + str(num)
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
							

			
    	    	    

Main().run()