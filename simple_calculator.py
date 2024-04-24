class SimpleCalculator:
	def __init__(self) -> None:
    	
		"""
		Instantiate any data attributes
  
		"""
		self.his_list = []
		pass

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		operators = ['+','*','/','-']
		token = []
		s = ''
		for i in input_expression:
			if i.isnumeric():
				s+=i
				continue
			else:
				if len(s)>0:
					token.append(s)
				s = ''
				if not i==' ':
					token.append(i)
		if len(s)>0:
			token.append(s)
				
		
		
		

		
		if len(token)!=3:
			self.his_list.append((input_expression,'Error'))
			#print( "Error")
			return "Error"
			
			
		if token[1]  not in operators:
			self.his_list.append((input_expression,'Error'))
			#print( "Error")
			return "Error"
		if token[0] in operators or token[2] in operators:
			self.his_list.append((input_expression,'Error'))
			#print( "Error")
			return "Error"
		else:
			a = operators.index(token[1])
			if a==0:
				ans = float(token[0]) + float(token[2])
				self.his_list.append((input_expression,ans))
				#print(ans)
				return ans
			elif a==1:
				ans = float(token[0])*float(token[2])
				self.his_list.append((input_expression,ans))
				#print(ans)
				return ans
			elif a==2:
				if float(token[2])==0:
					self.his_list.append((input_expression,'Error'))
					return "Error"
				ans = float(token[0])/float(token[2])
				self.his_list.append((input_expression,ans))
				#print(ans)
				return ans
			elif a==3:
				ans = float(token[0]) - float(token[2])
				self.his_list.append((input_expression,ans))
				#print(ans)
				return ans

			

		

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		self.his_list = self.his_list[::-1]
		#print(self.his_list)
		return self.his_list
"""
calculator = SimpleCalculator()
answer = calculator.evaluate_expression("2 / 3")
answer = calculator.evaluate_expression("2 +")
history = calculator.get_history()
"""