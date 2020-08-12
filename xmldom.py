import xml.dom.minidom


def main():
    domtree = xml.dom.minidom.parse('xmldata.xml')
    rootnode = domtree.documentElement

    # display some information about the content
    print(f'The root element is {rootnode.nodeName}')
    print(f'The Title is: {rootnode.getAttribute("title")}')
    entries = domtree.getElementsByTagName('entry')
    print(f'There are {entries.length} entry tags')

    # create a new entry tag in memory
    newItem = domtree.createElement('entry')

    # add some text to the entry
    newItem.appendChild(domtree.createTextNode('Magic Entry!'))

    # now add the entry to the first post
    firstPost = domtree.getElementsByTagName('post')[0]
    firstPost.appendChild(newItem)

    # Now count the entry tags again
    entries = domtree.getElementsByTagName('entry')
    print('Now there are {0} entry tags'.format(entries.length))

    # Print out the domtree as xml
    print(domtree.toxml())


if __name__ == '__main__':
    main()
# The root element is blogposts
# The Title is: Blog Posts Collection
# There are 3 entry tags
# Now there are 4 entry tags
# <?xml version="1.0" ?><blogposts title="Blog Posts Collection" date="A date" author="Some dude">
#
#    <post type="summary">
#       <title>Parse XML With SAX</title>
#    <entry>Magic Entry!</entry></post>
#
#    <post type="detail">
#       <title>Overview</title>
#       <entry>
#          Parsing XML is great
#       </entry>
#       <entry/>
#       <entry>
#          Have fun with XML parsing
#       </entry>
#    </post>
# </blogposts>