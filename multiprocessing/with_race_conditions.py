from threading import Thread, Lock



class CheapRich:

	money = 100

	lock = Lock()

	def cheap(self):

		for _ in range(10**6):
			self.lock.acquire()
			self.money -= 10
			self.lock.release()

		print(f"Cheap done")

	def rich(self):
		
		for _ in range(10**6):
			self.lock.acquire()
			self.money += 10
			self.lock.release()

		print(f"Rich done")


ss = CheapRich()

t1 = Thread(target=ss.cheap)
t2 = Thread(target=ss.rich)

t1.start()
t2.start()

t1.join()
t2.join()

print("With Lock Final money: ", ss.money)






















class CheapRich:

	money = 100

	def cheap(self):

		for _ in range(10**6):
			self.money -= 10

		print(f"Cheap done")

	def rich(self):
		
		for _ in range(10**6):
			self.money += 10

		print(f"Rich done")


ss = CheapRich()

t1 = Thread(target=ss.cheap)
t2 = Thread(target=ss.rich)

t1.start()
t2.start()

t1.join()
t2.join()

print("without Lock Final money: ", ss.money)
