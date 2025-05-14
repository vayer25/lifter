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


with open('video_games.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Name', 'Genre', 'Developer', 'ESRB Classification']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(video_games)

print('\nThe information has been saved in the database correctly.') 
