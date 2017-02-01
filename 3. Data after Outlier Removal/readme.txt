Here we try fo find only strong data. so we take threshold as 5. It means, in 15 days period if a road segment has atleast 5 records for specific time we take it otherwise remove the data.
For better data set. We use 2 standard deviation fo the mean as finding outlier. we calculate arithmetic mean and standard deviation(30 mins interval for 15 days) then remove the data considered as outlier
1. 'Data after threshold and outlier' contains some files after threshold setting and outlier removal.
2. 'Threshold Outlier removal.py' contains the source code for that job.