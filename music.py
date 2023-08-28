notes = {"C4": 1, "C#4": 2, "D4": 3, "D#4": 4
    , "E4": 5, "F4": 6, "F#4": 7, "G4": 8
    , "G#4": 9, "A4": 10, "A#4": 11, "B4": 12
    , "C5": 13, "C#5": 14, "D5": 15, "D#5": 16
    , "E5": 17, "F5": 18, "F#5": 19, "G5": 20
    , "G#5": 21, "A5": 22, "A#5": 23, "B5": 24}

notes_2 = {'A2': 1, 'A♯2': 2, 'B2': 3, 'C3': 4, 'C♯3': 5, 'D3': 6, 'D♯3': 7, 'E3': 8, 'F3': 9, 'F♯3': 10, 'G3': 11,
           'G♯3': 12, 'A3': 13, 'A♯3': 14, 'B3': 15, 'C4': 16, 'C♯4': 17, 'D4': 18, 'D♯4': 19, 'E4': 20, 'F4': 21,
           'F♯4': 22, 'G4': 23, 'G♯4': 24, 'A4': 25, 'A♯4': 26, 'B4': 27, 'C5': 28, 'C♯5': 29, 'D5': 30, 'D♯5': 31,
           'E5': 32, 'F5': 33, 'F♯5': 34, 'G5': 35, 'G♯5': 36, 'A5': 37, 'A♯5': 38, 'B5': 39, 'C6': 40}

chords = {"A": ["A3", "C#4", "E4"],
          "Am": ["A3", "C4", "E4"],
          "B": ["B3", "D#4", "F#4"],
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
               "B": [4, 7, 12, 16, 19, 24],
               "Bm": [12, 24, 3, 15, 7, 19],
               "C": [1, 5, 8, 13, 17, 20],
               "Cm": [1, 4, 8, 13, 16, 20],
               "D": [3, 7, 10, 15, 19, 22],
               "Dm": [3, 6, 10, 15, 18, 22],
               "E": [5, 9, 12, 17, 20, 24],
               "Em": [5, 8, 12, 17, 20, 24],
               "F": [6, 10, 1, 18, 22, 13],
               "Fm": [6, 9, 1, 18, 21, 13],
               "G": [8, 12, 3, 20, 15, 24],
               "Gm": [8, 11, 3, 20, 23, 15]}

chord_notes_2 = {'A': [1, 13, 25, 37, 5, 17, 29, 8, 20, 32],
               'Am': [1, 13, 25, 37, 4, 16, 28, 40, 8, 20, 32],
               'B': [3, 15, 27, 39, 7, 19, 31, 10, 22, 34],
               'Bm': [3, 15, 27, 39, 6, 18, 30, 10, 22, 34],
               'C': [4, 16, 28, 40, 8, 20, 32, 11, 23, 35],
               'Cm': [4, 16, 28, 40, 7, 19, 31, 11, 23, 35],
               'D': [6, 18, 30, 10, 22, 34, 1, 13, 25, 37],
               'Dm': [6, 18, 30, 9, 21, 33, 1, 13, 25, 37],
               'E': [8, 20, 32, 12, 24, 36, 3, 15, 27, 39],
               'Em': [8, 20, 32, 11, 23, 35, 3, 15, 27, 39],
               'F': [9, 21, 33, 1, 13, 25, 37, 4, 16, 28, 40],
               'Fm': [9, 21, 33, 12, 24, 36, 4, 16, 28, 40],
               'G': [11, 23, 35, 3, 15, 27, 39, 6, 18, 30],
               'Gm': [11, 23, 35, 2, 14, 26, 38, 6, 18, 30]}



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


def obtain_genotype(text):
    notes_list = text.split(",")
    complete_notes = []
    pitches = []
    durations = []
    chromosome = []
    for i in range(len(notes_list)):
        notes_list[i] = notes_list[i].replace(" quarterLength ", '')
        notes_list[i] = notes_list[i].replace(" ", '')
        complete_notes.append(notes_list[i].split("="))
        pitch = complete_notes[i][0]
        duration = float(complete_notes[i][1])
        pitches.append(pitch)
        durations.append(duration)
        chromosome.append(notes[pitch])
        zeroes = int(duration/0.5) - 1
        for _ in range(zeroes):
            chromosome.append(0)

    return chromosome

# gen = [8, 13, 0, 17, 0, 17, 0, 13, 8, 8, 12, 15, 12, 15, 20, 20, 13, 10, 5, 10, 0, 13, 0, 17, 13, 10, 13, 0, 0, 18, 0, 0]
# print(genotype_translation(gen))