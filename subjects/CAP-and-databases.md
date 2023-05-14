# CAP Theorem and Databases
Source: https://www.ibm.com/topics/cap-theorem

- [CAP Theorem and Databases](#cap-theorem-and-databases)
- [1. What is CAP Theorem?](#1-what-is-cap-theorem)
- [2. NoSQL Databases](#2-nosql-databases)
- [3. MongoDB](#3-mongodb)
- [4. Apache Cassandra](#4-apache-cassandra)
- [5. Microservices](#5-microservices)


# 1. What is CAP Theorem?

The CAP theorem, also known as Brewer's theorem, is a theorem in computer science that states that it is impossible for a distributed computer system to simultaneously provide the following guarantees:

* **Consistency:** Every read operation returns the most recent write operation that was performed on a given data item.
* **Availability:** Every request received by the system must be eventually responded to, even if it means returning an error.
* **Partition tolerance:** The system continues to operate even if some of the nodes fail.
 
# 2. NoSQL Databases
 NoSQL databases are classified into three types based on the CAP theorem:

* **CP databases:** : Consistency and partition tolerance at the expense of availability.

* **AP databases:**: Availability and partition tolerance at the expense of consistency.

* **CA databases:**: Consistency and availability across all nodes, but can't deliver fault tolerance.

In practice, CA databases don't exist because partitions can't be avoided in distributed systems.

# 3. MongoDB

- MongoDB is a CP database that stores data as BSON documents. It uses a single-master replication model to maintain consistency across the network.
- When the primary node (master) becomes unavailable, the secondary node with the most recent operation log will be elected as the new primary node.
This ensures that the data remains consistent across the entire network, even in the event of a network partition.

# 4. Apache Cassandra

- Apache Cassandra is an AP database that stores data on a distributed network. 
- It has a masterless architecture, which means that all nodes are equal and there is no single point of failure. 
- Cassandra provides eventual consistency, which means that data may be inconsistent for a short period of time after it is written. However, Cassandra quickly reconciles inconsistencies, making it a highly performant database.
- Cassandra is a good choice for applications that need to be highly available, such as social media platforms and e-commerce websites. It is also a good choice for applications that need to be able to handle large amounts of data, such as big data analytics and machine learning.

# 5. Microservices

Microservices can have their own databases. Choose a database according to your needs:

* **Consistency most important:** Choose a CP database like PostgreSQL.
* **Availability most important:** Choose an AP database like Cassandra or Apache CouchDB.
 