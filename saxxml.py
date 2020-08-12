import xml.sax

# SAX XML Example
# define a Custom ContentHandler class that extends ContenHandler
class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.postCount = 0
        self.entryCount = 0
        self.isInTitle = False

    # Handle startElement
    def startElement(self, tagName, attrs):
        if tagName == 'blogposts':
            print('Blogposts title: ' + attrs['title'])
        elif tagName == 'post':
            self.postCount += 1
        elif tagName == 'entry':
            self.entryCount += 1
        elif tagName == 'title':
            self.isInTitle = True

    # Handle endElement
    def endElement(self, tagName):
        if tagName == 'title':
            self.isInTitle = False

    # Handle text data
    def characters(self, chars):
        if self.isInTitle:
            print('Title: ' + chars)

    # Handle startDocument
    def startDocument(self):
        print('About to start!')

    # Handle endDocument
    def endDocument(self):
        print('Finishing up!')


def main():
    # create a new content handler for the SAX parser
    handler = CustomContentHandler()

    # call the parse method on an XML file
    xml.sax.parse('xmldata.xml', handler)

    # when we're done, print out some interesting results
    print(f'There were {handler.postCount} post elements')
    print(f'There were {handler.entryCount} entry elements')


if __name__ == '__main__':
    main()
# About to start!
# Blogposts title: Blog Posts Collection
# Title: Parse XML With SAX
# Title: Overview
# Finishing up!
# There were 2 post elements
# There were 3 entry elements

# XML DOM API
