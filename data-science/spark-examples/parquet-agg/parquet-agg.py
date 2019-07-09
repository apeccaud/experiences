import sys
from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: parquet-agg file", file=sys.stderr)
        sys.exit(-1)
    
    spark = SparkSession\
        .builder\
        .appName("parquet-agg")\
        .getOrCreate()

    parquet_file = spark.read.parquet(sys.argv[1])

    # Convert parquet file to temporary view in order to use SQL statements
    parquet_file.createOrReplaceTempView("parquetFile")
    sales_daily = spark.sql("select date_trunc(\"day\", created_at), sum(extended_gmv) from parquetFile group by 1 order by 1")
    sales_daily.write.csv("output/sales_daily")

    spark.stop()
