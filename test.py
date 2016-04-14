import re

text=open("test.txt")
data=text.read()


def colonParser(data):
    if data[0]==':':
        return (':', data[1:].lstrip())

def spaceparser(data):
    if data[0]==' ':
        return (' ', data[1:].lstrip())





def parser(data):
  
  if data[0:4] == "null" :
     return None, data[4:],0;
  else :
     return None

def commaParser(data):
    if data and data[0]==',':
        return (',', data[1:].strip())




def stringparser(data):
  i=1
  if data[0]=='"' :
    while data[i]!='"' :
	 i+=1
    return data[1:i] , data[i+1:] 
  else :
    return None




def numparser(data):
    result= re.match( r'[0-9]+\.?[0-9]*', data)
    
    
    if result:
    	leng=len(result.group())
    	return  result.group(), data[leng:] 

    return None


def arrayparser(data):
 
  arr=[]

  if data[0] != "[" :
      return None

  while data[0]!="]":
  	  
	  a = elementparser(data[1:])
	  if a :
	      data=a[1]
	      
	      if a[0] !=',' 
	  	      arr.append(a[0]) 
	  	      
	  
  return arr , data[1:]



def objectparser(data):
    obj = {}
    if data[0] != '{':
    	return None


       
    while data[0] != '}':



        result = stringparser(data[1:])
        if result == None:
            raise SyntaxError
        key = result[0]
        result = colonParser(result[1].strip())
        if result == None:
            raise SyntaxError
        result = elementparser(result[1].strip())
        if result == None:
            raise SyntaxError
        obj[key] = result[0]
        data = result[1].lstrip()
       
    return (obj, data[1:])

	 
     
def elementparser(data) :

	
		
	
	    if commaParser(data):
	        return commaParser(data)

	    if stringparser(data):
	        return stringparser(data)
	 	       
	    if numparser(data):
	        return numparser(data)

	    if arrayparser(data):
	        return arrayparser(data)

	    if objectparser(data):
	    	return objectparser(data)
	    if spaceparser(data):
	    	return spaceparser(data)

    


st1 = elementparser(data.strip())


print st1[0]