 # Angular Framework
 
- [Angular Framework](#angular-framework)
- [1. Modules](#1-modules)
- [2. Components](#2-components)
  - [2.1. Component Lifecycle](#21-component-lifecycle)
- [3. Sharing data between child and parent components](#3-sharing-data-between-child-and-parent-components)
- [4. Templates](#4-templates)
- [5. Directives](#5-directives)
- [6. Pipes](#6-pipes)
- [7. Optimization](#7-optimization)
- [8. Dependency Injection](#8-dependency-injection)
- [9. Reactive using Observable and RxJS](#9-reactive-using-observable-and-rxjs)
- [10. Routing](#10-routing)
- [11. Security](#11-security)
 

# 1. Modules

* A module is a collection of components, directives, pipes, and services that are used to build an Angular application. Modules are used to organize code and make it easier to manage.
* It can import other modules.
* **Common modules** include:
    * `BrowserModule`: Provides the basic functionality for Angular applications, such as the ability to create and manage components.
    * `FormsModule`: Provides the ability to create and manage forms in Angular applications.
    * `HttpModule`: Provides the ability to make HTTP requests in Angular applications.
* **Lazy loading**:
  * Improves perfomance.
  * Divides the public and private part of the application. This improves security.

# 2. Components

* A component is a reusable piece of code that can be used to create HTML elements. Components can be nested to create complex UIs.

## 2.1. Component Lifecycle
* An Angular component has a lifecycle that is triggered by events such as creation, destruction, and change detection.
* The lifecycle allows developers to control how a component behaves at different stages of its life. 
  * `ngOnChanges`: Called when the component's input properties change.
  * `ngOnInit`: 
    * Called when the component is initialized.
    * Usually to suscribe or pull data from external services.
  * `ngAfterViewInit`: Called after the component's view has been initialized.
  * `ngOnDestroy`: 
    * Called when the component is destroyed.
    * Usually to unsuscribe observables. This avoids memory leaks.

# 3. Sharing data between child and parent components

* There are a number of ways to share data between child and parent components:
    * **Input decorator:** The `@Input()` decorator can be used to inject data into a component from its parent.
    * **Output decorator:** The `@Output()` decorator can be used to emit data from a component to its parent.
    * **Service class:** A service class can be used to share data between components.
    * **Service with observable:** An observable can be used to share data between components in a reactive way.

# 4. Templates

* A template is a HTML file that is used to define the layout and behavior of an Angular component.
* Templates can be used to create dynamic HTML elements, bind data to HTML elements, and execute JavaScript code.

# 5. Directives

* A directive is a custom HTML attribute that can be used to add functionality to HTML elements.
* Directives can be used to change the appearance of an HTML element, bind data to an HTML element, or execute JavaScript code.
* Every angular component creates a new structural directive.  
* **Structural directives**
  * NgIf
    * Conditionally renders an element
  * NgForOf
    * Repeats an element for each item in an array
  * NgSwitch
    * Switches between different templates based on a value
  * NgContent
    * Injects content from a parent component into a child component
* **Attribute directives**
  * NgClass
    * Dynamically adds or removes CSS classes to an element
  * NgStyle
    * Dynamically sets the style properties of an element
  * NgModel
    * Binds an input element to a property in a component


# 6. Pipes

* A pipe is a function that can be used to transform data.
* Pipes can be used to format data, convert data types, and filter data.
* Angular includes:

  * **DatePipe:** The DatePipe can be used to format dates.
  * **UpperCasePipe:** The UpperCasePipe can be used to convert text to uppercase.
  * **LowerCasePipe:** The LowerCasePipe can be used to convert text to lowercase.
  * **CurrencyPipe:** The CurrencyPipe can be used to format numbers as currency.
  * **DecimalPipe:** The DecimalPipe can be used to format numbers with a specific number of decimal places.
  * **PercentPipe:** The PercentPipe can be used to format numbers as percentages.

# 7. Optimization

* Loads the necessary, all the others parts lazy.
* Minimize bundles.
* Clean de the code.
* Reduce images size.
* Use components small in size.
* Good practice when using observables.
* Use `strict` and `production` mode.

# 8. Dependency Injection
- Pending

# 9. Reactive using Observable and RxJS
- Pending

# 10. Routing
- Pending

# 11. Security
- Pending 