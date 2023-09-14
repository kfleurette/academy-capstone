##Step 1: Containerize
FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1
COPY . .
USER root
RUN pip install --upgrade pip && pip install pyspark==3.1.2
CMD ["python3", "weather_capstone.py"]
