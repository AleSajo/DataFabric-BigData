# Big Data - Progetto Data Fabric

| Studente | Matricola |
|:---|:---|
|Alessandro Sajeva|521125|
|Massimiliano Patrizi|508637|

# Descrizione del progetto
Questo progetto prende in esame dei dataset di IMDb (https://developer.imdb.com/non-commercial-datasets/) contenenti varie informazioni su film e lavoratori del mondo cinematografico.
Dopo aver effettuato delle trasformazioni e pulizia su questi dataset, vengono caricati all'interno di Neo4j, un Graph DBMS, in modo da poter visualizzare questi dati e le loro relazioni sottoforma di grafi o tabelle, oltre al rispettivo metagraph.


# Passaggi per la riproduzione
1. Installare i requirements\
    `pip install -r requirements.txt`

2. Aprire l'interfaccia di Neo4j ed effettuare il login\
    `brew services start neo4j`
   
4. Eseguire gli script python nell'ordine:\
    `(a) resetDatabase.py`\
    `(b) loadDatasetFromFolder.py`\
    `(c) createIndexes.py`\
    `(d) createRelations.py`
5. Utilizzare le query Cypher per interagire con i dati all'interno di Neo4j.

    Per visualizzare il metagraph eseguire questi passaggi
6. Spostare il file `apoc-5.9.0-core.jar` da `$NEO4J_HOME/labs` a `$NEO4J_HOME/plugins`
7. Eseguire il comando: `CALL apoc.meta.graph`

8. Per eseguire le pipeline: `sh launch_pipeline#.sh`
   
9. Per chiudere la connessione a Neo4j, digitare\
    `brew services stop neo4j`
