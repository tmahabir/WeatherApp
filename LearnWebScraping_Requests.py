import requests
from bs4 import BeautifulSoup

                    #this is an example on the White House website where we will try to extract all of the links on the page that point to the
                    #briefings and statements.

                    #"get" function is used to access the wanted webpage
result = requests.get("https://www.whitehouse.gov/briefings-statements/")

                    # result.status_code ensures the website is accessible, (200 means ok, 404 means bad)
                    #print(result.status_code)

                    #result.headers allows you to verify that you have accessed the correct page
                    #print(result.headers)

                    #result.content stores the page content
src = result.content

                    #Now that we have the page source stored, we will use the BS module to parse and process the source
                    #To do so, create a BS object based on the source variable we created above (src)
                                    #soup = BeautifulSoup(src, 'html.parser')
soup = BeautifulSoup(src, 'lxml')

                        #If we want to see a list of all of the links on the page:
links= soup.find_all("a")
                        #a_tag defines a hyperlink, which is used to link from page to another
#print(links)
#print("\n")

                        # If we just want to extract the link that contains the text "About"
                        # on the page instead of every link. We can use the built-in
                        # "text" function to access the text content between the <a> </a> tags.
for link in links:
   if "About" in link.text:
       print(link)
       print(link.attrs['href']) #only prints out the href part of the a_tag, href indicates the link's destination

urls = []
                        #if we want to find all the things with the h2_tag and then inside of that h2_tag, extract the a_tag
for h2_tag in soup.find_all("h2"):             #find_all returns a list
    a_tag = h2_tag.find('a')                   #find finds a single element
    urls.append(a_tag.attrs['href'])              #add the href part of each a_tag to the urls list (Reminder: href indicates the link's destination)
print(urls)