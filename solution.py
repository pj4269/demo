import sys 
import numpy as np 

# please input 'q' to quit

stdin = sys.stdin
arr = np.empty((0,3), int)

for line in stdin: 
		try: 							
				if 'q' == line.rstrip(): 							    
				  break							
				arr = np.append(arr, float(line))
				mean = np.round(np.mean(arr), 3)						
				mean = ('%f' % mean).rstrip('0').rstrip('.')
				std = np.round(np.std(arr), 3)
				std = ('%f' % std).rstrip('0').rstrip('.')
				med = np.round(np.median(arr), 3)
				med = ('%f' % med).rstrip('0').rstrip('.')
				print('{}, {}, {}'.format(mean, std, med) )
		except :
				  print ('Wrong input')
				  
  
print("Exit") 

