def open_and_print_file_per_line(path):
    with open(path) as file:
        
        songs = [line.strip() for line in file]

    sorted_songs = sorted(songs)

    for word in sorted_songs:
        print(f'Linea: {word}')

open_and_print_file_per_line('songs.txt')