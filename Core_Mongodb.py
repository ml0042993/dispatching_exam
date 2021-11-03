import pymongo
import setting
class MongodbClient:
	def __init__(self):
		'''
		初始化
		连接spider数据库
		'''
		self.db = pymongo.MongoClient(setting.MONGOCLIENT)['test']

	def read_Nosql(self,num):
		'''
		:param Nosql_name:需要查询的数据库的名称
		:return: {'number': 1}
		'''
		# return eval('self.db.{}'.format(Nosql_name)+'.find({},{"Real_url":1,"_id":0})')
		return self.db.get_collection("test").find({"numner":num},{"_id":0})
	def count(self):
		return len(list(self.db.proxypool.find({})))

if __name__ == '__main__':
	obj = MongodbClient()
	for i in obj.read_Nosql(1):
		print(i)
		# print(obj.read_Nosql({"number": 1}))
	# print(len(list(obj.all().clone())))########
	# taps = math.ceil(len(list(obj.all().clone()))/10)+1
	# for i in range(1,taps):
	# 	sk = 10*i-10
	# 	for j in obj.all().skip(sk).limit(10):
	# 		if j:
	# 			print(j,type(j))
	# 		else:break
	# 	print('\n')