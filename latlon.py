#!/usr/bin/env python
import re

def decimalat(DegreeString):

		SearchString = '(\d+) ([\d\.]+) (\w)'
		Result = re.search(SearchString, ElementList[2])

		Degree=float(Result.group(1))
		Minute=float(Result.group(2))
		print ('min',Minute)
		Compass=Result.group(3)
		DecimalDegree=Degree+Minute/60
		
		if Compass in 'SW':
			DecimalDegree=-DecimalDegree
		return DecimalDegree

InFileName = 'Marrus_claudanielis.txt'

InFile = open(InFileName, 'r')

LineNumber = 0

for Line in InFile:
	Line = Line.strip()

	if LineNumber > 0:
		ElementList = Line.split('\t')
		print('Depth:{}, Lat:{}, Lon:{}'.format(ElementList[4], ElementList[2], ElementList[3]))

		latitude = decimalat (ElementList[2])

		print (latitude)

	LineNumber = LineNumber + 1

InFile.close()