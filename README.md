# AcronymCreator

A program that reads the text from file and creates acronyms for each line
--------------------------------------------------------------------------------------------------------------------------------------

Rules for creating the acronym are :

• Acronym is formed by taking first letter of each word in a line of text.
• If the acronym is used for a previous line, then recreate the acronym by adding the
second letter of the first word to the acronym.
• If the recreated acronym is already used for a previous line, this should be flagged
as a duplicate acronym.
• The acronym should be in upper case letters.
• The acronym creation should be case insensitive, that is it should be independent of
the case of the letters in the expanded form.
• Blank lines and other white spaces are to be ignored
--------------------------------------------------------------------------------------------------------------------------------------
Input:-

One Two
Three Four
Five Six

Output:-

OT->One Two
TF->Three Four
FS->Five Six

Input:-

Any Time Machine
Any Time Money

apple Talk magic

Output:-

ATM->Any Time Machine
ANTM->Any Time Money
APTM->apple Talk magic
