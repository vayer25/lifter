import csv


countries_list = [
	{
		'name': 'Costa Rica',
		'capital': 'San José',
		'currency': 'Colón',
		'area_km2': '51,100',
	},
	{
		'name': 'Colombia',
		'capital': 'Bogotá',
		'currency': 'Peso Colombiano',
		'area_km2': '1,141,748',
	},
	{
		'name': 'México',
		'capital': 'Ciudad de México',
		'currency': 'Peso Mexicano',
		'area_km2': '1,972,550',
	},
]

country_headers = (
	'name',
	'capital',
	'currency',
	'area_km2',
)

def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

write_csv_file('countries.csv', countries_list, country_headers)

#este es para crear un documento al darle run a esto se crea automaticamnete countries.csv


# We are defining a function named write_csv_file. It takes:
#file_path: The name of the file we want to create ('countries.csv')
#data: The list of country dictionaries
#headers: The column names


# Opens the file in write mode ('w')
#'utf-8' makes sure it can handle accents like "México" and "San José" correctly

# Creates a CSV writer that knows how to handle dictionaries (DictWriter).
# It uses your headers to match the dictionary keys to column names.

#     writer.writeheader() = Writes the column titles first: name, capital, currency, area_km2

#     writer.writerows(data) = Writes each dictionary in the list as a row in the CSV file.

# write_csv_file('countries.csv', countries_list, country_headers)
#"Use the function and write a file named countries.csv using the country data and headers we provided."