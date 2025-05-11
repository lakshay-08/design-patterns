# Decorator Design Pattern

## What is the Decorator Pattern?

The **Decorator Design Pattern** is a structural design pattern that allows you to **dynamically add new functionality to objects** without altering their structure. This is done by placing the object inside a special wrapper (i.e., the decorator) that adds the behavior.
Instead of using inheritance to extend behavior, decorators allow you to compose behavior using wrappers.

---

## Components

- **Component**: The original object or function that we want to enhance.
- **Decorator**: A wrapper that adds new functionality before/after delegating to the original component.

---

## Python and Decorators

In Python, decorators are often implemented as functions that take another function as input and return a new function with added behavior.
