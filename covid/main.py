from kivy.lang import Builder

from kivymd.app import MDApp




class Example(MDApp):
    man  = 'self.shake()'

    def build(self):
        return Builder.load_file('java.kv')


Example().run()