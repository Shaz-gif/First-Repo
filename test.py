input_expression = '{278827 * {78783 /(78)} + (8939 /2/ 89982)}'
operators = ['+','*','/','-']
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
 
def token(input_expression):
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
 
 
#print(token(input_expression))

from stack import Stack

def check_brackets( list_tokens):
	
    a = Stack()
    lefty = [')','}']
    righty = ['(','{']
    key = 0
    for i in list_tokens:
        if i == '(':
            key = 1
        if key:
            b = a.peek()
            if b == '(':
                
                if i==lefty[1] or i==righty[1]:
                    return False
        if i in righty: 
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



#print(float('/'))

def check(exp):
    def isfloat(num):
        try:
            float(num)
            return True
        except:
            return False


    oper = ['/','*','-','+']
    Token = token(exp)
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

def eval_simp(exp):
    
    if check(exp):
        token_ = token(exp)
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
    

def evaluate_list_token(token):
    if token==[]:
        return 'Error'
    if not check_brackets(token):
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
            token[index:i+1] = [eval_simp(s)]
            i = index
        else:
            i+=1
            
    
    s = ''
    for i in token:
        s+=str(i)
    if len(token)>1:
        token = [eval_simp(s)]
            
            
        
            
    return token[0]
exp = '5//5'
input_expression = '(3+5/5)*5'
#print(token(input_expression))
#print(check(exp))
print(evaluate_list_token(token(input_expression)))
#print(eval_simp(exp))
        
            





