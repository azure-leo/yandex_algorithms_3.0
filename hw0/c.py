# Коллекционер Диего
# Диего увлекается коллекционированием наклеек. На каждой из них написано число,
# и каждый коллекционер мечтает собрать наклейки со всем встречающимися числами
# Диего собрал N наклеек, некоторые из которых, возможно, совпадают
# Как-то раз к нему пришли K коллекционеров. i-й из них собрал все 
# наклейки с номерами не меньшими, чем pi

# Напишите программу, которая поможет каждому из коллекционеров 
# определить, сколько недостающих ему наклеек есть у Диего. Разумеется,
# гостей Диего не интересуют повторные экземпляры наклеек

n = int(input())

diego = map(int, input().split())

k = int(input())

coll = list(map(int, input().split()))

diego = list(set(diego))

diego.sort()

# diego = [10, 20, 30, 40, 50]
#           0   1   2   3  4   l5   6   7   8    9
# coll = [50]
#print(diego)


for i in range(0, k):
	l = 0
	r = len(diego) - 1
	mid = 0
	nothing = False
	while(l <= r):
		mid = (l + r) // 2
		if(diego[mid] < coll[i] and mid+1 > r):
			mid += 1
			break
		elif(diego[mid] < coll[i]):
			l = mid + 1
		elif(diego[mid] > coll[i]):
			r = mid - 1
		elif(diego[mid] == coll[i]):
			break
	ans = mid
	print(ans)
