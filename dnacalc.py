#!/usr/bin/env python

# This is a comment

DNAseq = 'ATGAAC'

print( 'Sequence ' + DNAseq )

SeqLength = float (len( DNAseq ))

print( 'Length is ' + str(SeqLength) )

NumberA = DNAseq.count('A')

NumberT = DNAseq.count('T')

NumberC = DNAseq.count('C')

NumberG = DNAseq.count('G')

print('A: ' + str( NumberA / SeqLength ) )

print('T: ' + str( NumberT / SeqLength ) )

print('C: ' + str( NumberC / SeqLength ) )

print('G: ' + str( NumberG / SeqLength ) )

