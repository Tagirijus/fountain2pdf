# Fountain parser

## About

This python script contains a renderer `fountain2pdf.py` , which converts .fountain files to .pdf files using the python library [Reportlab](https://pypi.python.org/pypi/reportlab).

## Install

You need the `fountain` parser installed as a python3 library in the system. You can find it here: https://github.com/Tagirijus/fountain.

## Usage

To convert a fountain file into pdf you simply can use this script like this:

	python fountain2pdf.py [FOUNTAIN-FILE]

This already renders your fountain script into a PDF. You can add the parameter `-h` or `-help` to get an verview of possible parameters. For example: you can mark a specific character, which will get greyed background for easy identification in the readin of the whole script with `-c/-char [CHARACTER NAME]`. If the character is called "Manuel Senfft" you would type:

	python fountain2pdf.py the_script.fountain -c "Manuel Senfft"

This will generate a PDF with a slightly different output name than the original: it will add _CHARACTERNAME to the file name. `the_script.fountain` will become `the_script_MANUEL_SENFFT.pdf` in the above case.

The parameter `-co` or `-char-only` will make a similar rendering. Instead of giving the character grey background (or another background like set up in the specific style.py), it will ONLY render the characters text.

The parameter `-n` or `-notes` will enable the rnedering for the fountain notes. Otherwise they will not be rendered!

The parameter `-i` or `-index` will generate some kind of index with hyper links to the acts and scenes and stuff. Could be buggy though. Use with care.

The parameter `-d` or `-numbers` and the parameter `-s` or `-soundlist` are some personal parameters. They are for my personal workflow of radio play production. The first mentioned parameter numbers all the action sentences in the script with ascending numbers. The other parameter starts another script with which I can generate a soundlist and categorize sounds I would have to record for my radio play.

## Additional information

First I did not want to make this script public, but now I did. Keep in mind that I do not have that much time for improving things a lot or writing good documentation about these scripts. I primary made the scripts for my personal workflow.

Speaking of my personal workflow: take a look at [Fountainhead](https://github.com/derickc/Fountainhead). It is a sublime text plugin and script highlighting I am working with. It is really great and you should not miss it, when you like to write scripts with fountain syntax!

## ToDo

Rewrite everything in Python 3 with flake8 style guide enforcement ...
