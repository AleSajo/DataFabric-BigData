#!/bin/bash

# Ricorda di fornire i permessi a questo script eseguendo: chmod +x launch_pipeline2.sh

#$SPARK_HOME/bin/spark-shell \
#--jars spark-connector/neo4j-connector-apache-spark_2.12-5.0.1_for_spark_3.jar \
#-i /Users/Massimiliano/Documents/BigData/DataFabric-BigData/pipeline3.scala \

$SPARK_HOME/bin/spark-shell \
--jars spark-connector/neo4j-connector-apache-spark_2.12-5.0.1_for_spark_3.jar \
-i /Users/alessandro/Development/BigData/BigData-SecondoProgetto2023/DataFabric-BigData/pipeline3.scala \
