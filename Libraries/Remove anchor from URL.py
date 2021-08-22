# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
# remove_url_anchor('www.codewars.com#about')
# returns 'www.codewars.com'
# remove_url_anchor('www.codewars.com?page=1')
# returns 'www.codewars.com?page=1'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def remove_url_anchor(url):
    return url.split("#")[0]


remove_url_anchor("www.codewars.com#about")
remove_url_anchor("www.codewars.com/katas/?page=1#about")
remove_url_anchor("www.codewars.com/katas/")
