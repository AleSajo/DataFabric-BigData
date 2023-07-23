import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"
username = "neo4j" 
password = "bigdataneo4j" # Da modificare con la propria password

# Funzione per creare gli indici
def create_indexes():
    driver = GraphDatabase.driver(uri, auth=(username, password))

    # Text indexes are a type of single-property index. Unlike range indexes, text indexes index only properties with string values.
    # Using the keyword IF NOT EXISTS makes the command idempotent, and no error will be thrown if you attempt to create the same index twice.
    with driver.session() as session:
        session.run("CREATE TEXT INDEX title_tconst_index IF NOT EXISTS FOR (t:Title) ON (t.tconst)")
        session.run("CREATE TEXT INDEX professional_nconst_index IF NOT EXISTS FOR (p:Professional) ON (p.nconst)")

    driver.close()

start_time = time.time()

create_indexes()

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for creating indexes: ", elapsed_time, "s")