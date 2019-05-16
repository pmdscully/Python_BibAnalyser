import bibtexparser 
import sys, numpy as np
from config import App

appConfig = App() 

def load_bib_as_bibdb( f ):
    with open(f) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database

def get_property(db, c):
  l = []
  for x in db.entries_dict.keys():
   try:
    l.append( db.entries_dict[x][c] )
   except:
    pass # ignore entries with the specified field missing
  return l

def count_unique( l ):
    d = {}
    for i in l:
        if i in d:
            # already in, + 1
            d[i] += 1
        else:
            # missing , set as 1.
            d[i] = 1
    return d

def show_journals_by_desc( bibdb ):
    l = get_property(bibdb, "journal")
    l += get_property(bibdb, "journaltitle")
    d = count_unique( l )
    sorted_x = sorted(d.items(), reverse=True, key=lambda kv: kv[1])
    print("------------------------------------")
    print("----- Ordered Journal Titles: ------")
    print("------------------------------------")
    for x in sorted_x:
        print(x)

def main():
    filepath = appConfig.config("bibtex_filepath")
    bibdb = load_bib_as_bibdb( filepath )
    show_journals_by_desc( bibdb )


if __name__ == "__main__":
    main()