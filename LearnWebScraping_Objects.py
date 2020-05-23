from bs4 import BeautifulSoup

                                    #HTML Code - the html content that we are going to parse using Beautiful Soup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""

                                    #Creating a file called "index.html" and then, write the html content above to this file
with open('index.html', 'w') as f:
    f.write(html_doc)

                                    #Create a Beautiful Soup object based on the html_doc string variable that we defined above
                                    #This will allow us to parse the HTML content
soup = BeautifulSoup(html_doc, "lxml")

                                    #If you want to print out nicely formatted HTML
#print(soup.prettify())
#print(soup) #prints it out normally

#Tag:

                                    # Finds the FIRST occurrence of usage for a "b"
                                    # bold tag.
#print(soup.b) #this prints out <b>The Dormouse's story</b>

                                    # The "find" function also does the same, where it
                                    # only finds the FIRST occurrence in the HTML doc
                                    # of a tag with "b"
#print(soup.find('b')) #this also prints out <b>The Dormouse's story</b>

                                    # If we want to find ALL of the elements on the page
                                    # with the "b" tag, we can use the "find_all" function.
#print(soup.find_all('b'))

# Name:

                                    # This gives the name of the tag. In this case, the
                                    # tag name is "b".
#print(soup.b.name)

                                    # We can alter the name and have that reflected in the
                                    # source. For instance:
#tag = soup.b #this is currently <b>The Dormouse's story</b>
#tag.name = "blockquote" #now tag printed is <blockquote>The Dormouse's story</blockquote>

# Attributes:

                                    #Finds all instances of bold tags, and then returns the THIRD occurence of the bold tags (index 2)
#tag = soup.find_all('b')[2]


                                    # This specific tag has the attribute "id", which
                                    # can be accessed like so:
#print(tag['id'])       #prints 1 since ID is 1 in <b id="1">Test 1</b>

                                    #tags can have multiple attributes assigned to it
                                    #For example:
#tag = soup.find_all('b')[3]     #here tag is <b another-attribute="1" id="verybold">Test 2</b>

                                    # We can then access multiple attributes that are
                                    # non-standard HTML attributes:
#print(tag['id'])
#print(tag['another-attribute'])

                                    # If we want to see ALL attributes, we can access them
                                    # as a dictionary object:
#tag = soup.find_all('b')[3]
#print(tag.attrs)           #prints a dictionary where the key is the name of the attribute and the value is the value of the attribute

                                    # These properties are mutable, and we can alter them
                                    # in the following manner.
#tag = soup.find_all('b')[3]
#tag['another-attribute'] = 2      #now the value for this attribute is 2 and not 1

                                    # We can also use Python's del command for lists to
                                    # REMOVE attributes:
#tag = soup.find_all('b')[3]
#del tag['id']
#del tag['another-attribute']

                                    #Navigable String
                                    #returns the string content between the tags
#tag = soup.find_all('b')[3]
#print(tag.string)


                                    # We can use the "replace_with" function to replace
                                    # the content of the string with something different:
#tag = soup.find_all('b')[3]
#tag.string.replace_with("This is another string")


