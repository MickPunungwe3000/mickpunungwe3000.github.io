---
published: true
title: "The Real Signs You Need SOLID Principles in Your Code"
date: 2025-07-19
layout: single
author_profile: true
header:
  overlay_image: /assets/image/clean-code-banner.jpg
  overlay_filter: 0.3
categories: [CleanCode]
tags: [Java, SOLID, Design Principles]
---

SOLID principles are foundational to maintainable, scalable software design.

A colleague once dropped a line that stuck with me:

> “If you’re implementing an interface and returning `null` or throwing `UnsupportedOperationException`, you probably need Interface Segregation.”

That one sentence nailed it better than most books.

It made me realize: we overcomplicate design principles. We memorize definitions but don’t know **when** or **why** to actually use them.

So here’s SOLID explained in _plain language_, with real signals that tell you **“Yo, it’s time to apply this.”**

---

### 🧱 S – Single Responsibility Principle (SRP)

**One reason to change. One job. That’s it.**

If your class is juggling different concerns, reading files, validating inputs, sending emails then that’s a massive red flag.

> **Test yourself**:  
> “Would two different people ask for changes to this class for different reasons?”

**Example**

```java
    // BAD: One class doing multiple unrelated jobs
    class UserManager {
        void saveUser(User user) { ... }
        void sendWelcomeEmail(User user) { ... } // Shouldn’t live here
        void logActivity(User user) { ... }     // Nope
    }

    // BETTER: Separate classes by responsibility
    class UserRepository { void save(User user) { ... } }
    class EmailService { void sendWelcome(User user) { ... } }
    class AuditLogger { void logActivity(User user) { ... } }

```

### 🔌 O – Open/Closed Principle (OCP)

**Open for extension, closed for modification.**

If you keep cracking open the same class every time there’s a new requirement, you're violating OCP.

Ask this:
“Can I add a new behavior without editing existing working code?”

**Example**

    // BAD: Have to modify this class every time a new shape is added
    class AreaCalculator {
        double calculate(Object shape) {
            if (shape instanceof Circle) { ... }
            else if (shape instanceof Rectangle) { ... }
            // Keep adding more else-ifs?
        }
    }

    // BETTER: Use polymorphism
    interface Shape {
        double calculateArea();
    }

    class Circle implements Shape {
        public double calculateArea() { ... }
    }

    class Rectangle implements Shape {
        public double calculateArea() { ... }
    }

### 🐧 L – Liskov Substitution Principle (LSP)

**Subclasses should behave like their parent class - no surprises.**

If your subclass throws exceptions or breaks assumptions just to “fit in,” it doesn’t belong.

Quick test:
“If I use this subclass anywhere the parent is expected, will it work without weird behavior?”

**Example**

    // BAD: Violates LSP
    class Bird { void fly() { ... } }

    class Penguin extends Bird {
        void fly() { throw new UnsupportedOperationException(); } // uh-oh
    }

    // BETTER: Use better abstraction
    interface Bird { void eat(); }

    interface FlyingBird extends Bird { void fly(); }

    class Penguin implements Bird {
        public void eat() { ... }
    }

    class Eagle implements FlyingBird {
        public void fly() { ... }
        public void eat() { ... }
    }

### 🎯 I – Interface Segregation Principle (ISP)

**Don’t make classes implement methods they don’t care about.**

If you have to write return null; or throw new UnsupportedOperationException();, your interface is too damn fat.
Ask yourself:
“Am I implementing methods that have nothing to do with my object’s job?”

**Example**

    // BAD: Too broad
    interface Worker {
        void work();
        void eat();
    }

    // Robot is not hungry
    class Robot implements Worker {
        public void work() { ... }
        public void eat() { throw new UnsupportedOperationException(); } // Red flag
    }

    // BETTER: Split it
    interface Workable { void work(); }
    interface Eatable { void eat(); }

    class Human implements Workable, Eatable { ... }
    class Robot implements Workable { ... }

### 🔌 D – Dependency Inversion Principle (DIP)

**High-level modules shouldn’t depend on low-level details. Both should depend on abstractions.**

If you hardcode your service to use a specific class (like new MySQLDatabase()), swapping or testing becomes painful.

Check this:
“If I wanted to replace this dependency with something else (like a mock or a different DB), can I do it easily?”

**Example**

    // BAD: Tight coupling to low-level details
    class OrderService {
        private MySQLDatabase db = new MySQLDatabase(); // Hard to test/mock
    }

    // BETTER: Depend on abstraction
    interface Database {
        void save(Order order);
    }

    class OrderService {
        private final Database db;

        public OrderService(Database db) {
            this.db = db;
        }
    }

### Final Thought

SOLID isn’t about sounding smart.
It’s about writing code that survives growth, change, and real-world stress.

If you ever catch yourself:

-Editing the same class for multiple features
-Dreading changes because everything’s tangled
-Implementing methods you don’t need
-Struggling to test or swap dependencies

Then yes, you need SOLID.
And you need it now.

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/). I’m documenting the grind so you don’t have to make the same mistakes I did.