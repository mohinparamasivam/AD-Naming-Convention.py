
#!/usr/bin/python3

import os


file = open("/root/HTB/sauna/users","r")

file_write = open("/root/HTB/sauna/wordlist","a+")

for i in file :

	#combine first and lastname lowercase

	firstname_1 = i.split()[0].lower()
	lastname_1 = i.split()[1].lower()
	combined_1 = firstname_1+lastname_1
	file_write.write(combined_1+"\n")

	#initial of first name combined with complete lastname

	initial = i[0].lower()
	lastname_2 = i.split()[1].lower()
	combined_2 = initial+lastname_2
	file_write.write(combined_2+"\n")

	#combined first 3 characters of firstname and first 3 characters of lastname
	firstname_3 = i[0:3].lower()
	lastname_3 = i.split()[1][0:3].lower()
	combined_3 = firstname_3+lastname_3
	file_write.write(combined_3+"\n")

'''
	# combine 3 letters of firstname and 3 random numbers 

	firstname_4 = i[0:3].lower()

	#use crunch to generate random numbers behind each usernames

	os.system("crunch 6 6 " + "0123456789 " + "-t " + firstname_4+"%%%"+" -o /root/HTB/sauna/crunch_"+firstname_4)

	file_crunch = open("/root/HTB/sauna/crunch_"+firstname_4,"r")

	for content in file_crunch:

		file_write.write(content)


'''