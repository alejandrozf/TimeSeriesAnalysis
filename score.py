import numpy as np
from scipy.stats.stats import pearsonr,spearmanr # linear correlation
import matplotlib.pyplot as plt

def plot_array(L,val):
	"""
	Plot the graphical representation for array along
	with the corresponding value. 
	"""
	plt.plot(L,'.-')
	plt.axis([0, 300, 0, 300])
	plt.annotate(val,(200,270))
	plt.show()

def stability(L):
	"""
	A measure of 'stability' of input array L
	using Spearman linear correlation.
	Normalized result to [0,100] format.
	"""
	#~ corr1 = pearsonr(np.arange(L.shape[0]), L)
	corr2 = spearmanr(np.arange(L.shape[0]), L)
	
	#~ stdev = np.std(L)
	#~ rank = np.max(L) - np.min(L)
	#~ res = rank,stdev
	res = np.abs(corr2[0])*100
	
	return res
	

def percent(slope):
	"""
	Convert from a difference of array values
	to a [0,100] format.
	"""
	slope = np.degrees(np.arctan(slope))
	slope += 90
	slope = (slope * 5)/9
	return slope

def recent_performance(L,w):
	"""
	Recent performance value as 
	the difference of two last values
	of array.
	Normalized result to [0,100] format.
	"""
	delta = L[-1] - L[-2]
	
	if delta < 0:	# weak recent performance
		return percent(delta)*w
	return 0		# acceptable recent performance

def growth(L):
	"""
	Rate of growth, calculated taking the mean of all differences(slopes)
	on array.
	"""
	res = np.diff(L).mean()
	res = percent(res)
	return res

def GetScore(L):
	"""
	The main function.
	Returns the score of input based on 3 factors:
	stability, recent performance & rate of growth.
	"""
	st = stability(L)
	rp = recent_performance(L,0.1)
	gr = growth(L)
	return calc(st,rp,gr,0.5,0.02)
	
def calc(st,rp,gr,w1,w2):
	"""
	Utility function
	"""
	res = (st*w1 - rp)*gr*w2
	return res

