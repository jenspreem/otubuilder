#mutation percentage lets say hardcoded 0 to 3 we do a "species" analysis
read seq
seq len
calc substitutions needed to get 3 perc
rand(0...3)=x
if x==0 print seq
else while x>0
#randomly choose either substitution or deletion in seq
 if rand(0..1)==0 
  seq=substitute(seq,rand(len(seq)))
 if rand(0..1)==1
  seq=delete(seq,rand(len(seq)))
 x=x-1
print seq

#we do all of the above for single sequence n times where n is pulled
#from a list of numbers (so we can give different abundance for each generated "species")



