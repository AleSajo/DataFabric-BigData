###########################################
##### CODICE PRESO DAL PRIMO PROGETTO #####
###########################################

# L'idea è quella di esportare i dati da Neo4j in una forma
# in cui si possa lavorare con Spark. 

# Import per lavorare su Neo4j
import csv
import os
import time
from neo4j import GraphDatabase

# Import per lavorare con spark
from pyspark.sql import SparkSession
from pyspark.sql.functions import year, col, regexp_replace, length, split, explode, from_unixtime, row_number, sum as Ssum, desc as Sdesc
from pyspark.sql.window import Window

# Prima fase di estrazione dati con Neo4j


# Crea la sessione Spark
spark = SparkSession.builder.appName("ReviewsAnalysis").getOrCreate()

# Carica i dati
reviews = spark.read.format("csv").option("header", "true").option("delimiter", ";").load("file:///Users/alessandro/Development/BigData/BigData-PrimoProgetto2023/ReviewsCleaned.csv")

userId_Num_Den = reviews.select(
    col("UserId").alias("userid"),
    col("HelpfulnessNumerator").cast("float").alias("helpfulnessnumerator"),
    col("HelpfulnessDenominator").cast("float").alias("helpfulnessdenominator")
)

userId_appreciation = userId_Num_Den \
  .groupBy("userid") \
  .agg(Ssum(col("helpfulnessnumerator")).alias("sum_numerator"), Ssum(col("helpfulnessdenominator")).alias("sum_denominator")) \
  .withColumn("mean", col("sum_numerator")/col("sum_denominator")) \
  .orderBy(Sdesc(col("mean"))) \
  .limit(10) \
  .select("userid", "mean")

userId_appreciation.show()