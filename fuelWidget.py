from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty,ObjectProperty

class FuelBar(Widget):
	fill = NumericProperty(.1)
	barWidth = NumericProperty(20)

class FuelWidget(BoxLayout):
	label = ObjectProperty()
	meter = ObjectProperty()
	label = ObjectProperty()
		
class FuelOverview(BoxLayout):
	widgets={}
	def updateData(self,client,vessel):
		resources=client.pollResources(vessel)
		for resource in resources.keys():
			if(resource not in self.widgets):
				self.widgets[resource]=FuelWidget()
				self.add_widget(self.widgets[resource])
			values=resources[resource]
			print(values['amount'],values['max'])
			self.widgets[resource].meter.fill=values['amount']/values['max']
			self.widgets[resource].label.text=resource
