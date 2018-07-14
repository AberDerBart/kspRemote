import krpc

class ClientDummy:
	def connect(self):
		pass
	def getVessel(self):
		return 'vessel'
	def pollResources(self,vessel):
		d={}
		for i in range(1,6):
			d[str(i)]={'max':20,'amount':i}
		return d

class Client:
	def __init__(self):
		self.conn=None
	def connect(self):
		self.conn = krpc.connect()
	def getVessel(self):
		try:
			vessel=self.conn.space_center.active_vessel
			return vessel
		except krpc.error.RPCError:
			return None
		
	def pollResources(self,vessel):
		try:
			resources={}
			for resName in vessel.resources.names:
				amount=vessel.resources.amount(resName)
				max_=vessel.resources.max(resName)
				resources[resName]={"amount":amount, "max":max_}
			return resources
		except krpc.error.RPCError:
			return {}
