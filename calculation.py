class stack():
	def __init__(self):
		self._list = []
		self.length = 0

	def push(self, elem):
		self._list.append(elem)
		self.length += 1

	def top(self):
		return self._list[self.length-1]

	def pop(self):
		temp = self.top()
		self._list.pop()
		self.length -= 1
		return temp

	def empty(self):
		return len(self._list) == 0



def is_float(string):
	idx = 0
	dot = 0
	while idx < len(string):
		if string[idx] == '.':
			dot += 1
		elif string[idx] >'9' or string[idx] < '0':
			return False
		idx += 1

	if dot > 1:
		return False
	return True




def string_to_list(string):
	_list = []
	idx = 0
	while idx < len(string):
		if string[idx] in ('+','-','*','/','(',')'):
			_list.append(string[idx])
			idx += 1
		elif string[idx].isdigit() == False and string[idx] != '.':
			#print("Invalid Input")
			return None
		else:
			end = idx + 1
			while end < len(string) and is_float(string[idx:end+1]):
				end += 1
			_list.append(float(string[idx:end]))
			idx = end

	return _list		




def list_to_suffix_expr(_list):
	if _list == None:
		return None

	operator_stack = stack()
	result_stack = stack()
	idx = 0
	while idx < len(_list):
		if isinstance(_list[idx], float):
			result_stack.push(_list[idx])
		elif _list[idx] == '(':
			operator_stack.push(_list[idx])
		elif _list[idx] == ')':
			while operator_stack.empty() == False and operator_stack.top() != '(':
				result_stack.push(operator_stack.pop())
			if operator_stack.empty():
				return None
			else:
				operator_stack.pop()
		elif _list[idx] in ('*','/'):
			if operator_stack.empty() or operator_stack.top() in ('+','-','('):
				operator_stack.push(_list[idx])
			else:
				while operator_stack.empty() == False and operator_stack.top() in ('*','/'):
					result_stack.push(operator_stack.pop())
				operator_stack.push(_list[idx])
		else:
			while operator_stack.empty() == False and operator_stack.top() != '(':
				result_stack.push(operator_stack.pop())
			operator_stack.push(_list[idx])

		idx += 1
	

	while operator_stack.empty() == False:
		result_stack.push(operator_stack.pop())

	return result_stack._list



def get_answer(_list):
	if _list == None:
		return None
	mystack = stack()

	idx = 0
	while idx < len(_list):
		if _list[idx] == '/':
			if mystack.empty():
				return None
			a = mystack.pop()
			if mystack.empty():
				return None
			b = mystack.pop()

			if a == 0:
				return None
				
			mystack.push(b / a)
		elif _list[idx] == '*':
			if mystack.empty():
				return None
			a = mystack.pop()
			if mystack.empty():
				return None
			b = mystack.pop()
			mystack.push(a * b)
		elif _list[idx] == '+':
			if mystack.empty():
				return None
			a = mystack.pop()
			if mystack.empty():
				return None
			b = mystack.pop()
			mystack.push(a + b)
		elif _list[idx] == '-':
			if mystack.empty():
				return None
			a = mystack.pop()
			if mystack.empty():
				return None
			b = mystack.pop()
			mystack.push(b - a)
		else:
			mystack.push(_list[idx])

		idx += 1
		#print(mystack.top())

	return mystack.top()



def calculation(string):
	try:
	    	if string.strip() == "" or string.strip() == '.':
		    	return None
	    	string = ('(' + string + ')').replace(" ","").replace("(-","(0-").strip()
	    	inffix_expression = string_to_list(string)
	    	#print(inffix_expression)
	    	suffix_expression = list_to_suffix_expr(inffix_expression)
	    	#print(suffix_expression)
	    	return get_answer(suffix_expression)
	except:
	    	return None



# for debug
# if __name__ == "__main__":
# 	print("for debug:")
# 	print(calculation("123+456/100"))
# 	print(calculation("-12"))
# 	print(calculation("1-2*(3-8)"))
