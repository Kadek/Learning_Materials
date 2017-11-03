import requests
from lxml import etree
from io import StringIO

import os, re

import pdf2txt
import pdfminer

# FIND COUNTRY LINKS - START ----------------------------------
def get_country_links(main_webpage_link):

	tree = get_webpage(main_webpage_link)
	return get_country_links_container(tree)

def get_webpage(link):

	r = requests.get(link)
	parser = etree.HTMLParser()
	tree = etree.parse(StringIO(r.text), parser)

	return tree	


def get_country_links_container(tree):
	paths = [
		"//td[@class='ms-rteTableOddCol-default']//*[strong]",
		"//td[@class='ms-rteTableFooterOddCol-default']//*[strong]"
	]

	return get_specific_links(tree, paths)

def get_specific_links(tree, paths):

	container = []

	for path in paths:
		download_links(tree, path, container)

	return container

def download_links(tree, path, container):

	els = tree.findall(path)

	for el in els:
		if(el.attrib.get("href") is not None):
			container.append(el.attrib.get("href"))

	return container

# FIND COUNTRY LINKS - END ----------------------------------

# FIND UNIS LINKS - START ----------------------------------
def get_main_webpage():

	return "http://administracja.sgh.waw.pl"

def get_unis_list(country_link):

	tree = get_webpage(get_main_webpage() + country_link)
	return get_unis_links_container(tree)

def get_unis_links_container(tree):

	paths = [
		"//div[@class='ms-WPBody ms-wpContentDivSpace']/ul/li//a",
	]

	return get_specific_links(tree, paths)

# FIND UNIS LINKS - END ----------------------------------

def get_links_file():
	links = get_country_links("http://administracja.sgh.waw.pl/pl/cpm/wymiana_miedzynarodowa/wyjezdzajacy/raporty/Strony/default.aspx")

	container = {}
	for link in links:
		container[link] = get_unis_list(link)

	with open("links.txt", "w") as f:
		for main_link in container:
			f.write(main_link + "\n")
			f.write("-----------------------------------" + "\n")
			for link in container[main_link]:
				f.write(link  + "\n")
			f.write("-----------------------------------"  + "\n")


# DOWNLOAD PDFS - BEGIN ----------------------------------

def get_pdfs(file_name, dir_name):

	#os.makedirs(dir_name)
	links = read_links_from_file(file_name)
	curr_country = ""
	i = -1

	while (i < len(links) - 1):
		i = i + 1
		if(len(curr_country) == 0):
			curr_country = read_curr_country(links[i])
			os.makedirs(dir_name + "/" + curr_country)

			# skips the break line
			i = i + 1
			continue
	
		if(re.search('[a-zA-Z]', links[i])):
			pdf = download_pdf(links[i])
			save_pdf(links[i], pdf, curr_country)
		else:
			print("Downloaded: " + curr_country) 
			curr_country = ""

def read_curr_country(link):
	p = re.compile("([^/]+)\.aspx")
	m = p.search(link)
	return m.group(1)

def read_links_from_file(file_name):

	with open(file_name) as f:
		links_list = f.readlines()

	return [x.strip() for x in links_list]	

def download_pdf(link):
	return requests.get(get_main_webpage() + link)

def save_pdf(link, pdf, curr_country):

	file_name = extract_file_name(link)
	if(file_name is None):
		return

	# get city name and create folder if not present
	curr_city = get_curr_city(curr_country, file_name)
	if(not os.path.isdir("./pdfs/"+curr_country+"/"+curr_city)):
		os.makedirs("./pdfs/"+curr_country+"/"+curr_city)

	file_path = "pdfs/" + curr_country + "/" + curr_city + "/" + file_name
	with open(file_path, "wb") as f:
		f.write(pdf.content)

def extract_file_name(link):
	file_formats = ["pdf", "doc", "odt"]

	for file_format in file_formats:
		p = re.compile("([^/]+\."+file_format+")")
		m = p.search(link)

		if(m is not None):
			file_name = m.group(1)
			break

	if(m is None):
		print("Unknown file format")
		file_name = None	

	return file_name

