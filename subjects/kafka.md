# Apache Kafka

- [Apache Kafka](#apache-kafka)
- [1. Writing messages to Kafka](#1-writing-messages-to-kafka)
  - [1.1. Producers](#11-producers)
  - [1.2. Topics](#12-topics)
  - [1.3. Partitions](#13-partitions)
  - [1.4. Replication](#14-replication)
- [2. Reading Data from Kafka](#2-reading-data-from-kafka)
  - [2.1. Consumers](#21-consumers)
  - [2.2. Consumer groups](#22-consumer-groups)
  - [2.3. Offsets](#23-offsets)
  - [2.4. Heartbeat](#24-heartbeat)
- [3. Kafka Internals](#3-kafka-internals)
  - [3.1. Broker](#31-broker)
  - [3.2. Zookeeper](#32-zookeeper)
  - [3.3. Log](#33-log)
  - [3.4. Replication](#34-replication)
- [4. Reliable Data Delivery](#4-reliable-data-delivery)
  - [4.1. Exactly-once semantics](#41-exactly-once-semantics)
  - [4.2. At-least-once semantics](#42-at-least-once-semantics)
  - [4.3. At-most-once semantics](#43-at-most-once-semantics)
- [5. Building Data pipelines](#5-building-data-pipelines)
  - [5.1. Kafka Connect](#51-kafka-connect)
  - [5.2. Kafka Streams](#52-kafka-streams)
- [6. Monitoring Kafka](#6-monitoring-kafka)
  - [6.1. JMX](#61-jmx)
  - [6.2. Prometheus](#62-prometheus)
  - [6.3. Grafana](#63-grafana)
- [7. Streaming Processing](#7-streaming-processing)
  - [7.1. Apache Spark](#71-apache-spark)
  - [7.2. Apache Flink](#72-apache-flink)
  - [7.3. Amazon Kinesis](#73-amazon-kinesis)

# 1. Writing messages to Kafka

## 1.1. Producers
- Write messages to Kafka topics.
- Can be configured to use a variety of serialization formats.

## 1.2. Topics
- A logical grouping of messages.
- Can be partitioned to improve scalability.

## 1.3. Partitions
- A physical division of a topic.
- Messages are distributed across partitions based on a hash of their key.

## 1.4. Replication
- Each partition is replicated to a number of brokers.
- This ensures that messages are not lost if a broker fails.

# 2. Reading Data from Kafka

## 2.1. Consumers
- Read messages from Kafka topics.
- Can be configured to use a variety of consumer groups.

## 2.2. Consumer groups
- A group of consumers that read from the same topic.
- Messages are distributed across consumers in the group.

## 2.3. Offsets
- The position in a partition where a consumer is reading from.
- Offsets are maintained by Kafka and are used to resume reading from where a consumer left off.

## 2.4. Heartbeat
- A periodic message that consumers send to Kafka to indicate that they are still alive.
- If a consumer fails to send a heartbeat, Kafka will mark it as dead and stop sending it messages.

# 3. Kafka Internals

## 3.1. Broker
- A server that runs Kafka.
- Brokers are responsible for storing messages, replicating them to other brokers, and serving them to consumers.

## 3.2. Zookeeper
- A distributed coordination service that Kafka uses to store metadata about its topics, brokers, and consumers.

## 3.3. Log
- A circular log that stores messages.
- Messages are appended to the log in a append-only fashion.

## 3.4. Replication
- Each partition is replicated to a number of brokers.
- This ensures that messages are not lost if a broker fails.

# 4. Reliable Data Delivery

## 4.1. Exactly-once semantics
- Guarantees that messages are delivered exactly once.
- This is the most reliable delivery semantics, but it can be the most expensive.

## 4.2. At-least-once semantics
- Guarantees that messages are delivered at least once.
- This is a less expensive delivery semantics than exactly-once, but it can result in duplicate messages.

## 4.3. At-most-once semantics
- Guarantees that messages are delivered at most once.
- This is the least expensive delivery semantics, but it can result in lost messages.

# 5. Building Data pipelines

## 5.1. Kafka Connect
- A framework for building and managing data pipelines that connect Kafka to other data sources and sinks.

## 5.2. Kafka Streams
- A library for building real-time streaming applications that process data from Kafka.

# 6. Monitoring Kafka

## 6.1. JMX
- A Java Management Extensions (JMX) console that can be used to monitor Kafka brokers.

## 6.2. Prometheus
- An open-source monitoring system that can be used to collect metrics from Kafka brokers.

## 6.3. Grafana
- A visualization tool that can be used to display metrics collected by Prometheus.

# 7. Streaming Processing

## 7.1. Apache Spark
- A distributed processing framework that can be used to process streaming data from Kafka.

## 7.2. Apache Flink
- A distributed processing framework that can be used to process streaming data from Kafka.

## 7.3. Amazon Kinesis
- A fully-managed service that can be used to process streaming data from Kafka.
