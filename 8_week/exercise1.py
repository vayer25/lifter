# Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

def open_and_print_file_per_line(path):
    with open(path) as file:
        # Read each line and remove newline characters
        songs = [line.strip() for line in file]

    # Sort the list alphabetically
    sorted_songs = sorted(songs)

    # Print each line with label
    for word in sorted_songs:
        print(f'Linea: {word}')

open_and_print_file_per_line('songs.txt')
