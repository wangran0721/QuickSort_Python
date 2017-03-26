def partition(a,left,right):
	pValue = a[right]
	storeIndex = left
	for i in range(left,right):
		if a[i] < pValue:
			a[storeIndex],a[i] = a[i],a[storeIndex]
			storeIndex += 1
	pValue,a[storeIndex] = a[storeIndex],pValue
	return storeIndex

def quicksort(a,left,right):
	while left < right:
		pivotNewIndex = partition(a,left,right)
		quicksort(a,left,pivotNewIndex-1)
		quicksort(a,pivotNewIndex+1,right)
