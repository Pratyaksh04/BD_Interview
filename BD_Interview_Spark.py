from pyspark.sql import SparkSession # type: ignore
from pyspark.sql import functions as f # type: ignore

spark = SparkSession.builder \
    .appName("ReadParquet") \
    .config("spark.sql.parquet.int96RebaseModeInRead", "CORRECTED") \
    .config("spark.sql.parquet.datetimeRebaseModeInRead", "CORRECTED") \
    .config("spark.sql.legacy.parquet.nanosAsLong", "true") \
    .getOrCreate()


#





base_path = ("D:\OneDrive\Desktop\BD Group Interview\MS_Contoso_Sample_Data_Set_Parquet")
sales = spark.read.parquet(f"{base_path}\Sales.parquet")

calendar = spark.read.parquet(f"{base_path}\Calendar.parquet")

channel = spark.read.parquet(f"{base_path}\Channel.parquet")

stores = spark.read.parquet(f"{base_path}\Stores.parquet")

geo = spark.read.parquet(f"{base_path}\Geography.parquet")

product = spark.read.parquet(f"{base_path}\Product.parquet")

prod_sub = spark.read.parquet(f"{base_path}\ProductSubcategory.parquet")

prod_cat = spark.read.parquet(f"{base_path}\ProductCategory.parquet")

promo = spark.read.parquet(f"{base_path}\Promotion.parquet")

#Chnges in personalDev

sales.printSchema()

ifnull("column_name","Values")
nullif("","Unknown")


clean_sales
