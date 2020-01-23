"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float], delta=0.0001) -> float:
	"""
	Calculate value of e^x with Taylor series
	:param x: x value
	:return: e^x value
	"""
	if x == 0:
		return 1
	else:
		result_sum = 1
		n = 1
		while True:
			result = (x ** n) / math.factorial(n)
			if result < delta:
				return result_sum
			else:
				result_sum += result
				n += 1


def sinx(x: Union[int, float], delta=0.0001) -> float:
	"""
	Calculate sin(x) with Taylor series
	:param x: x value
	:return: sin(x) value
	"""
	result_sin = 0
	n = 0
	while True:
		result_ = ((-1) ** n) * (x ** (2 * n + 1)) / (math.factorial(2 * n + 1))
		result_sin += result_
		if abs(result_) < delta:
			return result_sin
		else:
			n += 1


if __name__ == "__main__":
	#print(ex(1.55433))
	print(sinx(1.55433))