class SensorModule:
	ref_value = 0
	curr_value = 0 

	def _init_(self, ref_value = 0):
		self.ref_value = ref_value

	def setRefValue(ref_value):
		self.ref_value = ref_value

	def getRefValue():
        	return self.ref_value

	def setCurrValue(curr_value):
		self.curr_value = curr_value

	def getCurrValue():
		return self.curr_value
	
	def startMeasure():
		return 0
