# -*- coding: utf-8 -*-
#%%
"""
Created on Sun Aug 23 17:06:37 2020
split off on Thu Jan 27 05:53 2022
Updated and last run on 2022-11-28

@author: RobertWinslow

The first version of this code was meant to scrap the unicode emoji list 
and place the emoji codepointss into a dictionary.

This is a modification that I made to generate a markdown-formatted table for display on github pages.
"""

import urllib.request
from bs4 import BeautifulSoup

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#%% Grab the info

def urlToStr(url):
    "This function returns a webpage's source as just a big ol' string."
    #load Url text
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    urlStr = mybytes.decode("utf8")
    fp.close()  
    return urlStr

#sourceUrl = "https://www.unicode.org/Public/emoji/14.0/emoji-test.txt"
#sourceUrl = "https://www.unicode.org/Public/emoji/13.1/emoji-test.txt"
#sourceUrl = "https://www.unicode.org/Public/emoji/13.0/emoji-test.txt"
sourceUrl = "https://www.unicode.org/Public/emoji/15.0/emoji-test.txt"
sourceStr = urlToStr(sourceUrl)
sourceLines = sourceStr.split('\n')


#%% Jankily parse the info to create a list of tuples
# format is (group, subgroup, codepoint, shortname, version)

emojilist = []
currentGroup = ''
currentSubgroup = ''

for line in sourceLines:
    #If a line gives us a group or subgroup name, change the cooresponding variable
    if line.startswith('# group: '):
       currentGroup = line[9:]
    elif line.startswith('# subgroup: '):
       currentSubgroup = line[12:]
    #Now we need to parse the nonempty lines which start with a unicode code point.
    elif (line != '' and line[0] !='#'):
        #only add to the list if the character is 'fully-qualified'
        #statussnippet = line[57:62] only works for 13.1 onwards
        statsnipstart = line.index(';') + 2
        statussnippet = line[statsnipstart:statsnipstart+5] 
        if statussnippet != 'fully':
            continue
        else:
            #strip out the codepoint
            codepoint = line[:line.index(';')].rstrip()
            #pull out the CLDR short name, which occurs after E#.# 
            shortname = line[line.index('.'):].lstrip('1234567890. ')
            # I also want to version number so missing characters don't jank things up
            suffix = line[line.index('#'):]
            version = int(suffix[suffix.index('E')+1:suffix.index('.')])
            #exclude the skin tone variants, because that adds 1699 entries (nearly half of them!).
            if 'skin tone' in shortname:
                #if ' 200D ' in codepoint: #ZWJ
                #if len(codepoint.split()) > 1:
                continue
            else:
                #now add it to our list
                emojilist.append((currentGroup, currentSubgroup, codepoint, shortname, version))
        


# %% scan a font file to get a list of supported codepoints.

from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode

font = TTFont('EmojiTwoCOLRv0.ttf')

# Eh, this doesn't seem like it's reading the multiple codepoint characters. 
# https://stackoverflow.com/questions/47948821/python-imagefont-and-imagedraw-check-font-for-character-support
# I'll just need to scrape the folder.


#%% get a list of emojis from a folder

import os
def parsefolder(foldername):
    files = os.listdir(foldername)
    #print(files)
    emojiset = set()
    for filename in files:
        if filename.endswith('.svg'):
            filename = filename[:-4].upper().replace('-',' ')
            emojiset.add(filename)
    return emojiset


#%% Build the Markdwon tables v2.
# This time, we are checking sets instead of just the version.

def codepoint_to_string(codepoint):
    hexcodes = codepoint.split()
    glyph = ''.join(chr(int(hexcode,16)) for hexcode in hexcodes)
    return glyph

def codepoint_to_html(codepoint):
    hexcodes = codepoint.split()
    html = ''.join("&#x"+hexcode+";" for hexcode in hexcodes)
    return html

def checkforcodepoint(emojiset,codepoint):
    if codepoint in emojiset:
        return True
    elif codepoint.replace(' FE0F','').replace(' 200D','') in emojiset:
        return True
    else:
        return False

# data for versions of columns
COLUMNVERSIONS = [13,13,13]
fullemojiset = set(emoji[2] for emoji in emojilist)
COLUMNSETS = [parsefolder('e2svg'),fullemojiset,fullemojiset]

currentSubgroup = ''
currentgroup = ''
for group, subgroup, codepoint, shortname, version in emojilist:
    glyph = codepoint_to_html(codepoint)
    if group != currentgroup:
        print ('\n\n### '+group+'')
        currentgroup = group
    if subgroup != currentSubgroup:
        print ('\n#### '+subgroup+'\n')
        print('| name | EmojiTwo | Twemoji | OpenMoji |')
        print('|:-:|'+':-:|'*len(COLUMNSETS))
        currentSubgroup = subgroup
    linestring = f'| <small>{codepoint}</small><br>{shortname}<br>{glyph} | '
    for columnset in COLUMNSETS:
        if checkforcodepoint(columnset,codepoint):
            linestring += glyph
        linestring += ' | '
    print(linestring)
    #print(f'| {shortname} | {glyph} | {glyph} | {glyph} |')












#%%
#%%













# %% Build the markdown tables
# A useful link https://docs.python.org/3/howto/unicode.html
# There's gotta be a more intuitive way to convert from codepoint to character in pytho.
# I can't just add the '\U000...' to the start, because, well, reasons.
# So instead I'm converting the hex string to decimal and then using chr() to convert to character.

def codepoint_to_string(codepoint):
    hexcodes = codepoint.split()
    glyph = ''.join(chr(int(hexcode,16)) for hexcode in hexcodes)
    return glyph

def codepoint_to_html(codepoint):
    hexcodes = codepoint.split()
    html = ''.join("&#x"+hexcode+";" for hexcode in hexcodes)
    return html

# data for versions of columns
COLUMNVERSIONS = [13,14,14]

currentSubgroup = ''
currentgroup = ''
for group, subgroup, codepoint, shortname, version in emojilist:
    glyph = codepoint_to_html(codepoint)
    if group != currentgroup:
        print ('\n### '+group+'\n')
        currentgroup = group
    if subgroup != currentSubgroup:
        print ('\n#### '+subgroup+'\n')
        #print('| name | EmojiOne | Twemoji | OpenMoji |')
        print('| name | EmojiTwo | Twemoji | OpenMoji |')
        print('|:-:|'+':-:|'*len(COLUMNVERSIONS))
        currentSubgroup = subgroup
    linestring = f'| {shortname}<br>{glyph} | '
    for columnversion in COLUMNVERSIONS:
        if version <= columnversion:
            linestring += glyph
        linestring += ' | '
    print(linestring)
    #print(f'| {shortname} | {glyph} | {glyph} | {glyph} |')


#for codepoint, [group, shortname] in unicodeToInfo.items():
# %%

# %%
