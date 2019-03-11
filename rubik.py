from baseconvert import base

t = {"L": 0, "F": 0, "R": 1, "B": 1, "U": 2, "L2": 2, "D": 3, "R2": 3, "F2": 4, "U2": 4, "B2": 5, "D2": 5, "L'": 6, "F'": 6, "R'": 7, "U'": 7, "B'": 8, "D'": 8}

s = ["B2 R U F' R' L' B B2 L F D D' R' F2 D' R R D2 B' L R",
"L' L B F2 R2 F2 R' L F' B' R D' D' F U2 B' U U D' U2 F'",
"L F' F2 R B R R F2 F' R2 D F' U L U' U' U F D F2 U R U' F U B2 B U2 D B F2 D2 L2 L2 B' F' D' L2 D U2 U2 D2 U B' F D R2 U2 R' B' F2 D' D B' U B' D B' F' U' R U U' L' L' U2 F2 R R F L2 B2 L2 B B' D R R' U L"]

permutation = []

for x in s[0].split(" "):
	permutation.append(t[x])
permutation = ''.join([str(x) for x in permutation])
permutation10 = base(int(permutation), 9, 10)
i = permutation10[0]
P = permutation10[i+1:i+10]
t2 = t.copy()
t3 = [x for x in t.keys()]
y = 0
for x in range(0, 17, 2):
	t2[t3[list(t.values()).index(P[y])]] = y
	t2[t3[list(t.values()).index(P[y])+1]] = y
	y+=1
second = []
for x in s[1].split(" "):
	second.append(t2[x])
second = ''.join([str(x) for x in second])
second10 = base(int(second), 9, 10)
j, k = second10[0], second10[1]
length = second10[2+j:2+j+k]
length = ''.join([str(x) for x in length])
test = []
for x in s[2].split(" ")[0:int(length)]:
	test.append(t2[x])
test = ''.join([str(x) for x in test])
test = "0"+base(int(test), 9, 2, string=True)
print(test)