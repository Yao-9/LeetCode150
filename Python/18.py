import pdb
class Solution:
	# @param gas, a list of integers
	# @param cost, a list of integers
	# @return an integer
	def canCompleteCircuit(self, gas, cost):
		gas_left = gas_needed = start = 0
		for i, (g, c) in enumerate(zip(gas,cost)):
			gas_left += g - c
			if gas_left < 0:
				#pdb.set_trace()
				gas_needed -= gas_left
				start = i + 1
				gas_left = 0

		return start if gas_left >= gas_needed else -1
			
a = Solution()
test_gas = [1,2]
test_cost = [2,1]
print a.canCompleteCircuit(test_gas, test_cost)
