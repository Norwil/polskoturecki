from bs4 import BeautifulSoup

def process_soup():
	infile = open("ann_words2.xml","r", encoding='utf-8')
	contents = infile.read()
	soup = BeautifulSoup(contents,'xml')

	#

	for item in set(soup.findAll('string')[1:]):

		
	    print(item.text)

##content = soup.findAll(attrs={"name" : "orth"})
##print(list(content)[0])

process_soup()
