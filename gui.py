import customtkinter as ct
import pygame
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
    chords = chords_selected.split("-")
    num_samples = int(samples)
    for i in range(1,num_samples+1):
        ga_test = GeneticAlgorithm(chord_prog=chords, filename="examples/" + chords_selected + "-" + str(i))
        ga_test.run_genetic_algorithm()
        sample_label = ct.CTkLabel(master=frame, text="Sample " + str(i) + ":")
        sample_label.grid(row=2+i, column=0, pady=(10, 10), columnspan=2)
        button_1 = ct.CTkButton(master=frame, text="Play", command=lambda k=i:play(str(k), chords_selected))
        button_1.grid(row=2+i,column=1, pady=(10,10), columnspan=2)


def play(id, chords):
    sample = f'melodies/examples/{chords}-{id}.midi'
    pygame.mixer.music.load(sample)
    pygame.mixer.music.play(loops=0)



frame = ct.CTkFrame(master=root, width=450, height=300)
frame.grid(row=0, column=0, padx=(50,50), pady=(10,10), sticky="nsew", columnspan=2)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)


label = ct.CTkLabel(master=frame, text="Melody Generator")
label.grid(row=0, column=0, columnspan=3, pady=(10,10))


chord_selector = ct.CTkOptionMenu(frame, values=["C-G-Am-F", "C-F-G-F", "Am-F-C-G", "Dm-G-C-F", "C-Am-F-G"])
chord_selector.grid(row=1, column=0, pady=(10,50), padx=(5,5))
chord_selector.set("Select a Chord")

num_samples = ct.CTkEntry(master=frame, placeholder_text="Number of Samples")
num_samples.grid(row=1, column=1, pady=(10,50), padx=(5,5))

generate_button = ct.CTkButton(master=frame, text="Generate Samples",
                               command=lambda: generate_samples(num_samples.get(), chord_selector.get()))
generate_button.grid(row=1, column=2, pady=(10,50), padx=(5,5))

root.mainloop()