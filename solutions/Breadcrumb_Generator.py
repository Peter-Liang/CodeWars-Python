"""
4 kyu: Breadcrumb Generator
http://www.codewars.com/kata/breadcrumb-generator/train/python


As breadcrumb menùs are quite popular today, I won't digress much on explaining them, leaving the wiki link to do all the dirty work in my place.

What might not be so trivial is instead to get a decent breadcrumb from your current url. For this kata, your purpose is to create a function that takes a url, strips the first part (labelling it always HOME) and then builds it making each element but the last a <a> element linking to the relevant path; last has to be a <span> element getting the active class.

All elements need to be turned to uppercase and separated by a separator, given as the second parameter of the function; the last element can terminate in some common extension like .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there, sending users automatically to the upper level folder.

A few examples can be more helpful than thousands of words of explanation, so here you have them:

generate_bc("mysite.com/pictures/holidays.html", " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
generate_bc("www.codewars.com/users/GiacomoSorbi", " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
generate_bc("www.microsoft.com/docs/index.htm", " * ") == '<a href="/">HOME</a> * <span class="active">DOCS</span>'
Seems easy enough?

Well, probably not so much, but we have one last extra rule: if one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it (i.e.: taking just the initials of every word); url will be always given in the format this-is-an-element-of-the-url and you should ignore words in this array while acronymizing: ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]; a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased with hyphens replaced by spaces.

Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.

Examples:

generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.htm", " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
You will always be provided valid url to webpages in common formats, so you probably shouldn't bother validating them.

If you like to test yourself with actual work/interview related kata, please also consider this one about building a string filter for Angular.js.

Special thanks to the colleague that, seeing my code and commenting that I worked on that as if it was I was on CodeWars, made me realize that it could be indeed a good idea for a kata :)
"""


def generate_bc(url, separator):
    if '//' in url:
        url = url[url.index('//') + 2:]

    url = url.rstrip('/')

    try:
        for i, c in enumerate(url):
            if c in ['?', '#']:
                url = url[0:i]
                break

        menus = url.split('/')[1:]
        if menus and 'index.' == menus[-1][0:6]:
            menus = menus[:-1]
        if not menus:
            return '<span class="active">HOME</span>'

        breadcrumb = '<a href="/">HOME</a>'

        for i, e in enumerate(menus[:-1]):
            breadcrumb += separator + '<a href="/{}/">{}</a>'.format('/'.join(menus[:i + 1]), get_element_name(e))

        breadcrumb += separator + '<span class="active">{}</span>'.format(get_element_name(menus[-1]))
        return breadcrumb
    except:
        return url


ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]


def get_element_name(element):
    acronyms = element.split('-')
    for i, c in enumerate(acronyms[-1]):
        if c == '.':
            acronyms[-1] = acronyms[-1][:i]
            break

    if len(element) > 30:
        for i, c in reversed(list(enumerate(acronyms))):
            if c in ignore_words:
                acronyms.pop(i)
        return ''.join([s[0].upper() for s in acronyms])

    return ' '.join([s.upper() for s in acronyms])



assert generate_bc("mysite.com/pictures/holidays.html",
                   " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
assert generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars",
                   " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
assert generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top",
                   " * ") == '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
assert generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
                   " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
assert generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
                   " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

# print("https://www.linkedin.com/in/giacomosorbi".index('//'))
# print(generate_bc("https://www.linkedin.com/in/giacomosorbi", " * "))
assert generate_bc("https://www.linkedin.com/in/giacomosorbi",
                   " * ") == '<a href="/">HOME</a> * <a href="/in/">IN</a> * <span class="active">GIACOMOSORBI</span>'
print(generate_bc("www.agcpartners.co.uk", " * "))
assert generate_bc("www.agcpartners.co.uk", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.agcpartners.co.uk/", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.agcpartners.co.uk/index.html", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.google.ca/index.php", " * ") == '<span class="active">HOME</span>'
