#!/usr/bin/python

import sys
from operator import itemgetter
from random import randint

#list to store wanted copy-numbers
copynr_list=[]
#populate from  file
with open(str(sys.argv[2]), 'r') as fi:
	for line in fi:
		line=line.rstrip()
		copynr_list.append(line)


f=open(str(sys.argv[1]), 'r')
#lets loop the fasta file
while True:

# todo - count the names/seqs so you could do the copies by copienumber
	name = f.readline().strip()
	seq = f.readline().strip()
	if not name: break

	#calc substitutions needed to get 3 perc
	# should we use integer division that rounds up or down?
	# i'll use one that rounds down so we get stuff under 3 percent
	# x=((len(seq)*3)+100//2)//100 would round up this would mean some go over 3
	x=len(seq)*3/100
	substitutions=randint(0, x)#lets make 0 to 3 perc difference then

	if substitutions==0:
		print "nosub"
		print name
		print seq
		continue
	else:

		while (substitutions>0):
		#randomly choose either  deletion or substitution in your seq
		# right now 1:6 will be our indel/subs ratio 
		# https://academic.oup.com/mbe/article/26/7/1523/1120476/Variation-in-the-Ratio-of-Nucleotide-Substitution
		# guess rRNA could be lumped to noncoding as you won't get the negative selection of indels that are non 3 divisible
		# right now my indels are all 3bp dels
			if randint(0,5)==0: #do dels
				del_loc=randint(0,len(seq))
				seq = seq[:del_loc] + seq[del_loc+3:]
				print "del"
			else : #do subs
				sub_loc=randint(0,len(seq))
				subnt="A" #make the substitution table
				seq = seq[:sub_loc] + "A" + seq[sub_loc+1:]
				print "sub"
			substitutions=substitutions-1
	print name
	print seq

f.close()
