import customtkinter as ct
import pygame
import os
from GA import GeneticAlgorithm

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")
root = ct.CTk()
root.geometry("600x500")
root.title("Melody Generator")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
pygame.mixer.init()


def generate_samples(samples, chords_selected):
    for widget in frame.winfo_children():
        if widget not in main_widgets:
            widget.destroy()
    label_frame = ct.CTkFrame(master=frame, width=450, height=300, fg_color="transparent")
    label_frame.grid_propagate(0)
    label_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")
    label_frame.columnconfigure(0, weight=1)
    load_label = ct.CTkLabel(master=label_frame, text="Loading Samples...")
    load_label.grid(row=0, column=0, columnspan=3)
    root.update_idletasks()
    chords = chords_selected.split("-")
    num_samples = int(samples)
    label_frame.destroy()
    # load_label.destroy()
    for i in range(1,num_samples+1):
        ga_test = GeneticAlgorithm(chord_prog=chords, filename="examples/" + chords_selected + "-" + str(i))
        ga_test.run_genetic_algorithm()
        sample_label = ct.CTkLabel(master=frame, text="Sample " + str(i) + ":")
        sample_label.grid(row=2+i, column=0, pady=(10, 10))
        play_button = ct.CTkButton(master=frame, text="Play", command=lambda k=i:play(str(k), chords_selected))
        play_button.grid(row=2+i,column=1, pady=(10,10))
        view_button = ct.CTkButton(master=frame, text="View", command=lambda k=i: view(str(k), chords_selected))
        view_button.grid(row=2 + i, column=2, pady=(10, 10))


def play(id, chords):
    sample = f'melodies/examples/{chords}-{id}.midi'
    pygame.mixer.music.load(sample)
    pygame.mixer.music.play(loops=0)

def view(id, chords):
    sample = f'C:/Users/34683/Desktop/TFG/Melody_Composition_GA/melodies/examples/{chords}-{id}.musicxml'
    os.startfile(sample)

frame = ct.CTkFrame(master=root, width=450, height=300)
frame_bg = frame['bg']
frame.grid(row=0, column=0, padx=(50,50), pady=(10,10), sticky="nsew", columnspan=2)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
main_widgets = []
label = ct.CTkLabel(master=frame, text="Melody Generator", font=('Arial', 25))
main_widgets.append(label)
label.grid(row=0, column=0, columnspan=3, pady=(10,10))


chord_selector = ct.CTkOptionMenu(frame, values=["C-G-Am-F", "C-F-G-F", "Am-F-C-G", "Dm-G-C-F", "C-Am-F-G", "G-B-C-Cm"])
main_widgets.append(chord_selector)
chord_selector.grid(row=1, column=0, pady=(10,50), padx=(5,5))
chord_selector.set("Select a Chord Progression")

select_samples = ct.CTkEntry(master=frame, placeholder_text="Number of Samples")
main_widgets.append(select_samples)
select_samples.grid(row=1, column=1, pady=(10,50), padx=(5,5))

generate_button = ct.CTkButton(master=frame, text="Generate Samples",
                               command=lambda: generate_samples(select_samples.get(), chord_selector.get()))
main_widgets.append(generate_button)
generate_button.grid(row=1, column=2, pady=(10,50), padx=(5,5))

root.mainloop()