from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Firefox()
driver.get("https://find.pitt.edu")

# f = open("deans_list_fall_2019.csv")
# reader = csv.reader(f)
# names = []
# for row in reader:
#   names.append(row)


f2 = open("test.csv")
reader = csv.reader(f2)
names = []
for row in reader:
    names.append(row)


for i in names:
    f1 = open("emails.txt", "a")  # opens emails.txt to append information
    search = driver.find_element_by_id("txtSearch")  # Accesses the search bar
    search.clear()  # Clears existing text in the search bar
    search.send_keys(i)  # Types what you want to search
    search.send_keys(Keys.RETURN)  # Return key in order to search
    driver.implicitly_wait(3)  # Waits 4 seconds for results
    email = driver.find_element_by_partial_link_text('pitt')  # Finds location of Pitt email address in <a> tag
    dl_email = email.get_attribute('href')
    dl_email = dl_email.replace("mailto:", "")
    f1.write("Name: " + str(i) + "    Email: " + dl_email + "\n")  # gets the plaintext of email, writes to emails.txt
    f1.close()  # Closes emails.txt
    assert "No results found" not in driver.page_source
    driver.refresh()
