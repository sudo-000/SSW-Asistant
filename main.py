import mido
from tkinter import filedialog, Tk
import threading
import time
Tk().withdraw()
def Ch1(Track):
    for Event in Track:
        if Event.type == 'note_on' or Event.type == 'note_off' or Event.type == 'aftertouch' or Event.type == 'polytouch':
            Event.channel = 0
        elif Event.type == 'control_change' or Event.type == 'program_change' or Event.type == 'pitchwheel':
            Event.channel = 1
        elif Event.type == 'track_name':
            Event.name = "Made with SSW Assistant  |  Program written by: Happy_mimimix"
print("Welcome to SSW Assistant Ver1.02! Created by: Happy_mimimix")
print("Please select the midi file you want to open in the popup file dialog: ")
print()
f = str(filedialog.askopenfilename(filetypes=[('midi file', '.mid')]))
print("Loading midi file... ")
mid = mido.MidiFile(f)
print("Moving all events to channel 1... ")
Threads = []
for Track in mid.tracks:
    Threads.append(threading.Thread(target=Ch1, args=(Track,)))
    Threads[-1].start()
for EveryThread in Threads:
    EveryThread.join()
print("Merging tracks... ")
NewTrack = mido.merge_tracks(mid.tracks)
NewTrack.name = "Made with SSW Assistant  |  Program written by: Happy_mimimix"
print("Exporting midi file... ")
mid.tracks.clear()
mid.tracks.append(NewTrack)
mid.type = 0
mid.save(f.rstrip(".mid") + " - For Singer Song Writer.mid")
print()
print("All done! New file saved to: " + f.rstrip(".mid") + " - For Singer Song Writer.mid")
time.sleep(3)