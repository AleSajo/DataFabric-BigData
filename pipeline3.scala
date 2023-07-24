import org.apache.spark.sql.{SaveMode, SparkSession}
import org.apache.spark.sql.functions._
import scala.io.StdIn.readLine

val spark = SparkSession.builder().getOrCreate()

println("Seleziona il genere:")
println("1 - Comedy")
println("2 - Drama")
println("3 - Sport")
println("4 - Animation")
println("5 - Horror")
println("6 - Fantasy\n")

val genreSelection = readLine().trim.toInt

val (cypherQuery, genre) = genreSelection match {
  case 1 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Comedy" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Comedy")
  case 2 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Drama" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Drama")
  case 3 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Sport" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Sport")
  case 4 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Animation" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Animation")
  case 5 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Horror" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Horror")
  case 6 =>
    val query =
      """
        |MATCH (t:Title)-[:AVERAGE_RATING]->(r:Rating)
        |WHERE "Fantasy" IN split(t.genres, ",")
        |RETURN t.primaryTitle AS primaryTitle,
        |       t.genres AS genres,
        |       t.startYear AS year,
        |       r.averageRating AS averageRating
        |ORDER BY r.averageRating DESC
        |""".stripMargin
    (query, "Fantasy")
  case _ => throw new IllegalArgumentException("Invalid selection")
}

println(s"Hai selezionato il genere '$genre'\n")

val df = (spark.read.format("org.neo4j.spark.DataSource")
  .option("url", "bolt://localhost:7687")
  .option("authentication.basic.username", "neo4j")
  .option("authentication.basic.password", "neo4jjjj")
  .option("query", cypherQuery)
  .load())

df.show(100)

spark.close()
