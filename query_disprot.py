from BeautifulSoup import BeautifulStoneSoup
import pprint, pickle, sys

from protein import Protein, Region, Database

re_parse = 1

if re_parse:
    #Generic Beautiful Soup Stuff
    database_file = "disprot_v4.9.xml"
    database = open(database_file, 'r').read()
    soup = BeautifulStoneSoup(database)

    proteins = []

    #Pickle Out
    # pickle_file = open('db.py', 'w+')
    # sys.setrecursionlimit(10000)
    db = Database(soup)
    # pickle.dump(db, pickle_file)
else:
    #Pickle In
    pickle_file = open('db.py')
    pickle.load(pickle_file)

outfile = open('db.csv', 'w+')
outfile_seq = open('swq.csv', 'w+')

#seq_to_output = ["DP00002", "DP00042","DP00288","DP00510","DP00039","DP00195","DP00465","DP00532","DP00164","DP00531","DP00205","DP00219","DP00174","DP00016","DP00047","DP00564","DP00041","DP00563","DP00232","DP00068","DP00367","DP00198","DP00214","DP00332","DP00584"]
seq_to_output = ["DP00112", "DP00148", "DP00347", "DP00281", "DP00185", "DP00544", "DP00186", "DP00546", "DP00542", "DP00287", "DP00170", "DP00199", "DP00188", "DP00540", "DP00535"]


for protein in db.proteins:
    if protein.id in seq_to_output:
        outfile_seq.write(protein.id+'| '+protein.sequence+'\n')
    for region in protein.regions:
        outfile.write(protein.id+'| '+protein.name+'| '+region.type+'| '+region.struct_fun_type()+'| '+str(region.length())+'| '+str(protein.percentage_disordered())+'\n')