def get_curr_city(curr_country, link):
	cat_1 = ["singapur", 'azerbejdzan-raporty', 'indie', 'usa', 'tajwan', 
			 'rpa-raporty', 'nowa_zelandia', 'irlandia', 'chile', 'tajlandia', 
			 'rosja', 'liban', 'peru', 'brazylia', 'chiny', 'japonia', 'gruzja', 
			 'kanada', 'meksyk', 'hong-kong', 'australia', 'argentyna', 'korea_poludniowa', 'izrael']

	p = re.compile("([^_]+)_")
	m = p.findall(link)

	print(link)
	print(m)
	if(curr_country.lower() in cat_1):
		if(len(m) < 1):
			return ""
		return m[0]
	else:
		if(len(m) < 2):
			return ""
		return m[1]

# DOWNLOAD PDFS - END----------------------------------

# COMPUTE GRADES - BEGIN----------------------------------
def get_grades(pdfs_dir_name, grades_file_name):

	grades = compute_grades(pdfs_dir_name)
	save_grades(grades, grades_file_name)

def compute_grades(pdfs_dir_name):

	grades = get_names(pdfs_dir_name)

	for country in grades:
		print("Computing grades for country: {}".format(country))
		grades[country] = compute_country_grades(pdfs_dir_name, country)
		print("Finished computing grades for country: {}".format(country))

	return grades


def compute_country_grades(pdfs_dir_name, country):

	country_grades = get_names(pdfs_dir_name +"/"+ country)

	for uni in country_grades:
		print("****** Computing grades for Uni: {}".format(uni))
		country_grades[uni] = compute_uni_grades(pdfs_dir_name, country, uni)

	return country_grades


def compute_uni_grades(pdfs_dir_name, country, uni):

	documents = get_files_names(pdfs_dir_name +"/"+ country +"/"+ uni)

	sum_knowledge = 0
	sum_general = 0
	n = len(documents)
	for document in documents:
		(knowledge, general) = compute_document_grades(pdfs_dir_name, country, uni, document)
		if(knowledge == 0 or general == 0):
			n = n -1
			continue

		sum_knowledge += knowledge
		sum_general += general

	if(n == 0):
		return (0,0)
	return (sum_knowledge/n, sum_general/n)

def compute_document_grades(pdfs_dir_name, country, uni, document):

	try:
		document_text = pdf2txt.convert_pdf_to_txt(pdfs_dir_name + "/" + country + "/" + uni + "/" + document)
	except (pdfminer.pdfparser.PDFSyntaxError, pdfminer.pdfdocument.PDFTextExtractionNotAllowed, TypeError):
		return (0,0)

	p = re.compile("([1-5]) *[:-]")
	document_text = document_text[::-1]

	grades = [m.group(1) for m, _ in zip(p.finditer(document_text), range(2))]
	if(len(grades) < 2):
		return (0,0)

	return (int(grades[1]), int(grades[0]))

def get_names(path):

	names = {}

	for name in os.listdir("./"+path+"/"):
		if os.path.isdir("./"+path+"/"+name):
			names[name] = {}
	return names

def get_files_names(path):

	return [name for name in os.listdir("./"+path+"/")]

def save_grades(grades, grades_file_name):

	with open(grades_file_name+".txt", "w") as f:

		for country_name in grades:
			f.write("Country: {}\n".format(country_name))
			for uni_name in grades[country_name]:
				uni = grades[country_name][uni_name]
				f.write("Uni: {:15} knowledge:  {:6} , general {}\n".format(uni_name, uni[0], uni[1]))
			f.write("-----------------------------------------------------------------------------\n")

# COMPUTE GRADES - END----------------------------------

if __name__ == '__main__':
	links_file_name = "links.txt"
	pdfs_dir_name = "pdfs"
	grades_file_name = "grades"

	if(not os.path.isfile("./" + links_file_name)):
		print("Links file missing. Downloading")
		get_links_file()
		print("Download successful")
	else:
		print("Links file loaded.")

	if(not os.path.isdir("./"+pdfs_dir_name+"/")):
		print("Pdfs missing. Downloading")
		get_pdfs(links_file_name, pdfs_dir_name)
		print("Download successful")
	else:
		print("Pdfs loaded.")

	if(not os.path.isdir("./"+grades_file_name)):
		print("Gradess missing. Computing")
		get_grades(pdfs_dir_name, grades_file_name)
		print("Computation successful")
	else:
		print("Grades already present.")