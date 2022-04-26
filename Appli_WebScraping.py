import requests
import lxml.html as lh
import pandas as pd
import csv
import re

REMPLACE_SANS_ESPACE = re.compile("[;:!\'?,\"()\[\]]")
#REMPLACE_AVEC_ESPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|[.]")
REMPLACE_AVEC_ESPACE = re.compile("(<br\s/><br\s/>)|(-)|(/)|[.’']")
PUR_NOMBRE = re.compile("[0-9]")

# XPath content to collect
tags = ['//span[@class="stareval-note"]', \
        '//div[@class="content-txt review-card-content"]' ]
cols = ['Note', \
        'Description' ]


def getPage(url):
    page = requests.get(url)
    doc = lh.fromstring(page.content)

    # Get the Web data via XPath
    content = []
    for i in range(len(tags)):
        content.append(doc.xpath(tags[i]))

    # Gather the data into a Pandas DataFrame array
    df_liste = []
    for j in range(len(tags)):
        tmp = pd.DataFrame([content[j][i].text_content().strip() for i in range(len(content[i]))], columns=[cols[j]])
        tmp['key'] = tmp.index
        df_liste.append(tmp)

    # Build the unique Dataframe with one tag (xpath) content per column
    liste = df_liste[0]
    for j in range(len(tags)-1):
        liste = liste.join(df_liste[j+1], on='key', how='left', lsuffix='_l', rsuffix='_r')
        liste['key'] = liste.index
        del liste['key_l']
        del liste['key_r']
    
    return liste

def getPages(_nbPages, _url, uri_pages):
    liste_finale = pd.DataFrame()
    for i in range (_nbPages):
        liste = getPage(_url + uri_pages + str(i+1))
        liste_finale = pd.concat([liste_finale, liste], ignore_index=True)
    return liste_finale


def preprocess(txt):
    txt = [PUR_NOMBRE.sub("", line.lower()) for line in txt] # retire les nomre (comme les années)
    txt = [line.replace('\n', ' ')  for line in txt] # Retire les \n (retours chariots)
    txt = [REMPLACE_SANS_ESPACE.sub("", line.lower()) for line in txt]
    txt = [REMPLACE_AVEC_ESPACE.sub(" ", line) for line in txt]
    return txt

def get_webscrapping_avis(url, uri_pages, nbPages, chemin):
    df = getPages(nbPages, url, uri_pages)
    # df['Description'] = pd.DataFrame(preprocess(df['Description']))
    df = df.drop(["key"], axis = 1)
    df.to_csv(chemin, index=False, quoting=csv.QUOTE_NONNUMERIC)
    return chemin
