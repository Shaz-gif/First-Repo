from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		super().__init__()
		self.his_list = []
		pass

	

	def token(self,input_expression):
		token = []
		s = ''
		for i in input_expression:
			if i.isnumeric() or i=='.':
				s +=i
				continue
			else:
				if len(s)>0:
					token.append(float(s))
				s = ''
				if not i ==' ':
					token.append(i)
		if len(s)>0:
			token.append(float(s))
        
		return token
  
	def tokenize(self, input_expression):
		token = []
		s = ''
		for i in input_expression:
			if i.isnumeric():
				s+=i
				continue
			else:
				if len(s)>0:
					token.append(int(s))
					s = ''
				if not i==' ':
					token.append(i)
		if len(s)>0:
			token.append(int(s))
 
		return token	

	def check_brackets(self, list_tokens):
		"""
		check if brackets are valid, that is, all open brackets are closed by the same type 
		of brackets. Also () contain only () brackets.
		Return True if brackets are valid, False otherwise
		"""
		a = Stack()
		lefty = [')','}']
		righty = ['(','{']
		key = 0
		for i in list_tokens:
			pass
			
			if key:
				b = a.peek()
				if b == '(':
                
					if i==lefty[1] or i==righty[1]:
						return False
			if i in righty: 
				if i == '(':
					key = 1
				a.push(i)
            
			elif i in lefty:
				if a.is_empty():
					return False
				ch = a.peek()
            
				if not righty.index(ch)== lefty.index(i):
					return False
				a.pop()
		if len(a)==0:
			return True	
		else:
			return False

		
	def check(self,exp):
		def isfloat(num):
			try:
				float(num)
				return True
			except:
				return False

		oper = ['/','*','-','+']
		Token = self.token(exp)
    #print(Token)
		for i in range(len(Token)):
			if Token[i] in oper:
				try:
					if  isfloat(str(Token[i-1])) and isfloat(str(Token[i+1])):
					    #print(1)
						continue
					else:
						return False
				except:
						return False
			else:
				try:
                #print(1)
					if  isfloat(str(Token[i])): continue
                
				except:
					return False
        
		return True
	def eval_simp(self,exp):
		if self.check(exp):
			token_ = self.token(exp)
		    #print(token_)
			while '/' in token_:
				token_[token_.index('/')-1:token_.index('/')+2] = [token_[token_.index('/')-1]/token_[token_.index('/')+1]]		
			while '*' in token_:
			
				token_[token_.index('*')-1:token_.index('*')+2] = [token_[token_.index('*')-1]*token_[token_.index('*')+1]]
		    #print(token_)  		
			while '+' in token_:
				token_[token_.index('+')-1:token_.index('+')+2] = [token_[token_.index('+')-1]+token_[token_.index('+')+1]]		
			while '-' in token_:
				token_[token_.index('-')-1:token_.index('-')+2] = [token_[token_.index('-')-1]-token_[token_.index('-')+1]]    
		    #print(token_)
			return token_[0]
		else:
			return 'Error' 


	def evaluate_list_tokens(self, token):
		"""
		Evaluate the expression passed as a list of tokens
		Return the final answer as a float, and "Error" in case of division by zero and other errors
		"""
		if token==[]:
			return 'Error'
		if not self.check_brackets(token):
			return 'Error'
		l = []
		i = 0
		while i <(len(token)):
        
        #print(i)
        #print(token)
			if token[i]=='(' or token[i]=='{':
				l.append(i)
				i+=1
			elif token[i]==')' or token[i]=='}':
            #print(l)
				index = l[-1]
				l.pop()
				s = ''
            #print(token[index+2:i])
				for j in token[index+1:i]:
					s += str(j) 
            #print(s)
            #print( token[index:i+1])
				token[index:i+1] = [self.eval_simp(s)]
				i = index
			else:
				i+=1
            
    
		s = ''
		for i in token:
			s+=str(i)
		if len(token)>1:
			token = [self.eval_simp(s)]
            
            
        
            
		return token[0]

	def evaluate_expression(self, input_expression):
    	
		ans = self.evaluate_list_tokens(self.token(input_expression))
  
		self.his_list.append((input_expression,ans))
		return ans

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		return self.his_list[::-1]






