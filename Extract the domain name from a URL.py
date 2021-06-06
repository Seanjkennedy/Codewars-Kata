#Extract the domain name from a URL

"""Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
 For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == 'cnet'"""

def domain_name(url):
    prefix = ['https://', 'http://', 'www.']
    domain = url

    for i in prefix:
        if i in url:
            domain = domain.replace(i, "")

    end_of_domain = domain.index(".")
    return domain[:end_of_domain]
