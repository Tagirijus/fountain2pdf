# coding=utf-8

import fountain2pdf_style_radioplay as style # define your style here

import fountain2pdf_generate_soundlist
from fountain2pdf_2html import Fountain2HTML

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
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


def getCharacters(fount):
	chars = []

	# iterate through elements
	for f in fount.elements:
		if f.element_type == 'Character' and f.element_text.upper() not in chars:
			chars.append( f.element_text.upper() )

	return chars


def Fountain2PDF(fount, char=None):
	# generate filename
	if char and char.upper() in getCharacters(fount):
		char = char.upper()
		out_filename = PAR['file'].replace('.fountain', '_'+char.replace(' ', '_')+'.pdf')
		mark = True
	else:
		out_filename = PAR['file'].replace('.fountain', '.pdf')
		mark = False


	# generate doc and empty output-array
	doc = SimpleDocTemplate(out_filename, pagesize=A4, rightMargin=style.RIGHTMARGIN, leftMargin=style.LEFTMARGIN, topMargin=style.TOPMARGIN, bottomMargin=style.BOTTOMMARGIN)
	Story = []

	# iterate through every fountain element
	skip_empty_line = False
	mark_char = False
	section_count = 1
	scene_count = 1
	for f in fount.elements:

		# it is a section heading
		if f.element_type == 'Section Heading':
			# generate anchor for index linking for sections
			tmp_section_anchor = '<a name="section' + str(section_count) + '" />'
			section_count += 1
			Story.append(Paragraph( tmp_section_anchor + f.element_text, style.STYLE_SECTION_HEADING))
			skip_empty_line = False

		# it is a scene heading
		elif f.element_type == 'Scene Heading':
			# print scene number on the left, if enabled
			if style.SCENE_NUMBER_L:
				Story.append(Paragraph( f.scene_number, style.STYLE_SCENE_NUMBER_L))
			# get scene abbreviation and print it, if it is not a dot
			tmp_scene_abb = f.scene_abbreviation + ' ' if f.scene_abbreviation != '.' else ''
			# generate anchor for index linking for scenes
			tmp_scene_anchor = '<a name="scene' + str(scene_count) + '" />'
			scene_count += 1
			Story.append(Paragraph( tmp_scene_anchor + tmp_scene_abb + f.element_text, style.STYLE_SCENE_HEADING))
			# print scene number on the left, if enabled
			if style.SCENE_NUMBER_R:
				Story.append(Paragraph( f.scene_number, style.STYLE_SCENE_NUMBER_R))
			skip_empty_line = False

		# it is a comment / a note
		elif f.element_type == 'Comment':
			if PAR['notes']:
				Story.append(Paragraph( '[ ' + Fountain2HTML( f.element_text ) + ' ]', style.STYLE_COMMENT))
			else:
				skip_empty_line = True

		# it is action
		elif f.element_type == 'Action':
			Story.append(Paragraph( Fountain2HTML( f.element_text ), style.STYLE_ACTION))
			skip_empty_line = False

		# it is a character
		elif f.element_type == 'Character':
			if mark and f.element_text == char:
				Story.append(Paragraph( f.element_text, style.STYLE_CHARACTER_MARK))
				mark_char = True
			else:
				Story.append(Paragraph( f.element_text, style.STYLE_CHARACTER))
				mark_char = False
			skip_empty_line = False

		# it is a parenthetical
		elif f.element_type == 'Parenthetical':
			if mark and mark_char:
				Story.append(Paragraph( Fountain2HTML( f.element_text ), style.STYLE_PARENTHETICAL_MARK))
			else:
				Story.append(Paragraph( Fountain2HTML( f.element_text ), style.STYLE_PARENTHETICAL))
			skip_empty_line = False

		# it is dialogue
		elif f.element_type == 'Dialogue':
			if mark and mark_char:
				Story.append(Paragraph( Fountain2HTML( f.element_text ), style.STYLE_DIALOGUE_MARK))
			else:
				Story.append(Paragraph( Fountain2HTML( f.element_text ), style.STYLE_DIALOGUE))
			skip_empty_line = False

		# it is a transition
		elif f.element_type == 'Transition':
			Story.append(Paragraph( f.element_text, style.STYLE_TRANSITION))
			skip_empty_line = False

		# it is an empty line
		elif f.element_type == 'Empty Line':
			if style.PRINT_EMPTY_LINES and not skip_empty_line:
				Story.append(Paragraph('&nbsp;', style.STYLE_EMPTY_LINE))
				skip_empty_line = False

		# it is a page break
		elif f.element_type == 'Page Break':
			Story.append(PageBreak())
			skip_empty_line = False

		# it is a synopsis
		elif f.element_type == 'Synopsis':
			# TO DO !!!
			pass
			#skip_empty_line = False

		# it is a boneyard
		elif f.element_type == 'Boneyard':
			# TO DO !!!
			pass
			#skip_empty_line = False

	# get title and save to PDF
	doc.title = PAR['file'].replace('.fountain', '')
	doc.build(Story)







# START THE PROGRAMM

# get parameter settings
PAR = getProgrammParameters(sys.argv)

# get fountain file
d = open(PAR['file'], 'r')
F = fountain.Fountain( d.read() )
d.close()


# check if it should output soundlist or not
if PAR['soundlist']:
	print 'Soundlist generating still in development.'

# do normal script rendering
else:

	# check if it should output all characters automatically or not
	if PAR['char'] == 'all':
		Fountain2PDF(F)
		for x in getCharacters(F):
			Fountain2PDF(F, x)

	# make a single script render
	else:
		Fountain2PDF(F, PAR['char'])



# TODO: SOUNDLIST
# for x in fountain2pdf_generate_soundlist.generateSoundlist(PAR['file']):
# 	print x