import pygame
import time
import random
#import dart_balloon_game

pygame.init()
 
display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
 
block_color = (53,115,255)

import PySimpleGUI as sg
"""
    Demo - 2 simultaneous windows using read_all_window
    Window 1 launches window 2
    BOTH remain active in parallel
    Both windows have buttons to launch popups.  The popups are "modal" and thus no other windows will be active
    Copyright 2020 PySimpleGUI.org
"""
def make_win1():
    layout = [[sg.Text('The Arcade'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Text('Click the game of your choice. Enjoy gaming!')],
              [sg.Button('Tic Tac Toe'), sg.Button('Dart Balloon'), sg.Button('Exit')]]
    return sg.Window('Arcade Game', layout, location=(800,600), finalize=True)
def make_win2():
    layout = [[sg.Text('Tic Tac Toe')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Popup'), sg.Button('Exit')]]
    return sg.Window('Dart Balloon Game', layout, finalize=True)
window1, window2 = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Tic Tac Toe':
        sg.popup('Loading...')
        import tic_tac_toe
    elif event == 'Dart Balloon':
        sg.popup('Loading...')
        import dart_balloon_game
    elif event == 'Launch 2nd Window' and not window2:
        window2 = make_win2()
    elif event == '-IN-':
        window['-OUTPUT-'].update(f'You enetered {values["-IN-"]}')
        print ('Demo')
    elif event == 'Erase':
        window['-OUTPUT-'].update('')
        window['-IN-'].update('')
window.close()