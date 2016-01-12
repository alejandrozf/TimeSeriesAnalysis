from score import np,GetScore,stability,growth,recent_performance,plot_array

def r_int(a,b):
	res = np.random.randint(a,b,1)[0]
	return res

def r_float(a,b):
	res = np.random.uniform(a,b,1)[0]
	return res
	
def zig_zag(n):
	arr = [100]
	for i in range(299):
		arr.append(arr[-1] + r_int(-n,n))
	return np.array(arr)

def almost_linear(m,n):
	def noise(arr,n):
		to_insert = np.random.uniform(0,200,n)
		indexes = np.random.permutation(np.random.random_integers(0,299,n))
		for i in range(n):
			arr[indexes[i]] = to_insert[i]
		return arr
	arr = np.array([m*i + n for i in range(300)])
	return noise(arr,10)


	
	
if __name__ == "__main__":
	#~ for i in range(10):
		#~ Datasets for testing
		#~-----------------------------------------------------------------
		#~ LX = zig_zag(10)
		#~ LX = almost_linear(2,10)
		#~Plots
		#~----------------------------------------------------------------- 
		#~ plot_array(LX,'Stability='+str(stability(LX)))
		#~ plot_array(LX,'Recent Performace='+str(recent_performance(LX)))
		#~ plot_array(LX,'Growth='+str(growth(LX)))
		#~ plot_array(LX,'Score='+str(GetScore(LX)))
	LX = np.array([100, 100.234, 101.24, 99.3837, 103.347, 104.3864, 104.45, 105.34,
				   106.237, 102.348, 105.343, 107.34, 106.321, 108.486, 109.239], dtype = "float32")
	print str(GetScore(LX))
	#~ print(str(GetScore(LX)))
	#~ plot_array(LX,'Score='+str(GetScore(LX)))
