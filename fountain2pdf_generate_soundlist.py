# coding=utf-8

import sys, os, fountain, yaml, re


DEFAULT_LOCATION = 'HOME'


class SFX(object):
	def __init__(self, scene, scenenumber, sound, number, locations=[],  comment='', done=False):
		self.scene = scene # string
		self.scenenumber = scenenumber # string
		self.sound = sound # string
		self.number = number # integer
		self.locations = [DEFAULT_LOCATION] if len(locations) == 0 else locations # array
		self.comment = comment # string
		self.done = done # bool

	def __str__(self):
		if not self.comment:
			tmp_comment = ''
		else:
			tmp_comment = ' (' + self.comment + ')'
		return str(self.number) + ' ' + ', '.join(self.locations) + ': ' + self.sound + tmp_comment

	def __repr__(self):
		if not self.comment:
			tmp_comment = ''
		else:
			tmp_comment = ' (' + self.comment + ')'
		return str(self.number) + ' ' + ', '.join(self.locations) + ': ' + self.sound + tmp_comment


def getSoundsFromFountain(fount):
	actual_scene = ''
	actual_scene_number = ''
	sound_number = 1
	output = []
	for f in fount.elements:

		# get actual scene name and number
		if f.element_type == 'Scene Heading':
			actual_scene = f.element_text
			actual_scene_number = f.scene_number

		# get the sound
		if f.element_type == 'Action' and not '*Musik:' in f.element_text:
			for sentence in re.split('(?<=[.!?]) +', f.element_text):
				output.append( SFX(actual_scene, actual_scene_number, sentence.strip(), sound_number) )
				sound_number += 1

	return output


def generateSoundlist(datei):
	WHITE = '\033[97m'
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	MAGENTA = '\033[95m'
	CYAN = '\033[96m'
	BOLD = '\033[1m'
	DIM = '\033[2m'
	GREY = '\033[90m'
	UNDERLINE = '\033[4m'
	CL_E = '\033[0m'

	path_to_project = os.path.dirname(os.path.realpath(__file__))

	# cancel if no file was given
	if not datei:
		print RED + 'No file given as parameter for generateSoundlist() function.' + CL_E
		return None

	# functions
	def get_categories(l):
		out = []
		for x in l:
			for y in x.locations:
				if not y in out:
					out.append( y )
		return out

	def get_id(array, scene, scenenumber, sound):
		out = [x.sound for x in array]
		for y, x in enumerate(array):
			if x.scene == scene and x.scenenumber == scenenumber and x.sound == sound:
				return y
		return 0


	# check if soundlist for this project already exists and load it, or make an empty one:
	liste_datei = datei.replace('.fountain', '.yaml')
	if os.path.isfile(liste_datei):
		d = open(liste_datei, 'r')
		liste = yaml.load(d.read())
		d.close()
	else:
		liste = []

	# load source file
	d = open(datei, 'r')
	F = fountain.Fountain(d.read())
	d.close()

	# get actual sounds from fountain and count amount of sounds
	sounds = getSoundsFromFountain(F)
	amount = len(sounds)



	# beginn
	print 'Computing ' + datei + ' ...'
	print '"exit" = exit, "skip" = continue last session'
	print '":[NUMBER]" = jump to number, "print" = output.'
	print 'Enter data like this:'
	print '     "LOCATION=COMMENT"'
	print '     "LOCATION, LOCATION 2=COMMENT"'
	print '     "LOCATION"'
	print '     "LOCATION, LOCATION 2"'
	print '     "=COMMENT"'
	print



	# update actual soundlist from opened fountain with saved YAML
	for x in liste:
		if x.scene in [s.scene for s in sounds] and x.scenenumber in [s.scenenumber for s in sounds] and x.sound in [s.sound for s in sounds]:
			i = get_id(sounds, x.scene, x.scenenumber, x.sound)
			sounds[i].locations = x.locations
			sounds[i].comment = x.comment
			sounds[i].done = True


	# asking user stuff and generating the list
	skip = False
	skipto = 0
	for x in sounds:
		# check if entry already exists in liste
		if skipto > 0 and skipto != x.number:
			done = True
			skip = True
		elif skipto == x.number:
			done = x.done
			skip = False
			skipto = 0
		else:
			done = x.done
			skipto = 0
		if skip and done:
			continue
		else:
			if done:
				default 	= ', '.join( x.locations )
				default_com	= x.comment
			else:
				default 	= DEFAULT_LOCATION
				default_com	= ''

		# ask user for categorization
		categories = get_categories( sounds )
		cats_string = ''
		for cats_count, cats in enumerate(categories):
			cats_string += cats + ' (' + str(cats_count+1) + ')'
			if cats_count+1 < len(categories):
				cats_string += ', '
		print GREY + 'Categories: ' + PURPLE + cats_string
		print GREY + 'Scene: ' + x.scene + ' #' + x.scenenumber + '#'
		print YELLOW + str(x.number) + '/' + str(amount) + ': ' + CYAN + x.sound
		skip = False
		user = raw_input(RED + 'Rec-Location [' + BLUE + default + '=' + default_com + RED + '] > ' + CL_E)
		if user == 'exit':
			print
			exit()
		elif user == 'skip':
			skip = True
		elif len(user) > 0 and user[0] == ':':
			try:
				skipto = int(user[1:])
			except Exception:
				skipto = 0
		elif user == 'print':
			break
		else:
			if '=' in user:
				comment = user.split('=')[1]
				user = user.split('=')[0]
			else:
				comment = default_com
			user = default if user == '' else user
			locations = []
			for locs in user.split(','):
				loc_user_input = locs.strip().upper()
				if re.match(r'(\d+)', loc_user_input):
					if len(categories) >= int(loc_user_input):
						locations.append( categories[ int(loc_user_input)-1 ] )
						continue
				locations.append( loc_user_input )

			# update sound
			x.locations = locations
			x.comment = comment
			x.done = True


			# save list
			d = open(liste_datei, 'w')
			d.write( yaml.dump(sounds) )
			d.close()
		print

	# return the soundlist
	return sounds