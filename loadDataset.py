import csv
import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"  # L'URI non corrisponde a quello su cui usiamo neo4j browser, di default è questo
username = "neo4j"
password = "bigdataneo4j"

# Funzione per l'importazione dei dati
def import_data(file_path):
    driver = GraphDatabase.driver(uri, auth=(username, password))
    node_label = file_path.split('/')[-1].split('.')[0]

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        headers = reader.fieldnames

        with driver.session() as session:
            for row in reader:
                cleaned_row = {k: v.replace('"', "'").replace('\\N', '') for k, v in row.items()}
                properties = ', '.join([f"{header}: ${header}" for header in headers])
                query = f"CREATE (:{node_label} {{{properties}}})"
                session.run(query, **cleaned_row)

    driver.close()

file_path = 'data/Professional.tsv'

start_time = time.time()

import_data(file_path)

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for import: ", elapsed_time, "s")