# Create a list of the BRICS countries
country = [ 
            "Brazil", 
            "Russia", 
            "India", 
            "China", 
            "South Africa"
          ]

"""Create a dictionary of BRICS capitals.
Note that South Africa has 3 capitals. Therefore, we embed a list inside
the dictionary.
"""

capitals = {
    "Brazil": "Brasilia",
    "Russia": "Moscow",
    "India": "New Delhi",
    "China": "Beijing",
    "South Africa": [
                        "Pretoria",
                        "Cape Town",
                        "Bloemfontein"
                    ]
           }

# Print the list and dictionary
print( "country" )
print( "capitals" )
"""
What response did you get?
Se obtuvo las palabras country y capitals resaltadas en azul.
Why did the list and dictionary contents not print?
Porque al poner el comando print se debió poner el nombre de la lista y el diccionario sin comillas.
Fix the code and run the script again.
"""

print(country)
print (capitals)

print( capitals["South Africa"][1] )
"""
Why did you get an error for the 2nd capital of South Africa?
Hint: Check the syntax for the index value.
Porque hay un error en la sintaxis. Debemos cerrar el corchete luego de la comilla que cierra la palabra Africa.
"""
