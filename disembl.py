import re, pprint

outfilename = raw_input('Disembl Output filename: ')

outfile = open(outfilename, 'w+')
while True:
  try:
    seq_length = int(raw_input("How long is the sequence?: "))
    break
  except ValueError:
    print "Oops!  That was not a valid number.  Try again..."

the_string = raw_input('Copy and paste list of numbers: ')




ord_dis_arr = [0]*seq_length

rnge_s = r'(\d+)[\s\-]+(\d+),?'
rnge = re.compile(rnge_s)

res = rnge.findall(the_string)
for dis in res:
  start = int(dis[0])-1
  end = int(dis[1])
  ord_dis_arr[start:end] = [1]*(end-start)
  
for i in ord_dis_arr:
  outfile.write(str(i)+'\n')

