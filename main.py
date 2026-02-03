import sys
from os import path

import app

# File: main.py
# Authors: Daniel Cater, Edin Quintana, Ryan Razzano, and Melvin Chino-Hernandez
# Version: 2/3/2026
# Description: This is the main program that integrates query decomposition and document indexing. It allows users to input queries,
# decomposes them into structured components using spaCy, and searches the indexed documents using Pyserini.

def main():

    # Install Packages
    from packageInstaller import installPackages
    installPackages()

    # Check for corpus split.
    if (not path.exists("./CORPUS")):
        from FormatCorpus.SplitCorpus import split
        split()

    # Check for corpus formatter converter
    if (not path.exists("./CORPUS_converted")):
        from FormatCorpus.corpusFormatConverter import convert
        convert()

    # install packages before importing pyserini
    from pyseriniIndex import index
    from searcher import search

    # Ensure the index is created
    index()

    # Search
    if(sys.argv.__len__() > 1 and sys.argv[1] == "-cli"):
        query = input("Search query: ").strip()
        while query != "":

            print()
            hits = search(query)
            for hit in hits.values():
                print(f"{hit['rank']} | {hit['title']} | Score: {hit['score']:.4f}\n{hit['snippet']}\n")
            query = input("Search query: ").strip()
    else:
        app.run()
main()