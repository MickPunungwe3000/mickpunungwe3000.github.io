---
title: "Layered Architecture Simplified"
date: 2024-08-02
layout: single
author_profile: true
header:
  overlay_image: /assets/image/clean-code-banner.jpg
  overlay_filter: 0.3
categories: [Architecture]
tags: [Java, SOLID, Design Principles]
---

## Layered Architecture Simplified

**Layered architecture = clean separation of concerns.**  

Most apps follow this structure:

---

### 1. **Controller Layer**
Handles HTTP requests. No business logic here.

```java
@RestController
public class UserController {
    @GetMapping("/users/{id}")
    public UserDto getUser(@PathVariable Long id) {
        return userService.getUser(id);
    }
}

### 2. Service Layer

Business logic lives here. Talks to repos.

@Service
public class UserService {
    public UserDto getUser(Long id) {
        User user = repo.findById(id).orElseThrow();
        return mapper.toDto(user);
    }
}

### 3. Repository Layer

Handles database. Nothing else.

@Repository
public interface UserRepository extends JpaRepository<User, Long> {}

Why it matters

    Easier to test

    Easier to maintain

    Grows better with time

Golden Rule:
Don’t mix layers.
Controllers don’t talk to DB.
Services don’t return ResponseEntity.

Keep it clean. Keep it boring. That’s how systems survive.

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/). I’m documenting the grind so you don’t have to make the same mistakes I did.