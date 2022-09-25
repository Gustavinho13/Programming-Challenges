N = int(input())

inputs = []

for i in range(N):
	inputs.append(input().split(" "))

for i in range(len(inputs)):
	if int(inputs[i][0]) * int(inputs[i][1]) == int(inputs[i][2]):
		print("POSSIBLE DOUBLE SIGMA")
		continue
	print("16 BIT S/W ONLY")