# coding=utf-8

import re

class Italic(object):

	parse_re = re.compile(
		# one star
		r'\*'
		# anything but a space, then text
		r'([^\s].*?)'
		# finishing with one star
		r'\*'
		# must not be followed by star
		r'(?!\*)'
	)

	start_html = '<em>'
	end_html = '</em>'


class Bold(object):

	parse_re = re.compile(
		# two stars
		r'\*\*'
		# must not be followed by space
		r'(?=\S)'
		# inside text
		r'(.+?[*_]*)'
		# finishing with two stars
		r'(?<=\S)\*\*'
	)

	start_html = '<strong>'
	end_html = '</strong>'


class BoldItalic(object):

	parse_re = re.compile(
		# three stars
		r'\*\*\*'
		# must not be followed by space
		r'(?=\S)'
		# inside text
		r'(.+?[*_]*)'
		# finishing with three stars
		r'(?<=\S)\*\*\*'
	)

	start_html = '<strong><em>'
	end_html = '</em></strong>'


class Underline(object):

	parse_re = re.compile(
		# underline
		r'_'
		# must not be followed by space
		r'(?=\S)'
		# inside text
		r'([^_]+)'
		# finishing with underline
		r'(?<=\S)_'
	)

	start_html = '<u>'
	end_html = '</u>'


styles = (BoldItalic, Bold, Italic, Underline)

def Fountain2HTML(text):
	out = text
	for x in styles:
		out = x.parse_re.sub(x.start_html + r'\1' + x.end_html , out)
	return out