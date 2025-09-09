---
title: "Make Logging Work for You"
date: 2025-09-09
layout: single
author_profile: true
header:
  overlay_image: /assets/image/clean-code-banner.jpg
  overlay_filter: 0.3
categories: [Architecture]
tags: [Java, Spring, Clean Code, Best Practices, Logging, Architecture]
---

Some time last week, I overheard something interesting in the office. One of our technical leads asked another to prepare a talk about logging for our weekly Java meetup.

It got me thinking. Logging is one of those things we all do every day, but very few of us actually do it well. I'll be honest, when the conversation was happening, I stayed quiet. Instead of jumping in with my opinions, I decided to write them down here where I can organize my thoughts properly.

When logging is done poorly, it makes everyone's job harder. But when it's done right, it becomes your lifeline in production.

---

## Why We Log

We don’t log just to dump text into files. We log to **tell the story of what happened**. Good logs answer:  

- What happened  
- When it happened  
- Who or what triggered it  
- Whether it succeeded or failed  

When you think about it like that, it transforms from noise into a valuable map you can follow when things go wrong.

---

## Understanding Logging Levels

Most of us have seen these, but it’s easy to misuse them:  

- TRACE → microscopic detail, usually not for production  
- DEBUG → developer-focused, turned off in prod most of the time  
- INFO → the big picture, system milestones and flow  
- WARN → something unexpected happened, but the app recovered  
- ERROR → something broke and needs investigation  
- FATAL → the system is going down (I have actually never seen this one in practise)  

If you log nothing but INFO, you’ll miss the detail. If you log everything at DEBUG, you’ll drown in noise. The balance matters.

---

## Common Mistakes

- Printing to console with `System.out.println()`  
- Logging every tiny thing until the important stuff is buried  
- Forgetting to log at all and leaving future-you blind  
- Logging passwords, tokens, or private data that should never leave memory
- Concatenating strings instead of using placeholders:  


    // bad
    log.debug("User " + username + " logged in");

    // good
    log.debug("User {} logged in", username);

## Add Context

A log entry without context is like a diary entry that just says “it happened”.
What helps:
- Correlation IDs to trace a request through services
- Timestamps in a clear format like 2025-09-09T16:30:00Z
- Which environment you’re in (dev, staging, prod)
- Safe identifiers like user IDs or transaction IDs

With context, you can follow the entire journey of a request instead of staring at random messages.

## Structured Logging

Logs should be readable by both humans and machines. Plain text is fine, but JSON or key-value logging makes a world of difference when you use tools like ELK, Splunk or Loki.

    log.info("Payment processed",
            kv("transactionId", txnId),
            kv("amount", amount),
            kv("status", status));

## Logging in Spring Boot

    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

    @Service
    public class PaymentService {

        private static final Logger log = LoggerFactory.getLogger(PaymentService.class);

        public void processPayment(String userId, double amount) {
            log.info("Processing payment for user {}", userId);//Notice how INFO tells the story
            try {
                // business logic
                log.debug("Payment amount: {}", amount); //DEBUG gives detail
            } catch (Exception e) {
                log.error("Payment failed for user {}", userId, e); //ERROR captures failures.
            }
        }
    }

Best Practices That Pay Off

- Use placeholders instead of string concatenation
- Always include context like IDs and timestamps
- Keep logs structured for easier searching
- Respect the levels, don’t abuse INFO or DEBUG
- Never log sensitive data
- Centralize logs so you don’t SSH into servers to hunt them
- Use async logging in high-throughput apps
- Set log rotation and retention policies so files don’t grow forever

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/)