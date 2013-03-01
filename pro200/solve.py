import socket
import time 

def cubeEnding(sequence, ending):
	i = 0
	cube = 0
	count = 0
	while(count != sequence):
		i += 1
		cube = i**3
		if(str(cube).endswith(str(ending))):
			count += 1
	return i

def getSequenceNumber(question):
	#chop off the begining
	question = question[21:]

	seqString = ""
	i = 0
	char = question[i]
	while(char.isdigit()):
		char = question[i]
		if(char.isdigit()):
			seqString += char
		i += 1
	return int(seqString)

def getEnding(question):
	#find "digits"
	index = question.find("digits ")
	index += 7
	return int(question[index:index+3])
	
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("nullcon-e1.no-ip.org", 2000))

intro = s.recv(1024);
intro2 = s.recv(79);

for i in range(1, 100):
	print "i: " + str(i)
	question = s.recv(1024);
	if(i > 1):
		question += s.recv(1024);
		question = question[2:]
	print question
	sequence = getSequenceNumber(question)
	ending = getEnding(question)
	print sequence
	print ending
	answer = cubeEnding(sequence, ending)
	print answer
	s.sendall(str(answer) + "\n")


