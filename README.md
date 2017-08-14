# Otubuilder

Otubuilder will generate slightly altered copies from input sequences.
Input will be a fasta (uni-line, where one line is heading and another sequence)
and another file containing desired number of copies for each sequence in fasta file.

The first version of otubuilder will generate copies that are 0-3 percent different
from original sequence where difference is calculated simply as a base substitution or
a deletion event - gaps created by deletion events will be limited to 2-3 bases.




