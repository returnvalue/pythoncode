from lxml import etree


def main():
    postCount = 0
    entryCount = 0

    # build a doc structure using the ElementTree API
    doc = etree.parse('xmldata.xml').getroot()
    print(doc.tag)

    # Access the value of an attribute
    print(doc.attrib['title'])

    # Iterate over tags
    for elem in doc.findall('post'):
        print(elem.tag)

    # CountDecorator the number of posts
    postCount = len(doc.findall('post'))
    entryCount = len(doc.findall('.//entry'))

    print(f'There are {postCount} post elements')
    print(f'There are {entryCount} entry elements')

    # Create a new post
    newPost = etree.SubElement(doc, 'post')
    newPost.text = 'This is a new post'

    # CountDecorator the number of posts
    postCount = len(doc.findall('post'))
    entryCount = len(doc.findall('.//entry'))

    print(f'There are now {postCount} post elements')
    print(f'There are now {entryCount} entry elements')


if __name__ == '__main__':
    main()
# blogposts
# Blog Posts Collection
# post
# post
# There are 2 post elements
# There are 3 entry elements
# There are now 3 post elements
# There are now 3 entry elements