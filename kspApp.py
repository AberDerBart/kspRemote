from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from client import Client as Client
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class MainWindow(GridLayout):
	fuel=ObjectProperty()

	def build(self):
		pass

class KspApp(App):
	def build(self):
		Clock.schedule_interval(self.updateData, .1)
		self.mainWindow=MainWindow()
		self.client=Client()
		self.client.connect()
		return self.mainWindow
	def updateData(self,dt):
		vessel=self.client.getVessel()
		if(vessel):
			self.mainWindow.fuel.updateData(self.client,vessel)
		

KspApp().run()
