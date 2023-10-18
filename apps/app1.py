from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.options(header='True', inferSchema='True').csv("/opt/spark-data/forworkers/*.csv")

df.count()
df.printSchema()
df.select("categories").distinct().show()

def myFunc(s):
  return [(s["categories"], 1)]

lines = df.rdd.flatMap(myFunc).reduceByKey(lambda a, b: a + b)
