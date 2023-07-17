import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"
username = "neo4j" 
password = "password" # Da modificare con la propria password

# Funzione per creare gli indici
def create_indexes():
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        session.run("CREATE TEXT INDEX title_tconst_index FOR (t:Title) ON (t.tconst)")
        session.run("CREATE TEXT INDEX professional_nconst_index FOR (p:Professional) ON (p.nconst)")

    driver.close()

start_time = time.time()

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for creating indexes: ", elapsed_time, "s")

create_indexes()
