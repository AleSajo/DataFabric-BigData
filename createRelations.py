import time
from neo4j import GraphDatabase

# Configurazione del driver di Neo4j
uri = "bolt://localhost:7687"
username = "neo4j" 
password = "bigdataneo4j" # Da modificare con la propria password
#password = "neo4jjjj"

# Funzione per creare le relazioni
def create_relationships():
    driver = GraphDatabase.driver(uri, auth=(username, password))

    with driver.session() as session:
        session.run("""
            MATCH (p:Professional), (t:Title)
            WHERE t.tconst IN split(p.knownForTitles,",")
            MERGE (p)-[:HAS_WORKED_IN]->(t)
        """)
        session.run("""
            MATCH (c:Crew), (t:Title)
            WHERE t.tconst = c.tconst
            MERGE (c)-[:HAVE_WORKED_ON]->(t)
        """)
        session.run("""
            MATCH (a:Alias), (t:Title)
            WHERE t.tconst = a.titleId
            MERGE (t)-[:ALSO_KNOWN_AS]->(a)
        """)
        session.run("""
            MATCH (e:Episode), (t:Title)
            WHERE t.tconst = e.parentTconst
            MERGE (e)-[:IS_AN_EPISODE_OF]->(t)
        """)
        session.run("""
            MATCH (p:Principal), (a:Professional)
            WHERE a.nconst = p.nconst
            MERGE (a)-[:HAS_WORKED_AS]->(p)
        """)
        session.run("""
            MATCH (p:Principal), (t:Title)
            WHERE t.tconst = p.tconst
            MERGE (t)-[:FEATURED]->(p)
        """)
        session.run("""
            MATCH (r:Rating), (t:Title)
            WHERE t.tconst = r.tconst
            MERGE (t)-[:AVERAGE_RATING]->(r)
        """)
        session.run("""
            MATCH (p:Professional), (c:Crew)
            WHERE p.nconst IN split(c.directors,",")
            MERGE (p)-[:IS_DIRECTOR_IN_CREW]->(c)
        """)
        session.run("""
            MATCH (p:Professional), (c:Crew)
            WHERE p.nconst IN split(c.writers,",")
            MERGE (p)-[:IS_WRITER_IN_CREW]->(c)
        """)
        

    driver.close()

start_time = time.time()

# Esempio di utilizzo
create_relationships()

end_time = time.time()
elapsed_time = end_time - start_time
print("Time for establishing relations: ", elapsed_time, "s")
# Tempo di esecuzione registrato: 58.309s