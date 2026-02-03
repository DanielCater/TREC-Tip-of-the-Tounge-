# Information Retrieval System

A modular, Python-based Information Retrieval (IR) system built on Pyserini, LuceneSearcher, and a custom snippet highlighter. It supports query decomposition, multi-field search, snippet generation, and an optional GUI built with PySimpleGUI.

## Features

- LuceneSearcher-based retrieval
- Query decomposition (entities, description, media type, time, etc.)
- Semantic-aware snippet highlighting
- Densest-window snippet selection
- GUI mode with real text highlighting
- Command-line mode for batch or TREC-style runs
- Configurable fields for search and highlighting

## Installation

Clone the repository:

    git clone https://github.com/yourusername/yourrepo.git
    cd yourrepo

Install dependencies:

    python packageInstaller.py

Make sure you have a Pyserini-compatible index:

    python -m pyserini.index.lucene \
      --collection JsonCollection \
      --input path/to/json \
      --index indexes/myindex \
      --generator DefaultLuceneDocumentGenerator \
      --threads 8

## Query Decomposition

Queries are decomposed into fields such as:

- description
- entities
- media_type
- time

Only semantic fields (e.g., description, entities) are used for snippet highlighting to avoid noise.

Example query JSON:

    {
      "description": ["reuben", "loses", "everything"],
      "entities": ["reuben"],
      "media_type": ["play"],
      "time": ["one", "day"]
    }

## Running a Search (CLI Mode)

Use the command-line interface to run a search:

    python main.py -cli

Arguments:

-cli        Launch command-line interface (Uses GUI by default)

## Snippet Highlighting

The system uses a densest-window highlighter:

- Finds all occurrences of semantic query terms
- Scores windows based on term density
- Selects the best passage
- Highlights terms using GUI-safe or Markdown-safe markup

Example output:

    DocID: 21771695 | Score: 0.0323
    Snippet: Reuben, who one day **loses** **everything** in the play...

## GUI Mode (PySimpleGUI)

Launch the GUI:

    python main.py

Features:

- Search bar
- Enter-to-search support
- Scrollable results
- Real text highlighting using embedded Tkinter Text widget
- Snippet viewer
- Optional full-document popup



## Project Structure

    project/
    ├── FormatCorpus               # Format Corpus code
    ├── Test Queries               # Test queries from TREC
    ├── Test Query Results         # Results from TREC
    ├── app.py                     # GUI for IR system
    ├── gpt.py                     # Wrapper for GPT AI 
    ├── main.py                    # Main operation to format corpus, index, and search
    ├── packageInstaller.py        # Installs packages needed
    ├── packagesUsed.txt           # List of packages for installer
    ├── pyseriniIndex.py           # Indexes corpus
    ├── queryDecomposerAI.py       # Decomposes query with LLM
    ├── queryDecomposerImproved.py # Decompose using SpaCy
    ├── search.py                  # AI search tool
    ├── searchAI.py                # search tool
    ├── test.py                    # Test TREC queries against results