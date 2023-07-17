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
    (OPZIONALE) eliminare i nodi precaricati in neo4j tramite query cypher
    `MATCH (n:nodeName) DETACH DELETE n`
3. Eseguire gli script python nell'ordine:\
    `(a) loadDatasetFromFolder.py`\
    `(b) createIndexes.py`\
    `(c) createRelations.py`
4. Utilizzare le query Cypher per interagire con i dati all'interno di Neo4j.

    Per visualizzare il metagraph eseguire questi passaggi
5. Spostare il file `apoc-5.9.0-core.jar` da `$NEO4J_HOME/labs` a `$NEO4J_HOME/plugins`
6. Eseguire il comando: `CALL apoc.meta.graph`
7. Per chiudere la connessione a Neo4j, digitare\
    `brew services stop neo4j`