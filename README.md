# Simple-Kafka-and-Influx-DB

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


