// This pipeline returns the crews that worked in the most rated titles

import org.apache.spark.sql.{SaveMode, SparkSession}
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

val spark = SparkSession.builder().getOrCreate()


/* The stripMargin method removes the common leading whitespace from each line in the string up to the | character (if present)
*/
val cypherQuery =
      """
        |MATCH (c)-[:HAVE_WORKED_ON]->(t)-[:AVERAGE_RATING]->(r)
        |RETURN c.tconst AS tconst, 
        |       t.primaryTitle AS primaryTitle,
        |       c.directors AS directors, 
        |       c.writers AS writers,
        |       r.averageRating AS rating
        |ORDER BY r.averageRating DESC
        |""".stripMargin


val df = (spark.read.format("org.neo4j.spark.DataSource")
  .option("url", "bolt://localhost:7687")
  .option("authentication.basic.username", "neo4j")
  //.option("authentication.basic.password", "neo4jjjj")
  .option("authentication.basic.password", "bigdataneo4j")
  .option("query", cypherQuery)
  .load())

df.show(100)

val filteredDf = df.filter(df("rating") > 9.3)

print("Showing crews that worked on title rated more than 9.3\n")
filteredDf.show(100)

val avgRatingByDirectorDf = filteredDf.groupBy("directors")
  .agg(avg("rating")
  .alias("averageRating"))

print("Showing average title rating by director\n")
avgRatingByDirectorDf.show(100)

// Save the DataFrame to JSON format
/* 
val outputPath = "output_dir"
df.write.mode(SaveMode.Overwrite) // Change SaveMode as per your requirement
  .json(outputPath)
*/

spark.close()