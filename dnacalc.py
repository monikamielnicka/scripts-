#!/usr/bin/env python

# This is a comment

#DNAseq = raw_input ( "Enter a DNA sequence" ).upper()
#DNAseq = DNAseq.upper ()

DNAseq='AATGGGGCCCGTAACGTACA'

print('Sequence ' + DNAseq )

SeqLength =float(len( DNAseq ))

print('Length is ' + str(SeqLength) )


NumberA= DNAseq.count ('A')

NumberT= DNAseq.count ('T')

NumberC= DNAseq.count ('C')

NumberG= DNAseq.count ('G')


print('A:{:.2}'.format(NumberA / SeqLength))

print('T:{:.2}'.format(NumberT / SeqLength))

print('C:{:.2}'.format(NumberC / SeqLength))

print('G:{:.2}'.format(NumberG / SeqLength))

TotalStrong=NumberG + NumberC
TotalWeak=NumberA + NumberT

if SeqLength>=14:
	MeltTemp=64.9 + 41 * (TotalStrong - 16.4) / SeqLength 
	print('using long formula')

else: 
	
	MeltTemp=(4*TotalStrong)+(2*TotalWeak)
	print('using short formula')

print('Melting temp: {}'.format(MeltTemp))
	

print('Done.')