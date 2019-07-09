import sys
from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: csv2parquet csvfile", file=sys.stderr)
        sys.exit(-1)
    
    spark = SparkSession\
        .builder\
        .appName("csv2parquet")\
        .getOrCreate()

    spark.read.csv(sys.argv[1], header="true").write.parquet("output/sales.parquet")

    spark.stop()
