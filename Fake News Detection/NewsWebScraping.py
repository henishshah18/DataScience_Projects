from selenium import webdriver
import json
import csv

csv_data = [] #contains full data to write to CSV
row_data = [] #contains [link, title, content] 1 row data
f = open('config.json',) 
data = json.load(f) 
driver_path = data["driver_path"]
search_key = data["search_key"]


def openLink():
    count = 1
    all_urls = []
    categories = []
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    api_url = "https://abcnews.go.com/meta/api/search?q="+search_key+"&limit=9000&sort=&type=Story&section=&totalrecords=true&offset=0"
    driver = webdriver.Chrome(executable_path = driver_path, options=options)
    driver.get(api_url)
        
    response = driver.find_element_by_tag_name('pre')
    data = json.loads(response.text)
        
    for items in data["item"]:
        if 'Text' in items["dcType"]:
            all_urls.append(items["link"])
        
    for url in all_urls:
        try:
            row_data = []
            print(url,count)
            split_url = url.split("//")[1].split("/")[0].split(".")
            split_cat = url.split("//")[1].split("/")[1]
            if(split_url[0]=='abcnews'):
                driver.get(url)
                title = driver.find_element_by_class_name("Article__Headline__Title").text
                content = driver.find_element_by_class_name("Article__Content").text
                row_data.append(url)
                row_data.append(title)
                row_data.append(content)
                row_data.append(split_cat)
                csv_data.append(row_data)
            count += 1
        except:
            continue

    all_urls = []
        
	
def writeToCSV(csv_data):
    fields = ['Link', 'Title', 'Content', 'Category']
    
    rows = csv_data
    
    # name of csv file  
    filename = "master_scrapped_data.csv"
    
    # writing to csv file
    with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  

        # writing the fields  
        csvwriter.writerow(fields)  

        # writing the data rows  
        csvwriter.writerows(rows)


openLink()
writeToCSV(csv_data)