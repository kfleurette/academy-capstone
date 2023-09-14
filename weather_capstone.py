## Getting started
## Task 1: Extract, transform and load weather data from S3 to Snowflake
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, StructType

config = {
        'spark.jars.packages' : 'org.apache.hadoop:hadoop-aws:3.2.0',
        'fs.s3a.aws.credentials.provider' : 'com.amazonaws.auth.DefaultAWSCredentialsProviderChain'}

conf = SparkConf().setAll(config.items())
spark =  SparkSession.builder.config(conf=conf).getOrCreate()

df = spark.read.json("s3a://dataminded-academy-capstone-resources/raw/open_aq/")
df.printSchema()

## Step 1: Extract and transform


clean = df.select(
    [ "*",
    "Coordinates.longitude",
    "coordinates.latitude",
    "date.local",
    "date.utc"
    ]
)
clean.show()

drop_bad_colummns = clean.drop("coordinates", "date")

drop_bad_colummns.show()
