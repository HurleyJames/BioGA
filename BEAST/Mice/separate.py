def parity_separation(infile, outfile1, outfile2):
	
	inopen = open(infile, 'r')
	outopen1 = open(outfile1, 'w')
	outopen2 = open(outfile2, 'w')
	lines = inopen.readlines()
	i = 0
	for line in lines:
		i += 1
		if i % 2 == 0:
			outopen1.write(line)
		else:
			outopen2.write(line)
	
	inopen.close()
	outopen1.close()
	outopen2.close()
	
# outopen1 represent prey, outopen2 represent predator
parity_separation("chase.txt", "chase_prey.txt", "chase_pred.txt")
