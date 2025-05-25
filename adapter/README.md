# 🔌 Adapter Design Pattern

## Overview

This project demonstrates the **Adapter Design Pattern** using a real-world analogy: adapting a European plug to a US socket. The Adapter pattern is part of the **structural design patterns** and is used to allow incompatible interfaces to work together.

---

## 🧠 What Is the Adapter Pattern?

The Adapter Pattern acts as a **bridge** between two incompatible interfaces. It allows existing classes to be used with others without modifying their source code.

---

## 📁 Project Structure

- `adapter.py` – Core implementation of the Adapter Pattern
- `README.md` – This file

---

## 💡 Components Explained

- **Adaptee** (`EuropeanPlug`):  
  This class has a method (`connect_european`) that is not compatible with the client's expected interface.

- **Target Interface** (`USPlugInterface`):  
  This is the interface expected by the client code. It defines a `connect()` method.

- **Adapter** (`PlugAdapter`):  
  This class wraps the `EuropeanPlug` and converts its interface to match `USPlugInterface`.

- **Client** (`power_device`):  
  This function accepts any object implementing the `USPlugInterface` and uses the `connect()` method.

---

## 🔧 How It Works

- `EuropeanPlug` provides `connect_european()` which is not usable directly by client code expecting `connect()`.
- `PlugAdapter` adapts `EuropeanPlug` by wrapping it and exposing the `connect()` method.
- `power_device()` interacts with the adapter seamlessly as if it's a native US plug.
