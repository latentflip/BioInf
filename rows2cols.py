infilename = raw_input('Filename of input data: ')
outfilename = raw_input('Filename to save to: ')

infile = open(infilename, 'r')
outfile = open(outfilename, 'w+')
data = infile.read()

for letter in data:
  if letter.isalpha():
    outfile.write(letter+'\n')
  