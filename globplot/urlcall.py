import urllib2, urllib, re, urlparse
from pprint import pprint
from BeautifulSoup import BeautifulSoup as bs

#Root of website
url_root = 'http://globplot.embl.de'

def call_and_dl(prot_name, prot_sequence, url_root):
    #values
    values = {'do_invert':	'true',
    'do_smart':	'true',
    'join_frame_dis':	'4',
    'join_frame_dom':	'15',
    'key':	'process',
    'params':	'RL',
    'peak_frame_dis':	'5',
    'peak_frame_dom':  '74',
    'plot_title': prot_name,
    'sequence_string': prot_sequence}

    #Encode data and read the webpage
    data = urllib.urlencode(values)
    req = urllib2.Request(url_root+'/cgiDict.py', data)
    response = urllib2.urlopen(req)
    html = response.read()

    #Parse it
    soup = bs(html)

    #Find the image
    for image in soup.findAll("img"):
        im_filename = prot_name+'.jpg'
        urllib.urlretrieve(url_root+image["src"], im_filename)


    #Get the raw data
    def get_data(ltype, llink):
        if ltype in llink['href']: 
            urllib.urlretrieve(url_root+llink['href'], prot_name+ltype)
    get_data.prot_name = prot_name
    get_data.url_root = url_root

    for link in soup.findAll("a"):
        get_data('.smooth', link)
        get_data('.raw', link)


    #Find disorder ranges
    disorder_sections = []
    dis_range = re.compile(r'(\d+)[\s\-]+(\d+),?')
    for data in soup.find("p", "monospaced"):
        for line in data:
            if 'Disorder' in line:
                res = dis_range.findall(line)
                for seg in res:
                    disorder_sections.append([int(seg[0]), int(seg[1])])

sequences = open('../swq.csv').readlines()
for sequence in sequences:
    [name, sequence] = sequence.split('| ')
    call_and_dl(name, sequence, url_root)