import random 
namesDict = {
	'bubs' : 0,
	'gage' : 0, 
	'wegs' : 0, 
	'bodn' : 0, 
	'ordo' : 0, 
	'rose' : 0, 
	'bail' : 0,
	'wolf' : 0,
	'qual': 0,
	'nips' : 0
}

h = 10
w = 10

board = [[0 for x in range(w)] for y in range(h)] 


for x in range(w):
	for y in range(h):
		run = True
		print "x = " + str(x)
		print "y= " + str(y)
		while (run):
			randInt = int(random.random() * 10)
			randKey = namesDict.keys()[randInt]
			if (namesDict[randKey] < 10):
				namesDict[randKey] += 1
				board[x][y] = randKey + "  "
				run = False


for x in namesDict.keys():
	print x + " " + str(namesDict[x])


print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in board]))



