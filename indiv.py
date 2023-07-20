import time
import random
import concurrent.futures
from music21 import *
from music import *


class Individual:

    def __init__(self):
        self.melody = []
        self.melody_notes = []
        self.durations = []
        self.fitness = 0
        self.total_notes = 0
        self.scale_notes = []
        self.scale_roots = []
        self.o1 = 0
        self.o2 = 0
        self.o3 = 0
        self.o4 = 0
        self.o5 = 0
        self.o6 = 0
        self.o7 = 0
        self.o8 = 0
        self.o9 = 0
        self.o10 = 0
        self.o11 = 0

    def create_initial_melody_chords(self, chords):
        num_notes = len(chords) * 8
        starter_notes = provide_chord_notes(chords)
        idx = -1
        for i in range(0, num_notes):
            if i % 8 == 0:
                idx += 1
            self.melody.append(random.choice(starter_notes[idx]))
        self.get_melody_notes()
        self.scale_notes = keys[chords[0]]
        self.scale_roots = keys_roots[chords[0]]

    def create_initial_melody_same_note(self):
        self.melody = [1 for x in range(32)]
        print(self.melody)
        self.get_melody_notes()

    def create_initial_melody_random_notes(self):
        self.melody = [random.randrange(1, 23, 1) for i in range(32)]
        self.get_melody_notes()

    def get_melody_notes(self):
        # This function provides the notes present in a melody(ignoring note duration)
        self.melody_notes = [note for note in self.melody if note != 0]
        self.total_notes = len(self.melody_notes)
        self.durations = notes_durations(self.melody)

    def save_melody(self, chord_progression, filename):
        phenotype = genotype_translation(self.melody)
        treble_staff = stream.PartStaff()
        treble_staff.append(meter.TimeSignature('4/4'))
        chord_staff = stream.PartStaff()
        chord_staff.append(meter.TimeSignature('4/4'))

        with open('./melodies/'+filename+'.txt', 'w') as f:
            f.write("Time Signature: 4/4")
            f.write('\n')
            f.write("Key: " + chord_progression[0])
            f.write('\n')
            f.write("Melody: ")
            for notes in phenotype:
                treble_staff.append(note.Note(notes[0], quarterLength=notes[1]))
                f.write(str(notes[0]) + " quarterLength = " + str(notes[1]) + ",")
            f.write('\n')
            for this_chord in chord_progression:
                triad = chords[this_chord]
                chord_staff.append(chord.Chord(triad, quarterLength=4))
        result = stream.Score([treble_staff, chord_staff])
        result.write("musicxml", fp="C:/Users/34683/Desktop/TFG/Melody_Composition_GA/melodies/"+filename)
        result.write("midi", fp="C:/Users/34683/Desktop/TFG/Melody_Composition_GA/melodies/" + filename+".midi")
        # result.show()

    def play_melody(self, chord_progression):
        phenotype = genotype_translation(self.melody)
        treble_staff = stream.PartStaff()
        treble_staff.append(meter.TimeSignature('4/4'))
        chord_staff = stream.PartStaff()
        chord_staff.append(meter.TimeSignature('4/4'))
        for notes in phenotype:
            treble_staff.append(note.Note(notes[0], quarterLength=notes[1]))
        for this_chord in chord_progression:
            triad = chords[this_chord]
            chord_staff.append(chord.Chord(triad, quarterLength=4))
        result = stream.Score([treble_staff, chord_staff])
        result.show()

    def evaluate_melody_1(self, chord_prog, num_objectives=9):
        chords_notes = provide_chord_notes(chord_prog)
        self.fitness = 0
        self.fitness += 0.5 * self.objective_1(chords_notes)
        self.fitness += (0.3 / 4) * self.objective_2()
        self.fitness += 0.1 * self.objective_3()
        self.fitness += (0.3 / 4) * self.objective_4()
        self.fitness += (0.3 / 4) * self.objective_5()
        self.fitness += self.objective_6()
        self.fitness += self.objective_7()
        self.fitness += (0.3 / 4) * self.objective_8()
        self.fitness += 0.1 * self.objective_9()

    def evaluate_melody_2(self, chord_prog, num_objectives=5):
        chords_notes = provide_chord_notes(chord_prog)
        self.fitness = 0
        self.fitness += 0.5 * self.objective_1(chords_notes)
        self.fitness += (0.5 / 3) * self.objective_3()
        self.fitness += self.objective_6()
        self.fitness += self.objective_7()
        self.fitness += (0.5 / 3) * self.objective_8()
        self.fitness += (0.5 / 3) * self.objective_9()
        self.fitness += self.objective_11()

    def evaluate_melody_3(self, chord_prog, num_objectives=11):
        chords_notes = provide_chord_notes(chord_prog)
        self.fitness = 0
        self.fitness += 0.2 * self.objective_1(chords_notes)
        self.fitness += (0.2 / 8) * self.objective_2()
        self.fitness += 0.1 * self.objective_3()
        self.fitness += (0.2 / 8) * self.objective_4()
        self.fitness += (0.2 / 8) * self.objective_5()
        self.fitness += (0.2 / 8) * self.objective_6()
        self.fitness += 0.1 * self.objective_7()
        self.fitness += (0.2 / 8) * self.objective_8()
        self.fitness += (0.2 / 8) * self.objective_9()
        self.fitness += 0.3 * self.objective_10(tresillo_rhythm)
        self.fitness += 0.1 * self.objective_11()

    def objective_1(self, chord_prog):
        # Objective 1: Checks the percentage of notes corresponding to chord notes
        idx = -1
        chord_notes = 0
        for i, note in enumerate(self.melody):
            if i % 8 == 0:
                idx += 1
            if note in chord_prog[idx]:
                chord_notes += 1
        # print("O1: ", chord_notes/self.total_notes)
        self.o1 = chord_notes / self.total_notes
        return chord_notes / self.total_notes

    def objective_2(self):
        # Objective 2: Checks how many scale steps away is the next note
        one_step = 0
        two_steps = 0
        same_note = 0
        three_steps = 0
        four_steps = 0

        for i in range(0, len(self.melody_notes) - 1):
            note = self.melody_notes[i]
            next_note = self.melody_notes[i + 1]

            if note == next_note:
                same_note += 1

            if (note in self.scale_notes) and (next_note in self.scale_notes):
                scale_index = self.scale_notes.index(note)

                if scale_index == len(self.scale_notes) - 1:
                    if next_note == self.scale_notes[scale_index - 1]:
                        one_step += 1
                    elif next_note == self.scale_notes[scale_index - 2]:
                        two_steps += 1
                    elif next_note == self.scale_notes[scale_index - 3]:
                        three_steps += 1
                    elif next_note == self.scale_notes[scale_index - 4]:
                        four_steps += 1

                elif scale_index == 0:
                    if next_note == self.scale_notes[scale_index + 1]:
                        one_step += 1
                    elif next_note == self.scale_notes[scale_index + 2]:
                        two_steps += 1
                    elif next_note == self.scale_notes[scale_index + 3]:
                        three_steps += 1
                    elif next_note == self.scale_notes[scale_index + 4]:
                        four_steps += 1

                else:
                    if next_note == self.scale_notes[scale_index + 1] or next_note == self.scale_notes[scale_index - 1]:
                        one_step += 1
                    elif next_note == self.scale_notes[scale_index + 1] or next_note == self.scale_notes[
                        scale_index - 2]:
                        two_steps += 1
                    elif next_note == self.scale_notes[scale_index + 1] or next_note == self.scale_notes[
                        scale_index - 3]:
                        three_steps += 1
                    elif next_note == self.scale_notes[scale_index + 1] or next_note == self.scale_notes[
                        scale_index - 4]:
                        four_steps += 1

            else:
                if abs(note - next_note) == 1 or abs(note - next_note) == 2:
                    one_step += 1
                if abs(note - next_note) == 6 or abs(note - next_note) == 8:
                    two_steps += 1
                if abs(note - next_note) == 10:
                    three_steps += 1
                if abs(note - next_note) == 12 or abs(note - next_note) == 14:
                    four_steps += 1

        obj2_value = one_step + two_steps + (same_note * 0.9) + (three_steps * 0.8) + (four_steps * 0.7)
        if self.total_notes == 1:
            obj2_value = 0
        else:
            obj2_value /= self.total_notes - 1

        # print("O2: ", obj2_value)
        self.o2 = obj2_value
        return obj2_value

    def objective_3(self):
        # Objective 3: Checks whether a given note triplet forms a falling, rising or stable pattern
        falling = 0
        rising = 0
        stable = 0
        i = 0
        prev_pattern = 0  # This variable checks if the previous note belonged to a pattern
        while i < len(self.melody_notes) - 2:
            note1 = self.melody_notes[i]
            note2 = self.melody_notes[i + 1]
            note3 = self.melody_notes[i + 2]

            if (note1 > note2) and (note2 > note3):
                if prev_pattern == 0:
                    falling += 3
                else:
                    falling += 2
                prev_pattern = 1
                i += 2
                continue

            if (note1 < note2) and (note2 < note3):
                if prev_pattern == 0:
                    rising += 3
                else:
                    rising += 2
                prev_pattern = 1
                i += 2
                continue

            if (note1 == note2) and (note2 == note3):
                if prev_pattern == 0:
                    stable += 3
                else:
                    stable += 2
                prev_pattern = 1
                i += 2
                continue

            prev_pattern = 0
            i += 1

        obj3_value = falling + rising + (0.8 * stable)
        obj3_value /= self.total_notes
        self.o3 = obj3_value

        # print("O3: ", obj3_value)
        # if obj3_value >= 1:
        #     self.o3 = 1
        #     return 1
        # self.o3 = obj3_value
        return obj3_value

    def objective_4(self):
        # Objective 4: Checks if the first note of the melody is the root note of the key
        if self.melody_notes[0] in self.scale_roots:
            self.o4 = 1
            return 1

        self.o4 = 0
        return 0

    def objective_5(self):
        # Objective 5: checks if the last note of the melody is the root note of the key
        if self.melody_notes[-1] in self.scale_roots:
            self.o5 = 1
            return 1

        self.o5 = 0
        return 0

    def objective_6(self):
        # Objective 6: Checks if two consecutive notes are more than five scale-steps away (fitness punishment)
        over_fifth = 0

        for i in range(0, len(self.melody_notes) - 1):
            note = self.melody_notes[i]
            next_note = self.melody_notes[i + 1]

            if abs(note - next_note) > 7:
                over_fifth += 1
        # print("O6: ", -over_fifth/(len(self.melody_notes)-1))
        if self.total_notes == 1:
            self.o6 = 0
            return 0

        self.o6 = -over_fifth / (len(self.melody_notes) - 1)
        return -over_fifth / (len(self.melody_notes) - 1)

    def objective_7(self):
        # Objective 7: Checks if two consecutive notes have a significant duration differencene (punishment)
        durations = notes_durations(self.melody)
        duration_change = 0
        for i in range(0, len(durations) - 1):
            note = durations[i]
            next_note = durations[i + 1]

            if abs(note - next_note) > 1:
                duration_change += 1
        # print("O7: ", -duration_change / (len(self.melody_notes) - 1))
        if self.total_notes == 1:
            self.o7 = 0
            return 0
        self.o7 = -duration_change / (len(self.melody_notes) - 1)
        return -duration_change / (len(self.melody_notes) - 1)

    def objective_8(self):
        # Objective 8: Checks if the pitch range surpasses an octave (punishent)
        lowest_pitch = min(self.melody_notes)
        highest_pitch = max(self.melody_notes)

        if highest_pitch - lowest_pitch <= 18:
            # print("O8: met")
            self.o8 = 1
            return 1

        self.o8 = 0
        return 0

    def objective_9(self):
        # Objective 9: Checks if there is enough tone variety to avoid same note repetition
        notes_set = set(self.melody_notes)
        different_notes = len(notes_set)
        if different_notes >= 5:
            # print("O9: met")
            self.o9 = 1
            return 1

        self.o9 = 0
        return 0

    def objective_10(self, pattern):
        num_notes = len(pattern)
        shortest_note = pattern.index(min(pattern))
        iterator_max = len(self.durations) - (num_notes - 1)
        satisfies_pattern = 0
        for i in range(0, iterator_max):
            base_duration = self.durations[i + shortest_note]
            j = i
            pattern_idx = 0
            follows_pattern = 1
            while j < (i + num_notes - 1):
                # print(pattern_idx)
                current_duration = self.durations[j]
                pattern_beat = pattern[pattern_idx]
                if current_duration != base_duration * pattern_beat:
                    follows_pattern = 0
                    break
                j += 1
                pattern_idx += 1

            if follows_pattern:
                satisfies_pattern += num_notes
                i += num_notes

        self.o10 = satisfies_pattern / len(self.melody_notes)
        return satisfies_pattern / len(self.melody_notes)

    def objective_11(self):
        if max(self.durations) > 1:
            self.o11 = -1
            return -1

        self.o11 = 0
        return 0

# mike = Individual()
# mike.create_initial_melody_chords(["C","Gm","Am","F"])
# print(mike.melody)
# print(genotype_translation(mike.melody))
# mike.evaluate_melody(["C","Gm","Am","F"])
# print(mike.fitness)
# print(mike.scale_notes)
# a = Individual()
# a.create_initial_melody_chords(["C","Gm","Am","F"])
# print(a.melody)
# print(genotype_translation(a.melody))
# a.evaluate_melody(["C","Gm","Am","F"])
# print(a.fitness)
# b = Individual()
# b.create_initial_melody_chords(["C","Gm","Am","F"])
# print(b.melody)
# print(genotype_translation(b.melody))
# b.evaluate_melody(["C","Gm","Am","F"])
# print(b.fitness)
