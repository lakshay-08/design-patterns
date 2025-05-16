# Abstract Factory Design Pattern

## Overview

The **Abstract Factory** design pattern is a **creational pattern** that provides an interface for creating **families of related or dependent objects** without specifying their concrete classes.

---

## When to Use

- You need to create objects that are **related by a theme** (e.g., UI components for different operating systems).
- You want to ensure that products created by a factory are **compatible**.
- You want to **decouple client code** from the actual product implementations.

---

## Key Components

- **Abstract Factory**  
  Declares interfaces for creating abstract products.

- **Concrete Factory**  
  Implements creation methods to produce concrete products.

- **Abstract Product**  
  Declares an interface for a type of product.

- **Concrete Product**  
  Implements the abstract product interface.

- **Client**  
  Uses only interfaces declared by abstract factory and abstract product.

---
