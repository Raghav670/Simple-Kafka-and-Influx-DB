from kafka import KafkaConsumer
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Replace placeholders with actual credentials
topic_name = 'influx'
consumer = KafkaConsumer(topic_name)

bucket = "test_bucket"
org = "ltd"
token = "G3CnQH7SK96QlX9esqSi1p-0h26KtTbwecV0DMFYbA4ZviGTOohdQUZ7D08TpATvDQJsQDA7ke4uFkKoTISK8g=="
url = "http://localhost:8086"
client = InfluxDBClient(url=url, token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

try:
    for message in consumer:
        point = Point("kafka_data").field("message", message.value.decode('utf-8'))
        write_api.write(bucket, org, point)
        print(f"Message written to InfluxDB: {message.value.decode('utf-8')}")

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()
