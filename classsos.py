##from bs4 import BeautifulSoup
import csv
import sqlite3 

class Polsko(object):

    def __init__(self):
        self.process_soup()
	self.create_connection()
	self.create_table()
	self.csv_reader()

    def create_connection(self):
	self.conn = sqlite3.connect("kelimeler.db")
	self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS kelimeler_tb""")
        self.curr.execute("""create table kelimeler_tb(
                                        ad text,
                                        sıfat text, 
                                        eylem text
                                        )""")
##    def process_soup(self):
##
##        infile = open("ann_words2.xml","r", encoding='utf-8')
##        contents = infile.read()
##        soup = BeautifulSoup(contents,'xml')
##          
##        for item in set(soup.findAll('string')[1:]):			
##            print(item.text)
##            item_data = item.text.split() # or whatever you need to do to turn item.text in to a list with 3 entries
##            data.append(item_data)
##        return data
##
    def csv_reader(self):
        with open('subtlex-pl.csv', encoding='utf-8') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
		print(row[0])

##    def csv_reader(self):
##		
##        with open('subtlex-pl.csv', encoding='utf-8') as csvfile:
##            readCSV = csv.reader(csvfile, delimiter=',')
##
##            words = []
##            
##            for row in readCSV:
##                word = row[1]
##
##                words.append(word)
##
##            print(words)

           

    def store_db(self, data):
        for item in data:
        
            self.curr.execute("""INSERT INTO kelimeler_tb VALUES (?)"""(
                    item.text['ad'][0]
                    ))
            self.conn.commit()
            self.conn.close()


Polsko()
