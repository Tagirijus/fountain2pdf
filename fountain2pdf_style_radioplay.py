# coding=utf-8

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.colors import lightgrey, grey

# settings and style

FONT = 'Helvetica'
FONTITALIC = 'Helvetica-Oblique'
FONTBOLD = 'Helvetica-Bold'
SIZE = 14
INDENT_LEFT = 28
INDENT_RIGHT = 28
PRINT_EMPTY_LINES = True

RIGHTMARGIN = 65
LEFTMARGIN = 65
TOPMARGIN = 65
BOTTOMMARGIN = 65

SCENE_NUMBER_L = True
SCENE_NUMBER_R = True

STYLE_SECTION_HEADING = ParagraphStyle(
	'Section Heading',
	fontName=FONT,
	fontSize=int(SIZE*1.4),
	leading=int(SIZE*1.4*1.125),
	alignment=TA_CENTER
	)

STYLE_SCENE_NUMBER_L = ParagraphStyle(
	'Scene Number Left',
	fontName=FONTBOLD,
	fontSize=SIZE,
	leading=0,
	textTransform='uppercase'
	)

STYLE_SCENE_HEADING = ParagraphStyle(
	'Scene Heading',
	fontName=FONTBOLD,
	fontSize=SIZE,
	leading=0,
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
	textTransform='uppercase'
	)

STYLE_SCENE_NUMBER_R = ParagraphStyle(
	'Scene Number Right',
	fontName=FONTBOLD,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	alignment=TA_RIGHT,
	textTransform='uppercase'
	)

STYLE_COMMENT = ParagraphStyle(
	'Comment',
	fontName=FONTITALIC,
	fontSize=int(SIZE*0.7),
	leading=int(SIZE*0.7),
	leftIndent=int(SIZE*6),
	rightIndent=int(SIZE*6),
	textColor=grey,
	alignment=TA_CENTER
	)

STYLE_ACTION = ParagraphStyle(
	'Action',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5),
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

STYLE_PARENTHETICAL = ParagraphStyle(
	'Parenthetical',
	fontName=FONTITALIC,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5)+int(SIZE*1.8),
	rightIndent=int(SIZE*2.5)
	)

STYLE_PARENTHETICAL_MARK = ParagraphStyle(
	'Parenthetical Mark',
	fontName=FONTITALIC,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5)+int(SIZE*1.8),
	rightIndent=int(SIZE*2.5),
	backColor=lightgrey
	)

STYLE_DIALOGUE = ParagraphStyle(
	'Dialogue',
	fontName=FONT,
	fontSize=SIZE,
	leading=int(SIZE*1.125),
	leftIndent=int(SIZE*2.5)+int(SIZE*1.8),
	rightIndent=int(SIZE*2.5)
	)

STYLE_DIALOGUE_MARK = ParagraphStyle(
	'Dialogue Mark',
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
	textTransform='uppercase',
	textColor=grey,
	alignment=TA_CENTER
	)

STYLE_EMPTY_LINE = ParagraphStyle(
	'Empty Line',
	fontName=FONT,
	fontSize=SIZE,
	leading=SIZE,
	leftIndent=int(SIZE*2.5),
	rightIndent=int(SIZE*2.5)
	)