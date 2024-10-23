# Design Patterns in Object-Oriented Programming (OOP)
- [Design Patterns in Object-Oriented Programming (OOP)](#design-patterns-in-object-oriented-programming-oop)
  - [1. **Introduction to Design Patterns**](#1-introduction-to-design-patterns)
  - [2. **Creational Design Patterns**](#2-creational-design-patterns)
  - [3. **Structural Design Patterns**](#3-structural-design-patterns)
  - [4. **Behavioral Design Patterns**](#4-behavioral-design-patterns)
  - [5. **Principles Related to Design Patterns**](#5-principles-related-to-design-patterns)
  - [6. **Anti-Patterns**](#6-anti-patterns)
  - [7. **Best Practices for Applying Design Patterns**](#7-best-practices-for-applying-design-patterns)
  - [8. **Real-World Applications of Design Patterns**](#8-real-world-applications-of-design-patterns)
  - [9. **Conclusion**](#9-conclusion)
  - [10. **Common Interview Questions on Design Patterns**](#10-common-interview-questions-on-design-patterns)
    - [1. **What are design patterns, and why are they important in software development?**](#1-what-are-design-patterns-and-why-are-they-important-in-software-development)
    - [2. **Can you explain the difference between a Factory Method and an Abstract Factory?**](#2-can-you-explain-the-difference-between-a-factory-method-and-an-abstract-factory)
    - [3. **What is the Singleton pattern, and when would you use it?**](#3-what-is-the-singleton-pattern-and-when-would-you-use-it)
    - [4. **How does the Strategy pattern differ from the State pattern?**](#4-how-does-the-strategy-pattern-differ-from-the-state-pattern)
    - [5. **What is the difference between composition and inheritance, and how does the Composite pattern leverage this?**](#5-what-is-the-difference-between-composition-and-inheritance-and-how-does-the-composite-pattern-leverage-this)
    - [6. **Explain the difference between the Adapter pattern and the Facade pattern.**](#6-explain-the-difference-between-the-adapter-pattern-and-the-facade-pattern)
    - [7. **What is the Observer pattern, and how does it relate to the Publish/Subscribe model?**](#7-what-is-the-observer-pattern-and-how-does-it-relate-to-the-publishsubscribe-model)
    - [8. **How does the Decorator pattern differ from the Proxy pattern?**](#8-how-does-the-decorator-pattern-differ-from-the-proxy-pattern)
    - [9. **What are the SOLID principles, and how do they relate to design patterns?**](#9-what-are-the-solid-principles-and-how-do-they-relate-to-design-patterns)
    - [10. **Can you provide a real-world example where you have applied a design pattern?**](#10-can-you-provide-a-real-world-example-where-you-have-applied-a-design-pattern)


For more detail explanations and examples go to https://refactoring.guru/design-patterns

## 1. **Introduction to Design Patterns**
   - **Definition and Importance**: Understanding what design patterns are, their role in solving common design problems, and their place in OOP.
   - **Types of Design Patterns**: 
     - Creational
     - Structural
     - Behavioral
   - **Key Benefits**: Reusability, maintainability, and scalability.

## 2. **Creational Design Patterns**
   - **Overview**: Focus on how objects are created to ensure flexibility and reuse of code.
   - **Key Patterns**:
     - **Singleton**: Ensures a class has only one instance and provides a global point of access to it.
     - **Factory Method**: Defines an interface for creating objects but lets subclasses alter the type of objects that will be created.
     - **Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
     - **Builder**: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.
     - **Prototype**: Creates new objects by copying an existing object, known as the prototype.

## 3. **Structural Design Patterns**
   - **Overview**: Deal with object composition and typically define relationships between classes or objects.
   - **Key Patterns**:
     - **Adapter**: Allows incompatible interfaces to work together by providing a wrapper that translates requests.
     - **Bridge**: Decouples an abstraction from its implementation so that the two can vary independently.
     - **Composite**: Composes objects into tree structures to represent part-whole hierarchies, allowing clients to treat individual objects and compositions of objects uniformly.
     - **Decorator**: Adds behavior or responsibilities to objects dynamically without modifying their code.
     - **Facade**: Provides a simplified interface to a complex subsystem.
     - **Flyweight**: Reduces the cost of creating and manipulating a large number of similar objects by sharing them.
     - **Proxy**: Provides a placeholder or surrogate for another object to control access to it.

## 4. **Behavioral Design Patterns**
   - **Overview**: Concerned with communication between objects and responsibilities of objects.
   - **Key Patterns**:
     - **Chain of Responsibility**: Passes a request along a chain of handlers, where each handler can either process the request or pass it on to the next handler in the chain.
     - **Command**: Encapsulates a request as an object, thereby allowing users to parameterize clients with different requests, queue requests, and support undoable operations.
     - **Interpreter**: Implements an expression interface to interpret a language, defining a grammatical representation for a language and providing an interpreter to deal with this grammar.
     - **Iterator**: Provides a way to access elements of a collection sequentially without exposing its underlying representation.
     - **Mediator**: Centralizes complex communication and control logic between related objects.
     - **Memento**: Captures and restores an object’s internal state without violating encapsulation.
     - **Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
     - **State**: Allows an object to alter its behavior when its internal state changes, appearing as if the object has changed its class.
     - **Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
     - **Template Method**: Defines the skeleton of an algorithm, deferring some steps to subclasses without changing the algorithm’s structure.
     - **Visitor**: Represents an operation to be performed on elements of an object structure without changing the classes on which it operates.

## 5. **Principles Related to Design Patterns**
   - **SOLID Principles**:
     - **Single Responsibility Principle (SRP)**: A class should have only one reason to change, meaning it should have only one job.
     - **Open/Closed Principle (OCP)**: Software entities should be open for extension, but closed for modification.
     - **Liskov Substitution Principle (LSP)**: Subtypes should be substitutable for their base types without altering the correctness of the program.
     - **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they do not use.
     - **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules, both should depend on abstractions.

## 6. **Anti-Patterns**
   - **Definition**: Common responses to recurring problems that are ineffective and counterproductive.
   - **Examples**:
     - God Object
     - Spaghetti Code
     - Lava Flow
     - Big Ball of Mud

## 7. **Best Practices for Applying Design Patterns**
   - **Choosing the Right Pattern**: Patterns should be applied to specific problems, not force-fit into every design.
   - **Pattern Overuse**: Recognizing when not to use design patterns and avoiding pattern obsession.
   - **Refactoring**: Using design patterns as a tool to improve existing code.

## 8. **Real-World Applications of Design Patterns**
   - **Case Studies**: Examples of how design patterns are applied in real-world applications such as web development, mobile apps, game development, and enterprise systems.
   - **Design Patterns in Frameworks**: How modern frameworks (e.g., Spring, Django, React) utilize design patterns under the hood.

## 9. **Conclusion**
   - **Importance of Design Patterns**: Summarizing how design patterns can enhance the design, flexibility, and maintainability of OOP-based systems.
   - **Further Reading & Practice**: Recommended books (e.g., "Design Patterns: Elements of Reusable Object-Oriented Software") and practice exercises.

## 10. **Common Interview Questions on Design Patterns**

### 1. **What are design patterns, and why are they important in software development?**
   **Answer**: 
   Design patterns are typical solutions to common problems in software design. They are blueprints that can be customized to solve specific design issues. They help in creating more flexible, reusable, and maintainable code. Using design patterns also improves communication between developers since they provide a shared vocabulary for solutions.

### 2. **Can you explain the difference between a Factory Method and an Abstract Factory?**
   **Answer**: 
   The **Factory Method** pattern allows subclasses to decide which class to instantiate. It's focused on the creation of a single product. The **Abstract Factory** pattern, on the other hand, provides an interface to create families of related or dependent objects without specifying their concrete classes. The Abstract Factory is used when multiple products are needed, but the exact type isn't known until runtime.

### 3. **What is the Singleton pattern, and when would you use it?**
   **Answer**: 
   The **Singleton** pattern ensures that a class has only one instance and provides a global point of access to that instance. It's commonly used when exactly one object is needed to coordinate actions across the system, such as in logging, database connection pooling, or configuration settings.

### 4. **How does the Strategy pattern differ from the State pattern?**
   **Answer**: 
   Both patterns allow behavior to be changed at runtime, but the **Strategy** pattern is used when you want to switch between interchangeable algorithms or behaviors dynamically. The **State** pattern is used to alter the behavior of an object when its internal state changes. The key difference is that **Strategy** focuses on choosing an algorithm, while **State** deals with changing the object's behavior as it transitions between different states.

### 5. **What is the difference between composition and inheritance, and how does the Composite pattern leverage this?**
   **Answer**: 
   **Inheritance** is a mechanism to extend existing functionality by creating a subclass. **Composition**, on the other hand, is the practice of building complex objects by combining simpler objects. The **Composite** pattern leverages composition by structuring objects into tree hierarchies where individual objects and compositions (composed of many objects) are treated uniformly. This pattern is often used for building structures like file systems or UI components.

### 6. **Explain the difference between the Adapter pattern and the Facade pattern.**
   **Answer**: 
   The **Adapter** pattern is used to convert an interface of a class into another interface the client expects. It allows classes with incompatible interfaces to work together. The **Facade** pattern, on the other hand, provides a simplified interface to a complex system, making it easier to use but without altering the subsystem itself. In short, Adapter is for compatibility between interfaces, while Facade is for simplifying a complex system.

### 7. **What is the Observer pattern, and how does it relate to the Publish/Subscribe model?**
   **Answer**: 
   The **Observer** pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents (observers) are notified and updated automatically. This is similar to the **Publish/Subscribe** model, where publishers broadcast messages to multiple subscribers without knowing who they are, and subscribers automatically receive updates. The Observer pattern is often used in GUIs and event-driven systems.

### 8. **How does the Decorator pattern differ from the Proxy pattern?**
   **Answer**: 
   The **Decorator** pattern adds behavior or functionality to an object dynamically, without altering its structure. It is used to wrap objects to extend their functionality. The **Proxy** pattern provides a surrogate or placeholder for another object to control access to it, like adding security, lazy initialization, or logging. While both patterns wrap objects, Decorator focuses on adding features, and Proxy focuses on controlling access.

### 9. **What are the SOLID principles, and how do they relate to design patterns?**
   **Answer**: 
   The **SOLID** principles are a set of guidelines for designing flexible, maintainable, and scalable object-oriented systems:
   - **S**ingle Responsibility: A class should have only one reason to change.
   - **O**pen/Closed: Classes should be open for extension but closed for modification.
   - **L**iskov Substitution: Subtypes must be replaceable for their base types without affecting the correctness of the program.
   - **I**nterface Segregation: Clients should not be forced to depend on interfaces they do not use.
   - **D**ependency Inversion: High-level modules should depend on abstractions, not on low-level modules.

   Many design patterns adhere to SOLID principles. For example, the **Factory Method** and **Abstract Factory** patterns support the Open/Closed Principle by allowing easy extension of product creation without modifying existing code.

### 10. **Can you provide a real-world example where you have applied a design pattern?**
   **Answer**: 
   One common example is using the **Singleton** pattern to manage database connections in a web application. Since opening multiple database connections can be resource-intensive, ensuring there is only one connection instance shared across the application saves resources and prevents issues like overloading the database server. Another example is using the **Strategy** pattern in a payment processing system where different payment methods (credit card, PayPal, etc.) can be selected dynamically at runtime.