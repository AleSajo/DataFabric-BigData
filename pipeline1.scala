import org.apache.spark.sql.{SaveMode, SparkSession}
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.functions._

val spark = SparkSession.builder().getOrCreate()

val df = (spark.read.format("org.neo4j.spark.DataSource")
  .option("url", "bolt://localhost:7687")
  .option("authentication.basic.username", "neo4j")
  .option("authentication.basic.password", "bigdataneo4j")
  .option("labels", "Title")
  .load())

df.show()

// Save the DataFrame to JSON format
val outputPath = "output.json"
df.write.mode(SaveMode.Overwrite) // Change SaveMode as per your requirement
  .json(outputPath)