# Pattern of enterprise application architectures

- [Pattern of enterprise application architectures](#pattern-of-enterprise-application-architectures)
- [1. Concurrency](#1-concurrency)
  - [1.1. Concurrency Problems](#11-concurrency-problems)
  - [1.2. Execution Context](#12-execution-context)
  - [1.3. Optimistic and Pessimistic Concurrency Control](#13-optimistic-and-pessimistic-concurrency-control)
  - [1.4. Transactions](#14-transactions)
- [2. Session State](#2-session-state)
- [3. Domain Logic Patterns](#3-domain-logic-patterns)
  - [3.1. Transaction Script](#31-transaction-script)
  - [3.2. Domain Model](#32-domain-model)
  - [3.3. Service Layer](#33-service-layer)
- [4. Data Source Architectural Patterns](#4-data-source-architectural-patterns)
  - [4.1. Active Record](#41-active-record)
  - [4.2. Data Mapper](#42-data-mapper)
- [5. Object-Relational Behavioral Patterns](#5-object-relational-behavioral-patterns)
  - [5.1. Unit of Work](#51-unit-of-work)
  - [5.2. Identity Map](#52-identity-map)
  - [5.3. Lazy Load](#53-lazy-load)
- [6. Object-Relational Structural Patterns](#6-object-relational-structural-patterns)
  - [6.1. Identity Field](#61-identity-field)
  - [6.2. Foreign Key Mapping](#62-foreign-key-mapping)
  - [6.3. Dependent Mapping](#63-dependent-mapping)
  - [6.4. Single Table Inheritance](#64-single-table-inheritance)
  - [6.5. Class Table Inheritance](#65-class-table-inheritance)
  - [6.6. Concrete Table Inheritance](#66-concrete-table-inheritance)
  - [6.7. Inheritance Mappers](#67-inheritance-mappers)
- [7. Object-Relational Metadata Mapping Patterns](#7-object-relational-metadata-mapping-patterns)
  - [7.1. Metadata Mapping](#71-metadata-mapping)
  - [7.2. QueryObject](#72-queryobject)
  - [7.3. Repository](#73-repository)
- [8. Web Presentation Patterns](#8-web-presentation-patterns)
  - [8.1. Model View Controller](#81-model-view-controller)
  - [8.2. Page Controller](#82-page-controller)
  - [8.3. Template View](#83-template-view)
  - [8.4. Application Controller](#84-application-controller)
- [9. Distribution Patterns](#9-distribution-patterns)
  - [9.1. Remote Facade](#91-remote-facade)
  - [9.2. Data Transfer Object](#92-data-transfer-object)
- [10. Offline Concurrency Patterns](#10-offline-concurrency-patterns)
  - [10.1. Optimistic Offline lock](#101-optimistic-offline-lock)
  - [10.2. Pessimistic Offline Lock](#102-pessimistic-offline-lock)
  - [10.3. Implicit Lock](#103-implicit-lock)
- [11. Session State Patterns](#11-session-state-patterns)
  - [11.1. Client Session State](#111-client-session-state)
  - [11.2. Server Session State](#112-server-session-state)
  - [11.3. Database Session State](#113-database-session-state)
- [12. Base Patterns](#12-base-patterns)
  - [12.1. Gateway](#121-gateway)
  - [12.2. Mapper](#122-mapper)
  - [12.3. Registry](#123-registry)



# 1. Concurrency
## 1.1. Concurrency Problems
  * Data corruption
  * Deadlocks
  * Livelocks
  * Lost updates
## 1.2. Execution Context
  * Thread
  * Process
  * Transaction
## 1.3. Optimistic and Pessimistic Concurrency Control
  * Optimistic concurrency control
  * Pessimistic concurrency control
## 1.4. Transactions
  * ACID
  * Isolation
  * Consistency
  * Durability

# 2. Session State
  * In-memory
  * Stateless
  * Stateful

# 3. Domain Logic Patterns

## 3.1. Transaction Script
  * How it works
    * Encapsulates all the logic for a single transaction
    * Provides a clear boundary between the UI and the domain logic
  * When to use it
    * When the domain logic is complex and needs to be encapsulated

## 3.2. Domain Model
  * How it works
    * Represents the domain of the application
    * Provides a common vocabulary for the application
  * When to use it
    * When the application needs to model a real-world domain

## 3.3. Service Layer
  * How it works
    * Provides a layer of abstraction between the UI and the domain logic
    * Makes the domain logic more reusable
  * When to use it
    * When the domain logic is complex or needs to be reused

# 4. Data Source Architectural Patterns

## 4.1. Active Record
  * How it works
    * Provides a direct mapping between database tables and objects
    * Makes it easy to access data from the database
  * When to use it
    * When the application needs to access data from the database directly

## 4.2. Data Mapper
  * How it works
    * Isolates the application from the database
    * Makes it easier to change the database
  * When to use it
    * When the application needs to be able to change the database

# 5. Object-Relational Behavioral Patterns
## 5.1. Unit of Work
  * How it works
    * Encapsulates all the logic for a single database transaction
    * Provides a way to roll back changes if a transaction fails
  * When to use it
    * When the application needs to perform multiple database operations as a single unit
## 5.2. Identity Map
  * How it works
    * Tracks objects that have been loaded from the database
    * Prevents the application from loading the same object multiple times
  * When to use it
    * When the application needs to load the same object multiple times
## 5.3. Lazy Load
  * How it works
    * Delays the loading of an object until it is actually needed
    * Improves performance by only loading objects that are needed
  * When to use it
    * When the application only needs to load a subset of objects

# 6. Object-Relational Structural Patterns

## 6.1. Identity Field
  * How it works
    * Provides a unique identifier for each object in the database
  * When to use it
    * When the application needs to be able to uniquely identify objects in the database

## 6.2. Foreign Key Mapping
  * How it works
    * Creates a relationship between two tables in the database
  * When to use it
    * When the application needs to relate two objects in the database

## 6.3. Dependent Mapping
  * How it works
    * Creates a relationship between a parent object and a child object in the database
  * When to use it
    * When the application needs to relate a parent object to a child object in the database

## 6.4. Single Table Inheritance
  * How it works
    * Stores all the data for a hierarchy of objects in a single table
  * When to use it
    * When the application needs to store a hierarchy of objects in the database

## 6.5. Class Table Inheritance
  * How it works
    * Stores each class in a separate table in the database
  * When to use it
    * When the application needs to store a hierarchy of objects in the database and needs to be able to access each class separately

## 6.6. Concrete Table Inheritance
  * How it works
    * Stores each class in a separate table in the database and stores a discriminator column to indicate which class each row belongs to
  * When to use it
    * When the application needs to store a hierarchy of objects in the database and needs to be able to access each class separately

## 6.7. Inheritance Mappers
  * How it works
    * Automatically maps objects to tables in the database based on their inheritance hierarchy
  * When to use it
    * When the application needs to store a hierarchy of objects in the database and needs to be able to access each class separately


# 7. Object-Relational Metadata Mapping Patterns

## 7.1. Metadata Mapping
  * How it works
    * Maps database metadata to object-oriented metadata
    * Provides a way to access database data from objects
  * When to use it
    * When the application needs to access database data from objects
## 7.2. QueryObject
  * How it works
    * Encapsulates database queries
    * Provides a way to execute queries without having to know the database schema
  * When to use it
    * When the application needs to execute database queries without having to know the database schema
## 7.3. Repository
  * How it works
    * Provides a layer of abstraction between the application and the database
    * Makes it easier to change the database without affecting the application
  * When to use it
    * When the application needs to be able to change the database without affecting the application

# 8. Web Presentation Patterns
## 8.1. Model View Controller
  * How it works
    * Separates the presentation of data from the logic of the application
    * Makes it easier to change the presentation of data without affecting the logic of the application
  * When to use it
    * When the application needs to be able to change the presentation of data without affecting the logic of the application
## 8.2. Page Controller 
  * How it works
    * Controls the flow of a web page
    * Makes it easier to create complex web pages
  * When to use it
    * When the application needs to create complex web pages
## 8.3. Template View
  * How it works
    * Provides a way to define the layout of a web page
    * Makes it easier to create consistent web pages
  * When to use it
    * When the application needs to create consistent web pages
## 8.4. Application Controller
  * How it works
    * Controls the flow of an application
    * Makes it easier to create complex applications
  * When to use it
    * When the application needs to create complex applications

# 9. Distribution Patterns
## 9.1. Remote Facade
  * How it works
    * Provides a way to access remote objects
    * Makes it easier to create distributed applications
  * When to use it
    * When the application needs to access remote objects
## 9.2. Data Transfer Object
  * How it works
    * Encapsulates data that is transferred between objects
    * Makes it easier to transfer data between objects
  * When to use it
    * When the application needs to transfer data between objects

# 10. Offline Concurrency Patterns
## 10.1. Optimistic Offline lock
  * How it works
    * Assumes that concurrent users will not modify the same data
    * Only locks data when it is actually modified
  * When to use it
    * When the application needs to be able to handle concurrent users
## 10.2. Pessimistic Offline Lock
  * How it works
    * Locks data as soon as it is accessed
    * Prevents concurrent users from modifying the same data
  * When to use it
    * When the application needs to prevent concurrent users from modifying the same data
## 10.3. Implicit Lock
  * How it works
    * Uses a database lock to prevent concurrent users from modifying the same data
    * The lock is released when the user finishes using the data
  * When to use it
    * When the application needs to prevent concurrent users from modifying the same data

# 11. Session State Patterns
## 11.1. Client Session State
  * How it works
    * Stores session state on the client
    * Makes it easier to create stateless servers
  * When to use it
    * When the application needs to create stateless servers
## 11.2. Server Session State
  * How it works
    * Stores session state on the server
    * Makes it easier to create stateful servers
  * When to use it
    * When the application needs to create stateful servers
## 11.3. Database Session State
  * How it works
    * Stores session state in the database
    * Makes it easier to create scalable servers
  * When to use it
    * When the application needs to create scalable servers

# 12. Base Patterns
## 12.1. Gateway
  * How it works
    * Provides a way to access a remote service
    * Makes it easier to create distributed applications
  * When to use it
    * When the application needs to access a remote service
## 12.2. Mapper
  * How it works
    * Maps data between different formats
    * Makes it easier to integrate different systems
  * When to use it
    * When the application needs to integrate different systems
## 12.3. Registry
  * How it works
    * Stores a list of objects
    * Makes it easier to find objects
    