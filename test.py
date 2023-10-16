class test:
	count=0
	def __init__(self):
		test.count+=1
	@classmethod
	def noofobjects(cls):
		print("the number of objects created",cls.count)
t1=test()
t2=test()
t4=test()
t5=test()
test.noofobjects()