<<<<<<< HEAD
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json


URL = 'https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", class_="sc-ertOQY cTYMbp")
restAPI = {}

def extractParamSection(section):
    isrequired = section.findnext(text="Required")
    section = {
        "name" : section.text,
        "required" : isrequired,
        "type" : section.findNext("p").text
    }
    return section

for div in results:
    ahref = div.find("a")
    title = ahref.text
    url = ahref['href']

    subpage = requests.get("https://developer.atlassian.com"+url)
    subsoup= BeautifulSoup(subpage.content, "html.parser")
    sections = subsoup.find_all("section", class_="sc-cyQzhP tIaJL")
    for section in sections:
        subtitle = section.find(
            "h3", class_="sc-izUgoq jrgPRL")
        route = section.find (
            "p", class_="sc-ibnDSj uiuRO"
        )
        params = {}

        for paramType in ["Path parameters", "Header parameters", "Query parameters", "Body parameters"]:
            subsection = section.find (
                text=paramType
            )
            try:
                paramNames = subsection.parent.findNext().find_all(
                    "strong")
                params[paramType] = list(
                    map(lambda param: {
                            "name" : (param.text),
                            "required" : param.find_next(text="Required"), 
                            "type" : param.findNext("p").text or ""}, 
                        paramNames))
            except: 
                False
        if "Query parameters" in params:
            queryParams = "&".join(list(map(lambda param: 
                "{}=".format(param['name']) + "${{param.{}}}".format(param['name']), params["Query parameters"]))).replace(" ","")
        else:
            url = route.text.split()[1]
            method = route.text.split()[0]

        name = subtitle.text.title().replace(" ","")
        name = ''.join([name[0].lower(), name[1:]])
        pprint(name)
        restAPI[name] = {
            "name" : name,
            "method" : method,
            "route" : url,
            "params" : params
        }

pprint(restAPI)

with open("API.json","w") as outfile:
    json.dump(restAPI,outfile)

=======
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import json


URL = 'https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("div", class_="sc-ertOQY cTYMbp")
restAPI = {}

for div in results:
    ahref = div.find("a")
    title = ahref.text
    url = ahref['href']

    subpage = requests.get("https://developer.atlassian.com"+url)
    subsoup= BeautifulSoup(subpage.content, "html.parser")
    sections = subsoup.find_all("section", class_="sc-cyQzhP tIaJL")
    for section in sections:

        subtitle = section.find(
            "h3", class_="sc-izUgoq jrgPRL")
        route = section.find (
            "p"
        )
        params = {}

        for paramType in ["Path parameters", "Header parameters", "Query parameters", "Body parameters"]:
            subsection = section.find (
                text=paramType
            )
            if subsection:
                params[paramType] = []
                subsection = subsection.parent
                while (subsection.next_sibling and subsection.next_sibling.find("strong")):
                    subsection = subsection.next_sibling
                    paramNames = subsection.find_all("strong")
                    params[paramType] += list(
                        map(lambda param: {
                            "name": (param.text),
                            "required": param.find_next(text="Required"),
                            "type": param.findNext("p").text or ""},
                            paramNames))
            
            
        if "Query parameters" in params:
            queryParams = "&".join(list(map(lambda param: 
                "{}=".format(param['name']) + "${{param.{}}}".format(param['name']), params["Query parameters"]))).replace(" ","")
        else:
            False
        url = route.text.split()[1]
        method = route.text.split()[0]
        name = subtitle.text.title().replace(" ","")
        name = ''.join([name[0].lower(), name[1:]])
        restAPI[name] = {
            "name" : name,
            "method" : method,
            "route" : url,
            "params" : params
        }


with open("API.json","w") as outfile:
    json.dump(restAPI,outfile)

>>>>>>> master
