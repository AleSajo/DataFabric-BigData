import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"
username = "neo4j" 
password = "bigdataneo4j" # Da modificare con la propria password
#password = "neo4jjjj"

# Elimino gli indici
def drop_indexes():
    driver = GraphDatabase.driver(uri, auth=(username, password))

    try:
        with driver.session() as session:
            session.run("DROP INDEX title_tconst_index")
            driver.close()
    except:
        print("title_tconst_index does not exists")
    try:
        with driver.session() as session:
            session.run("DROP INDEX professional_nconst_index")
            driver.close()
    except:
        print("professional_nconst_index does not exists")

# Elimino i nodi
# Bisogna eliminare iterativamente gruppi di nodi perché altrimenti non ce la fa con la memoria
def delete_all_nodes():
    print("Deleting all nodes")
    i=0
    while i < 100:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        with driver.session() as session:
            session.run("MATCH (n) WITH n LIMIT 10000 DETACH DELETE n RETURN count(*);")
        driver.close()
        i=i+1


start_time = time.time()

# qui eseguo le cancellazioni step by step
drop_indexes()
delete_all_nodes()

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for database reset: ", elapsed_time, "s")