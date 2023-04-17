notes = {"C4": 1, "C#4": 2, "D4": 3, "D#4": 4
    , "E4": 5, "F4": 6, "F#4": 7, "G4": 8
    , "G#4": 9, "A4": 10, "A#4": 11, "B4": 12
    , "C5": 13, "C#5": 14, "D5": 15, "D#5": 16
    , "E5": 17, "F5": 18, "F#5": 19, "G5": 20
    , "G#5": 21, "A5": 22, "A#5": 23}

chords = {"A": ["A3", "C#4", "E4"],
          "Am": ["A3", "C4", "E4"],
          "C": ["C4", "E4", "G4"],
          "Cm": ["C4", "D#4", "G4"],
          "D": ["D4", "F#4", "A4"],
          "Dm": ["D4", "F4", "A4"],
          "E": ["E4", "G#4", "B4"],
          "Em": ["E4", "G4", "B4"],
          "F": ["F3", "A3", "C4"],
          "Fm": ["F3", "G#3", "C4"],
          "G": ["G3", "B3", "D4"],
          "Gm": ["G3", "A#3", "D4"]}

chord_notes = {"A": [10, 2, 5, 22, 14, 17],
               "Am": [10, 1, 5, 22, 13, 17],
               "C": [1, 5, 8, 13, 17, 20],
               "Cm": [1, 4, 8, 13, 16, 20],
               "D": [3, 7, 10, 15, 19, 22],
               "Dm": [3, 6, 10, 15, 18, 22],
               "E": [5, 9, 12, 17, 20],
               "Em": [5, 8, 12, 17, 20],
               "F": [6, 10, 1, 18, 22, 13],
               "Fm": [6, 9, 1, 18, 21, 13],
               "G": [8, 12, 3, 20, 15],
               "Gm": [8, 11, 3, 20, 23, 15]}

keys = {"A": [2, 4, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22],
        "Am": [1, 3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22],
        "C": [1, 3, 5, 6, 8, 10, 12, 13, 15, 17, 18, 20, 22],
        "Cm": [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 18, 20, 21, 23],
        "D": [2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22],
        "Dm": [1, 3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22],
        "E": [2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 22],
        "Em": [1, 3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22],
        "F": [1, 3, 5, 6, 8, 10, 11, 13, 15, 17, 18, 20, 22, 23],
        "Fm": [1, 2, 4, 6, 8, 9, 11, 13, 14, 16, 18, 20, 21, 23],
        "G": [1, 3, 5, 7, 8, 10, 12, 13, 15, 17, 19, 20, 22],
        "Gm": [1, 3, 4, 6, 8, 10, 11, 13, 15, 16, 18, 20, 22, 23]}

keys_roots = {"A": [10, 22],
              "Am": [10, 22],
              "C": [1, 13],
              "Cm": [1, 13],
              "D": [3, 15],
              "Dm": [3, 15],
              "E": [5, 17],
              "Em": [5, 17],
              "F": [6, 18],
              "Fm": [6, 18],
              "G": [8, 20],
              "Gm": [8, 20]}

tresillo_rhythm = [2, 2, 1]


def provide_chord_notes(chord_prog):
    translated_chords = []
    for i in chord_prog:
        translated_chords.append(chord_notes[i])

    return translated_chords


def genotype_translation(genotype):
    melody = []
    melody_itr = -1
    for i in genotype:
        if i == 0:
            melody[melody_itr][1] += 0.5
            continue
        else:
            note = list(notes.keys())[list(notes.values()).index(i)]
            melody.append([note, 0.5])
            melody_itr += 1

    return melody


def notes_durations(genotype):
    duration = []
    melody_itr = -1
    for i in genotype:
        if i == 0:
            duration[melody_itr] += 0.5
            continue
        else:
            duration.append(0.5)
            melody_itr += 1

    return duration


