# 🧱 Bridge Pattern – Python Example

This repository demonstrates the **Bridge Design Pattern** in Python using a simple example involving `Shape` (abstraction) and `DrawingAPI` (implementation).

---

## 📘 What is the Bridge Pattern?

The **Bridge Pattern** is a structural design pattern that lets you **decouple an abstraction from its implementation** so the two can vary independently. This is especially useful when you have multiple dimensions of variation.

---

## 🎯 Example Scenario

You want to draw shapes like circles using different rendering APIs (e.g., OpenGL, DirectX). Instead of creating a class for each combination (like `CircleOpenGL`, `CircleDirectX`), the Bridge pattern helps you separate the abstraction (`Shape`) from the implementation (`DrawingAPI`).

---

## 🧩 Structure

    Shape (Abstraction)
    │
    ├── Circle (Refined Abstraction)
    │
    └── uses → DrawingAPI (Implementor Interface)
    ├── OpenGLAPI (Concrete Implementor)
    └── DirectXAPI (Concrete Implementor)

---

## 🐍 Python Code Overview

- `Shape`: Abstract base class that defines a common interface.
- `Circle`: A concrete shape that delegates drawing to a `DrawingAPI`.
- `DrawingAPI`: Interface for drawing implementations.
- `OpenGLAPI` and `DirectXAPI`: Provide actual drawing logic.

---
