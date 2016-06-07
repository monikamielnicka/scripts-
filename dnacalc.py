#!/usr/bin/env python

# This is a comment

#DNAseq = raw_input ( "Enter a DNA sequence" ).upper()
#DNAseq = DNAseq.upper ()

DNAseq='AATGGGGCCCGTAACGTACA'

print('Sequence ' + DNAseq )

SeqLength =float(len( DNAseq ))

print('Length is ' + str(SeqLength) )

#for bases in Bases
TotalStrong=0
TotalWeak=0


Bases='AGTC'
for base in Bases:
	frequency=(DNAseq.count (base)) / SeqLength
	print( '{}: {:.2}'.format (base, frequency))
	
for base in DNAseq:
	if base in 'CG':
		TotalStrong=TotalStrong+1
	else:
		TotalWeak=TotalWeak+1
		

print (TotalStrong, TotalWeak)

Counts = dict ()
for base in Bases
	Count = DNAseq.count (base)
	Counts[base] = Counts

if SeqLength>=14:
	MeltTemp=64.9 + 41 * (TotalStrong - 16.4) / SeqLength 
	print('using long formula')

else: 
	
	MeltTemp=(4*TotalStrong)+(2*TotalWeak)
	print('using short formula')

print('Melting temp: {}'.format(MeltTemp))
	

print('Done.')