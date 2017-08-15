#!/usr/bin/python

import sys
from operator import itemgetter
from random import randint


def substitute(char):
	#i'll set transition/transversion ration as 2:1
	if char=="A":
		if randint(0,3)==0:
			return "C" if randint(0,1)==0 else "T"
		else: return "G"
	if char=="G":
		if randint(0,3)==0:
			return "C" if randint(0,1)==0 else "T"
		else: return "A"
	if char=="C":
		if randint(0,3)==0:
			return "G" if randint(0,1)==0 else "A"
		else: return "T"
	if char=="T":
		if randint(0,3)==0:
			return "G" if randint(0,1)==0 else "A"
		else: return "C"

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
# todo - theres some control flow problem last name seq pair gets run with substitutions==0 from the end of the else statement below
# why doesn't it calculate it from the seq?
	name = f.readline().strip()
	seq = f.readline().strip()

	if not name: break
	if not seq: break

	#calc substitutions needed to get 3 perc
	# should we use integer division that rounds up or down?
	# i'll use one that rounds down so we get stuff under 3 percent
	# x=((len(seq)*3)+100//2)//100 would round up this would mean some go over 3
	x=len(seq)*3/100
	substitutions=randint(0, x)#lets make 0 to 3 perc difference then
	print "x"+str(x)
	print "subnr"+str(substitutions)
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
				del_loc=randint(0,len(seq)-1)
				seq = seq[:del_loc] + seq[del_loc+3:]#what if del_loc is in last 2 bp?
				print "del"
				substitutions=substitutions-1
			else : #do subs
				sub_loc=randint(0,len(seq)-1)
				subnt=substitute(seq[sub_loc])
				seq = seq[:sub_loc] + subnt + seq[sub_loc+1:]#what if subnt is the last nucleotide?
				print "sub"
				substitutions=substitutions-1
	print name
	print seq

f.close()
