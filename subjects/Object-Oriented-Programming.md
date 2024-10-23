# Object-Oriented Programming (OOP)

## 1. Definition
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data in the form of fields (attributes) and code in the form of methods (functions). OOP is centered around the idea of structuring programs so that data and operations are encapsulated within these objects, promoting code organization and reuse.

## 2. Core Principles (Pillars)
The four core principles of OOP form the foundation for creating flexible, reusable, and maintainable software designs:

- **Encapsulation**:
  - **Definition**: Encapsulation is the mechanism of restricting direct access to some of an object's components, which means that the object's internal state can only be modified through a controlled interface (usually via methods). This hides the implementation details and protects the integrity of the object's state.
  - **Example**: Using `private` fields and providing `public` getter and setter methods to access and modify the data.
  
- **Abstraction**: 
  - **Definition**: Abstraction is the process of hiding the complex implementation details and exposing only the essential features of an object. It allows you to focus on what an object does rather than how it does it.
  - **Example**: Defining abstract methods in abstract classes or interfaces, allowing subclasses to provide specific implementations.

- **Inheritance**: 
  - **Definition**: Inheritance allows a class (child or subclass) to inherit properties and behavior (fields and methods) from another class (parent or superclass). This promotes code reuse and establishes a relationship between classes.
  - **Example**: A `Dog` class can inherit from a `Animal` class and share its characteristics.

- **Polymorphism**: 
  - **Definition**: Polymorphism allows objects to be treated as instances of their parent class. It enables one interface to be used for a general class of actions, allowing behavior to vary depending on the actual object (dynamic method dispatch).
  - **Example**: A method like `draw()` might work differently for a `Circle`, `Rectangle`, or `Triangle` but is called in the same way.

## 3. Benefits of OOP
- **Code Reusability**: 
  - OOP encourages the reuse of existing classes and objects, reducing redundancy and duplication of code. For example, through inheritance, a subclass can reuse methods and attributes from a parent class.
  
- **Scalability**: 
  - OOP designs are easier to extend and scale by adding new classes, methods, or properties without modifying existing code. This is essential when developing large-scale applications.
  
- **Maintainability**: 
  - With encapsulation, changes in one part of the application (like an object's internal workings) don’t affect the rest of the system, making it easier to manage and maintain over time.
  
- **Ease of Debugging**: 
  - Since objects represent real-world entities, it’s easier to conceptualize and debug software systems. Well-encapsulated objects with clearly defined behavior lead to better modularity and isolation of errors.

## 4. Classes and Objects
- **Class Definition**: 
  - A class is a blueprint for creating objects. It defines the attributes (fields) and behaviors (methods) that the objects instantiated from the class will have. For example, a `Car` class might have fields like `color`, `make`, `model`, and methods like `startEngine()`, `drive()`.
  
- **Object Creation**: 
  - Objects are instances of a class and are created using the `new` keyword in Java. For example, `Car myCar = new Car();` creates an instance of the `Car` class.
  
- **State and Behavior**: 
  - The state of an object is represented by its fields (e.g., the `color` of a `Car`), and its behavior is represented by its methods (e.g., `drive()`).
  
- **Constructors**: 
  - Constructors are special methods used to initialize objects. There are two types:
    - **Default Constructor**: A constructor with no parameters.
    - **Parameterized Constructor**: A constructor with parameters to initialize object attributes when the object is created.

## 5. Common Interview Questions

1. **What are the differences between an abstract class and an interface?**
   - Abstract classes can have both concrete methods and abstract methods (methods without a body), while interfaces only declare method signatures by default (before Java 8) and require classes to implement those methods. After Java 8, interfaces can have default and static methods.
   - A class can inherit only one abstract class, but it can implement multiple interfaces.

2. **What is method overloading and method overriding?**
   - **Method Overloading**: Involves having multiple methods in the same class with the same name but different parameter lists (compile-time polymorphism).
   - **Method Overriding**: A subclass provides a specific implementation of a method that is already defined in its superclass (runtime polymorphism).

3. **Explain the `final` keyword in Java.**
   - The `final` keyword can be used with variables, methods, and classes:
     - **final variable**: A variable's value cannot be changed once initialized.
     - **final method**: A method cannot be overridden by subclasses.
     - **final class**: A class cannot be subclassed.

4. **What is the difference between shallow copy and deep copy?**
   - **Shallow Copy**: A copy of the object is made, but the references to objects inside it are not copied. The original and the copied object share the same inner objects.
   - **Deep Copy**: Not only the object is copied, but also all objects it references, creating independent copies.

5. **What is the use of the `super` keyword in Java?**
   - The `super` keyword is used to refer to the parent class's members (variables, methods, constructors). It is often used to call the superclass's constructor or to access methods/fields of the parent class that are hidden by the subclass.

6. **What is the difference between composition and inheritance?**
   - **Inheritance**: Represents an "is-a" relationship. For example, `Dog` is a subclass of `Animal`, meaning `Dog` is an `Animal`.
   - **Composition**: Represents a "has-a" relationship. For example, a `Car` has an `Engine`. Composition is often preferred over inheritance for code reuse when the relationship between classes is not an "is-a" relationship.

7. **Explain garbage collection in Java.**
   - Java provides automatic memory management with garbage collection. The Garbage Collector (GC) identifies and removes objects that are no longer in use, freeing memory for new objects. This helps prevent memory leaks and ensures efficient memory utilization.
  
8. **What is the difference between `==` and `equals()` in Java?**
   - **`==`**: This is the reference comparison operator, checking whether two references point to the same object in memory.
   - **`equals()`**: This method is used to compare the contents (or state) of two objects, typically overridden to define how two objects should be compared for equality.

9. **What is the significance of the `static` keyword?**
   - The `static` keyword in Java is used to define class-level methods and variables. Static members belong to the class rather than any specific instance of the class. This means you can access a static method or variable without creating an object of the class (e.g., `ClassName.staticMethod()`).

10. **What are access modifiers, and why are they important?**
    - **Private**: Members are accessible only within the class they are defined.
    - **Default** (no modifier): Members are accessible within the same package.
    - **Protected**: Members are accessible within the same package or by subclasses in different packages.
    - **Public**: Members are accessible from any class.
    - They are important because they define the level of access control and encapsulation for class members.