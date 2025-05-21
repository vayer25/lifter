import csv

add_games = int(input("How many video games would you like to add? "))

video_games = []

for i in range(add_games):
    print(f"\nVideo game number: {i+1}")
    name = input("Name: ")
    genre = input("Genre: ")
    developer = input("Developer company: ")
    classification = input("ESRB classification: ")

    video_game = {
        'Name': name,
        'Genre': genre,
        'Developer': developer,
        'ESRB Classification': classification
    }

    video_games.append(video_game)

with open('video_games_tab.txt', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Name', 'Genre', 'Developer', 'ESRB Classification']
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames,
        delimiter='\t',
        quotechar='|',
        quoting=csv.QUOTE_MINIMAL  
    )

    writer.writeheader()
    writer.writerows(video_games)

print('\nThe information has been saved in the tab-separated file with custom quote characters.')
