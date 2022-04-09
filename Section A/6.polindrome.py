def longestPal(string):
	n = len(string)            #size of string
	if (n < 2):
		return string      # if string is empty then size(single  character will always palindrome)
				                                                
	start=0
	maxLength = 1
	for i in range(n):
		low = i - 1                  #-1  start at the end of the character
		high = i + 1                 # 1	start first character string
		while (high < n and string[high] == string[i] ):			#loop check the condition 		
			high=high+1                                              #increse high(string index)value
	
		while (low >= 0 and string[low] == string[i] ):				
			low=low-1                                                #decrese low(string index)value
	
		while (low >= 0 and high < n and string[low] == string[high] ):        #check string last to first char
		    low=low-1
		    high=high+1
		
		length = high - low - 1
		if (maxLength < length):
			maxLength = length
			start=low+1
	
	return print("maximun palindrome string is :",string[start:start + maxLength])
	
string =input("enter the string :")                     #input string
longestPal(string)


