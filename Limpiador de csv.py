import csv

# Lee el archivo CSV y elimina duplicados
def remove_duplicates(input_file, output_file):
    seen = set()
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in reader:
            ra_dec = (row['ra'], row['dec'])
            if ra_dec not in seen:
                seen.add(ra_dec)
                writer.writerow(row)

# Nombre del archivo CSV de entrada y salida
input_file = r'C:\Users\vmgv0\Downloads\Base de datos mango.csv'
output_file = r'C:\Users\vmgv0\Downloads\Base de datos mango - copia.csv'

remove_duplicates(input_file, output_file)
print("El archivo CSV limpio se ha creado como:", output_file)
