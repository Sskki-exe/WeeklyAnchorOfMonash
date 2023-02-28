from selenium import webdriver

######## TO DO ########
# For each page:
#     For each card on page:
#         Check for dates on the post ("information session: 24th February")
#         If date is in the past, stop
#         Else, add post to list
#

driver = webdriver.Firefox()
driver.get("https://www.facebook.com/MSA.Freebies/")