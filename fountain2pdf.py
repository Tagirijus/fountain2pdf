# coding=utf-8

import fountain2pdf_style_radioplay as style # define your style here

import fountain2pdf_generate_soundlist
from fountain2pdf_2html import Fountain2HTML

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4

import sys, os, fountain



path_to_project = os.path.dirname(os.path.realpath(__file__))



# functions

def getProgrammParameters(arr):
	# possible parameters:
	# 1st parameter: filename of the source fountain file
	# -c / -char ["Character Name" / "all"] --> marks one char or all in seperate files
	# -n / -notes --> enables output for comments/notes
	# -s / -soundlist --> outputs a soundlist only
	# -i / -index --> enables first page as index of sections and scenes
	# -d / -numbers --> enables numbers on the sounds / action sentences

	# quit, if there is not at least one parameter
	if len(arr) < 2:
		print 'At least one parameter needed: source fountain file.'
		exit()

	# quit, if the given parameter is not a file
	if not os.path.isfile(arr[1]):
		print arr[1] + ' is not a valid file.'
		exit()

	# check parameters and assign default values
	output = {}

	# the file
	output['file'] = arr[1]

	# the characters
	if '-c' in arr:
		try:
			output['char'] = arr[arr.index('-c')+1]
		except Exception:
			output['char'] = None
	elif '-char' in arr:
		try:
			output['char'] = arr[arr.index('-char')+1]
		except Exception:
			output['char'] = None
	else:
		output['char'] = None

	# the notes
	if '-n' in arr or '-notes' in arr:
		output['notes'] = True
	else:
		output['notes'] = False

	# the soundlist
	if '-s' in arr or '-soundlist' in arr:
		output['soundlist'] = True
	else:
		output['soundlist'] = False

	# the index
	if '-i' in arr or '-index' in arr:
		output['index'] = True
	else:
		output['index'] = False

	# the nubers
	if '-d' in arr or '-nubers' in arr:
		output['nubers'] = True
	else:
		output['nubers'] = False

	# return the output
	return output


def zero(number, total):
	# number has 1 digit
	if number < 10:
		if total > 9999:
			return '0000' + str(number)
		elif total > 999:
			return '000' + str(number)
		elif total > 99:
			return '00' + str(number)
		elif total > 9:
			return '0' + str(number)
		else:
			return str(number)

	# number has 2 digits
	elif number < 100:
		if total > 9999:
			return '000' + str(number)
		elif total > 999:
			return '00' + str(number)
		elif total > 99:
			return '0' + str(number)
		else:
			return str(number)

	# number has 3 digits
	elif number < 1000:
		if total > 9999:
			return '00' + str(number)
		elif total > 999:
			return '0' + str(number)
		else:
			return str(number)

	# number has 4 digits
	elif number < 10000:
		if total > 9999:
			return '0' + str(number)
		else:
			return str(number)






# START THE PROGRAMM
PAR = getProgrammParameters(sys.argv)

# for x in fountain2pdf_generate_soundlist.generateSoundlist(PAR['file']):
# 	print x

print Fountain2HTML('Hallo hier ist der Manuel!')




exit()
# TEST HERE

# generate doc
doc = SimpleDocTemplate("test.pdf", pagesize=A4, rightMargin=65, leftMargin=65, topMargin=65, bottomMargin=65)

# fill document
Story = []

Story.append(Paragraph('<u><a href="#scene 1">Alien (Ernst)</a></u>', style.STYLE_SECTION_HEADING))
Story.append(Paragraph('1', style.STYLE_SCENE_NUMBER_L))
Story.append(Paragraph('Station', style.STYLE_SCENE_HEADING))
Story.append(Paragraph('1', style.STYLE_SCENE_NUMBER_R))
Story.append(Paragraph('<b>(01)</b> Man hört von draußen einen eisigen Windsturm und die Tür wird geschlossen. <b>(02)</b> Mark kommt näher und legt einen schweren Kasten hart auf den Tisch, zieht sich aus und setzt sich dann. <b>(03)</b> Er schaltet ein Aufnahmegerät ein.', style.STYLE_ACTION))
Story.append(Paragraph('Mark', style.STYLE_CHARACTER))
Story.append(Paragraph('(hektisch)', style.STYLE_DIALOG))
Story.append(Paragraph('15:34 Uhr: Ich habe neue Proben aus der Bohrung geholt und beginne jetzt mit den ersten Untersuchungen.', style.STYLE_DIALOG))
Story.append(Paragraph('&nbsp;', style.STYLE_DIALOG))
Story.append(Paragraph('Cut to:', style.STYLE_TRANSITION))
Story.append(Paragraph('2', style.STYLE_SCENE_NUMBER_L))
Story.append(Paragraph('Draussen', style.STYLE_SCENE_HEADING))
Story.append(Paragraph('2', style.STYLE_SCENE_NUMBER_R))
Story.append(Paragraph('<b>(04)</b> Eine neue Szene beginnt jetzt <a name="scene 1" />hier!', style.STYLE_ACTION))


# finally build the document and save it
doc.title = 'Alien (Ernst)'
doc.build(Story)