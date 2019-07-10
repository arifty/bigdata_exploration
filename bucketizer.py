from pyspark.ml.feature import Bucketizer

splits = range(0, 27558) 

df_result2_bucketed = Bucketizer(splits=splits, inputCol="amt_turnover", outputCol="panier") \ 
    .transform(df_ticket1) df_result2_bucketed.groupBy("panier") \ 
    .agg(min("amt_turnover").alias("from_CA"),max("amt_turnover").alias("to_CA")) \ 
    .orderBy(col("panier").desc()).show()