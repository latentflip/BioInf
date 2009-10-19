import re, pprint

infilename = raw_input('Pondr Input filename: ')
outfilename = raw_input('Pondr Output filename: ')


infile = open(infilename, 'r')
outfile = open(outfilename, 'w+')

lines = infile.readlines()

region_s = r'^Predicted disorder segment \[(\d+)\]-\[(\d+)\]'
region = re.compile(region_s)

size_s = r'Predicted residues: (\d+)'
size = re.compile(size_s)

vals_s = r'(\d+)\s+(\w+)\s+(\d+\.{1}\d+)'
vals = re.compile(vals_s)

ord_dis_arr = []
num_arr = []
res_arr = []
vlxt_arr = []

found_size = False
found_vals = False

for line in lines:
  if not found_size:
    size_res = size.match(line)    
    if size_res is not None:
      length = int(size_res.groups()[0])
      ord_dis_arr = [0]*length
      found_size = True
  else:
    if not found_vals:
      region_res = region.match(line)
      if region_res is not None:
          start = int(region_res.groups()[0])-1
          end = int(region_res.groups()[1])+1-1
          ord_dis_arr[start:end] = [1]*(end-start)
      if 'PREDICTOR VALUES' in line:
        found_vals = True
    else:
      vals_res = vals.search(line)
      if vals_res is not None:
        num_arr.append(vals_res.groups()[0])
        res_arr.append(vals_res.groups()[1])
        vlxt_arr.append(vals_res.groups()[2])

print len(ord_dis_arr),len(num_arr), len(res_arr), len(vlxt_arr)


if len(ord_dis_arr)==len(num_arr)==len(res_arr)==len(vlxt_arr):
  for i in range(0, len(ord_dis_arr)):
    outfile.write(num_arr[i]+', '+res_arr[i]+', '+vlxt_arr[i]+', '+str(ord_dis_arr[i])+'\n')
else:
  print 'Something is wrong as the lengths of the results are different'






