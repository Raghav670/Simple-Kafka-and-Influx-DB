from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

kafka_topic = 'your_kafka_topic'
influx_bucket = "your_influx_bucket"
influx_org = "your_influx_org"
influx_token = "your_influx_token"
influx_url = "http://localhost:8086"

# Create Kafka consumer
consumer = KafkaConsumer(kafka_topic)

# Create InfluxDB client
client = InfluxDBClient(url=influx_url, token=influx_token)
write_api = client.write_api(write_options=SYNCHRONOUS)

try:
    for message in consumer:
        point = Point("kafka_data").field("message", message.value.decode('utf-8'))
        write_api.write(influx_bucket, influx_org, point)
        print(f"Message written to InfluxDB: {message.value.decode('utf-8')}")

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()
