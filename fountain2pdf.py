# coding=utf-8

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import lightgrey, grey

# settings and style

FONT = 'Helvetica'
SIZE = 14
INDENT_LEFT = 28
INDENT_RIGHT = 28


STYLE_SECTION_HEADING = ParagraphStyle(
	'Section Heading',
	fontName=FONT,
	fontSize=int(SIZE*1.4),
	leading=int(SIZE*1.4*1.125),
	alignment=TA_CENTER,
	spaceAfter=int(SIZE*1.4)
	)

STYLE_SCENE_NUMBER_L = ParagraphStyle(
	'Scene Number Left',
	fontName=FONT+'-Bold',
	fontSize=SIZE,
	leading=0,
	textTransform='uppercase'
	)

STYLE_SCENE_HEADING = ParagraphStyle(
	'Scene Heading',
	fontName=FONT+'-Bold',
	fontSize=SIZE,
	leading=0,
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	textTransform='uppercase'
	)

STYLE_SCENE_NUMBER_R = ParagraphStyle(
	'Scene Number Right',
	fontName=FONT+'-Bold',
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	spaceAfter=SIZE,
	alignment=TA_RIGHT,
	textTransform='uppercase'
	)

STYLE_ACTION = ParagraphStyle(
	'Action',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	spaceAfter=SIZE,
	textColor=grey
	)

STYLE_CHARACTER = ParagraphStyle(
	'Character',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	textTransform='uppercase'
	)

STYLE_CHARACTER_MARK = ParagraphStyle(
	'Character_Mark',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	textTransform='uppercase',
	backColor=lightgrey
	)

STYLE_DIALOG = ParagraphStyle(
	'Dialog',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5)+int(SIZE*1.8),
	rightIndent=int(SIZE*2.5)
	)

STYLE_DIALOG_MARK = ParagraphStyle(
	'Dialog Mark',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5)+int(SIZE*1.8),
	rightIndent=int(SIZE*2.5),
	backColor=lightgrey
	)

STYLE_TRANSITION = ParagraphStyle(
	'Transition',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	spaceAfter=int(SIZE),
	textTransform='uppercase',
	textColor=grey
	)


# generate doc
doc = SimpleDocTemplate("test.pdf", pagesize=A4, rightMargin=65, leftMargin=65, topMargin=65, bottomMargin=65)

# fill document
Story = []

Story.append(Paragraph('<u>Alien (Ernst)</u>', STYLE_SECTION_HEADING))
Story.append(Paragraph('1', STYLE_SCENE_NUMBER_L))
Story.append(Paragraph('Station', STYLE_SCENE_HEADING))
Story.append(Paragraph('1', STYLE_SCENE_NUMBER_R))
Story.append(Paragraph('<b>(01)</b> Man hört von draußen einen eisigen Windsturm und die Tür wird geschlossen. <b>(02)</b> Mark kommt näher und legt einen schweren Kasten hart auf den Tisch, zieht sich aus und setzt sich dann. <b>(03)</b> Er schaltet ein Aufnahmegerät ein.', STYLE_ACTION))
Story.append(Paragraph('Mark', STYLE_CHARACTER))
Story.append(Paragraph('(hektisch)', STYLE_DIALOG))
Story.append(Paragraph('15:34 Uhr: Ich habe neue Proben aus der Bohrung geholt und beginne jetzt mit den ersten Untersuchungen.', STYLE_DIALOG))
Story.append(Paragraph('&nbsp;', STYLE_DIALOG))
Story.append(Paragraph('Cut to:', STYLE_TRANSITION))
Story.append(Paragraph('2', STYLE_SCENE_NUMBER_L))
Story.append(Paragraph('Draussen', STYLE_SCENE_HEADING))
Story.append(Paragraph('2', STYLE_SCENE_NUMBER_R))
Story.append(Paragraph('<b>(04)</b> Eine neue Szene beginnt jetzt hier!', STYLE_ACTION))


# finally build the document and save it
doc.title = 'Alien (Ernst)'
doc.build(Story)