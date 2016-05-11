# $ python sample.py
import json


def load_json():
	with open('geodata.min.json') as datafile:
		data = json.load(datafile)
	return data


def showCountry(data, country, state):
	for c in data:
		if c[0] == country:
			print str(c[0])+' has a total of '+ str(len(c[1])) + ' states and provinces'

			for s in c[1]:
				if s[0] == state:
					print 'The state/province of '+str(s[0])+' has '+ str(len(s[1]))+ ' districts'



if __name__ == '__main__':
	data = load_json()
	showCountry(data, 'India', 'Kerala')
