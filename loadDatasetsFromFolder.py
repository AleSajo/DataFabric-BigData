import csv
import os
import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"
username = "neo4j" 
password = "password" # Da modificare con la propria password

# Funzione per l'importazione dei dati
def import_data(folder_path):
    driver = GraphDatabase.driver(uri, auth=(username, password))

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.tsv'):
            file_path = os.path.join(folder_path, file_name)
            node_label = file_name.split('.')[0]

            with open(file_path, 'r') as file:
                reader = csv.DictReader(file, delimiter='\t')
                headers = reader.fieldnames

                with driver.session() as session:
                    transaction = session.begin_transaction()
                    counter = 0

                    for row in reader:
                        counter = counter + 1

                        if counter == 101:
                            transaction.commit()
                            print(f"Commit")
                            transaction = session.begin_transaction()
                            counter = 0

                        cleaned_row = {k: v.replace('"', "'").replace('\\N', '') for k, v in row.items()}
                        properties = ', '.join([f"{header}: ${header}" for header in headers])
                        query = f"CREATE (:{node_label} {{{properties}}})"
                        transaction.run(query, **cleaned_row)

    driver.close()

# Esempio di utilizzo
folder_path = 'data100K'

start_time = time.time()

import_data(folder_path)

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for import: ", elapsed_time, "s")