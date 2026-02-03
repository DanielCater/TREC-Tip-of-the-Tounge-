import json
import tkinter as tk

import PySimpleGUI as sg

import searcher as searcher
import searcherAI as searcherAI

# File: app.py
# Author: Daniel Cater
# Version: 2/3/2026
# Description: This file implements a simple GUI using PySimpleGUI to allow users to input queries

def run():

    # Define the GUI layout
    layout = [
        [sg.Text("Enter query"), sg.Input(key="query")],
        [sg.Button("Search", bind_return_key=True)],
        [sg.Checkbox("Use AI-enhanced search", key="use_ai")],
        [sg.Multiline(size=(80, 20), key="results")]
    ]

    window = sg.Window("Tip of the Tongue Retrieval", layout)

    # Event loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        # Handle search without AI
        if event == "Search":
            query = values["query"]
            # Replace with your IR system call:
            if values["use_ai"] == False:
                hits = searcher.search(query)
            else:
                hits = searcherAI.search(query)
            output = ""
            for hit in hits.values():
                output += f"{hit['rank']} | {hit['title']} | Score: {hit['score']:.4f}\n{hit['snippet']}\n\n"
            window["results"].update(output)
            
    window.close()