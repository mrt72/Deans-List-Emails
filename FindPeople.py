from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException as nSE
import csv

driver = webdriver.Firefox()
driver.get("https://find.pitt.edu")

f = open("deans_list_fall_2019.csv")
reader = csv.reader(f)
names = []
for row in reader:
    names.append(row)

# f2 = open("test.csv")
# reader = csv.reader(f2)
# names = []
# for row in reader:
# names.append(row)


for i in names:
    f1 = open("emails.txt", "a")  # opens emails.txt to append information
    search = driver.find_element_by_id("txtSearch")  # Accesses the search bar
    search.clear()  # Clears existing text in the search bar
    search.send_keys(i)  # Types what you want to search
    search.send_keys(Keys.RETURN)  # Return key in order to search
    driver.implicitly_wait(10)  # Waits 4 seconds for results
    try:
        email = driver.find_element_by_partial_link_text('@').text  # Finds location of Pitt email address in <a> tag
        results = driver.find_element_by_id("resultsInfo").text
        results = results[0]
        if int(results) == 1:
            f1.write("Name: " + str(i) + "    Email: " + email + "\n")  # gets the plaintext of email, writes to emails.txt
            # email = "Find Manually"
        elif int(results) > 1:
            f1.write("Name: " + str(i) + "    Email: " + email + " (Verify, Duplicate Names)\n")
        elif int(results) == 0:
            f1.write("Name: " + str(i) + "    Email: Not found!" + "\n")
        assert "0 results found" not in driver.page_source
        # dl_email = email.get_attribute('href') (Not needed, can just use .text at end of email find_element)
        # dl_email = dl_email.replace("mailto:", "")
        f1.close()  # Closes emails.txt
        driver.refresh()
    except nSE:  # exception to catch
        f1.write("Name: " + str(i) + "     Email: person not found \n")
