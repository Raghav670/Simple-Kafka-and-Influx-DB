# Simple standalone Kafka and Influx DB

## **DIAGRAM**
![Connecting kafka and influxdb ](https://github.com/Raghav670/Simple-Kafka-and-Influx-DB/assets/74827764/3258042b-5daf-4c57-9bac-bf09e24bc954)

## **OVERVIEW**

This project combines Kafka and InfluxDB to capture and save data from a Kafka topic to InfluxDB. It starts by configuring Zookeeper and Kafka for handling message streams. Then, it installs and sets up InfluxDB as the database. Finally, a Python script is used to read messages from Kafka and store them in InfluxDB.

# STEPS

## Step 1: Zookeeper Setup
Download and start Zookeeper in Ubuntu. Verify the QuorumPeer is running using jps.

### TO DOWNLOAD:
```rb
wget https://www.apache.org/dyn/closer.lua/zookeeper/<LATEST-ZOOKEEPER-VERSION>
```

### TO START ZOOKEEPER
```rb
/path/to/zookeeper/bin/zkServer.sh start
```

## Step 2: Kafka Setup
Download and start Kafka server. Create a topic, and use it to create a producer and consumer.

### TO DOWNLOAD [BINARY FILE]
```rb
wget https://downloads.apache.org/kafka/<LATEST-VERSION>/<FILE>.tgz
```

## Step 3: InfluxDB Installation and Configuration
Install and configure InfluxDB by downloading the package and installing it using dpkg.

```rb
curl -O https://dl.influxdata.com/influxdb/releases/influxdb2_2.7.4-1_amd64.deb
sudo dpkg -i influxdb2_2.7.4-1_amd64.deb
```

## Step 4: Start InfluxDB

- Start the InfluxDB service using the following command:
```rb
sudo service influxdb start
```
- Verify the status of InfluxDB:

```rb
sudo service influxdb status
```
- Connect to Inflex db WebUI

```rb
http://localhost:8086
```

- Selecting "Tokens" from the drop-down menu.
- Generating a new token with appropriate permissions.

## Step 5: Python Script for Data Integration

Write a Python script to consume messages from Kafka and write them to InfluxDB.

REFER: [Script.py](https://github.com/Raghav670/Simple-Kafka-and-Influx-DB/blob/adb3cffd93292729c3b6ab644c222e8fe9b8ce31/Script.py)







