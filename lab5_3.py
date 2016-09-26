def super_fibonacci(n, m):
	series=[]
	for i in range(m):
		series.append(1)
	for i in range(m,n):
		series_value=0
		for j in range(1,m+1):
			series_value=series_value+series[i-j]
		series.append(series_value)
	return series[n-1]

print(super_fibonacci(9,3))