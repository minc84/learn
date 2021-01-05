from datetime import datetime
import pytz
class Account:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.history = []


	@staticmethod
	def _get_time():
		return pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()
		

	def deposit(self, amount):
		self.balance +=amount
		self.show_balance()
		self.history.append([amount,self._get_time()])

	def withdraw(self, amount):
		if self.balance > amount:
			self.balance -= amount
			print(f'You spend {amount} units')
			self.history.append([-amount,self._get_time()])

			self.show_balance()
		else:
			print('not money')
			self.show_balance()

	def show_balance(self):
		print(f'You balance {self.balance}')

	def show_histore(self):
		for amount, date in self.history:
			if amount >0:
				transaction = 'deposit'
			else:
				transaction = 'withdraw'
			print(f'{amount}  {transaction}  {date}\t')



a = Account('Nikolay',0)


