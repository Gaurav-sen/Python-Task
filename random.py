import collections
import time

class RandomGenerator(object):
	"""docstring for RandomGenerator"""
	def __init__(self, greater,lower):
		super (RandomGenerator, self).__init__()
		self.__greaterfrequency = greater
		self.__lowerfrequency = lower
		self.__random_Array = []
		self.__gt = 0
		self.__lte = 0

		
	def __random__(self,s=[0], a=1, c=1): 
		s[0] = a*s[0] + c
		return s[0]

	def __randint__(self,start_range,end_range):
		str_list = str(int(start_range + (1 + end_range - start_range) * self.__random__() * time.time()))
		
		if int(str_list[-len(str(end_range)):]) > 5 and self.__gt <= self.__greaterfrequency:
			self.__gt = self.__gt+1
			self.__random_Array.append(int(str_list[-len(str(end_range)):]))
			return int(str_list[-len(str(end_range)):]) 
		
		elif int(str_list[-len(str(end_range)):]) <= 5 and self.__lte < self.__lowerfrequency:
			self.__lte = self.__lte+1
			self.__random_Array.append(int(str_list[-len(str(end_range)):]))
			return int(str_list[-len(str(end_range)):])
		
		else:
			return self.__randint__(start_range,end_range)

	def __getfrequency__(self):
		print("Greater than 5:",self.__gt, "times") 
		print("Less than or equal to 5:",self.__lte,"times")
		
	# counter = collections.Counter(random_Array)
	# print(counter) 
	


obj_r = RandomGenerator(73,27)
for i in range(0,100):  
		obj_r.__randint__(0,9)

obj_r.__getfrequency__()
