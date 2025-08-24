---
title: "Approaching load balancing"
date: 2025-08-23
layout: single
author_profile: true
header:
  overlay_image: /assets/image/clean-code-banner.jpg
  overlay_filter: 0.3
categories: [Architecture]
tags: [Java, Spring, Clean Code, Best Practices, Architecture]
---

## Load Balancing — A Dev’s Perspective

This post is inspired by some very *recent events*… wink wink 😅  
Let’s just say one server took the fall for the whole squad.  

---

### What DevOps Covers (and We Don’t Need to Worry About)
Load balancers, proxies, ingress controllers, DNS tricks ,that’s the infra team’s arena.  
They’ll set up NGINX, HAProxy, AWS ALB, or Kubernetes Ingress to make sure traffic *can* spread across nodes.  

Cool. Thanks, DevOps. 🙏  
But here’s the catch: **if the code isn’t load-balancer friendly, infra magic won’t save us.** 

---

### 1. Statelessness Is Our Job
Load balancers love stateless services. If we tie users to a specific node, we’re just sabotaging scaling.  
As a dev, I then can:  
- Move sessions out of memory → use **Redis** or JWT.  
- Store files externally → S3/Blob instead of local disk.  
- Keep services idempotent where possible.  

💡 Our code decides whether a node swap is seamless or a disaster.  

---

### 2. TPS Awareness
DevOps can tell you how many nodes you’re running.  
But only you know how many **transactions per second (TPS)** your service code can realistically handle.  

As a dev, measure:  
- **Baseline TPS per node** (via JMeter, Gatling, or Spring Boot load tests).  
- How TPS behaves on **spiky endpoints** (login, checkout, exports).  
- Whether retries **multiply load** when a node starts struggling.  

If you don’t know your per-node TPS ceiling, your scaling math is just vibes.  

---

### 3. Balancing Patterns That Hit the Code
Infra sets the balancing algorithm (Round Robin, Least Connections, Sticky).  
As devs, we need to account for side effects:  
- Sticky sessions = risk of node hotspots.  
- Round robin = assumes nodes are equally capable.  
- Least connections = better for heavy/long requests.  

💡 If you know the algo, you can predict how your code will behave under load.  

---

### 4. Spring Tools in Our Hands
This is where we can design smarter:  

- **RestTemplate/WebClient + LoadBalancer**  
 
    @LoadBalanced
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }

- **Feign Clients**

    @FeignClient(name = "user-service")
    interface UserClient {
        @GetMapping("/users/{id}")
        User getUser(@PathVariable("id") Long id);
    }

Spring Cloud Gateway → Edge routing + retries + weight-based balancing (dev-controlled).
These are the knobs we own.

### 5. Health & Resilience (Dev Side)

Infra will ping /health. What we expose is up to us:
-Add custom health indicators (e.g., DB reachable, cache alive).
-Fail fast when a dependency is dead.
-Wrap calls in Resilience4j circuit breakers + retries.

If we don’t expose proper signals, the load balancer keeps hitting a sick node, and TPS tanks.

### 6. Observability = Developer Debugging

DevOps can give you dashboards, but the signal quality comes from our code:
-Add request IDs to logs (MDC).
-Publish TPS metrics via Micrometer.
-Trace requests with OpenTelemetry spans.

Without this, all DevOps sees is “node 2 is red.” With our code-level observability, we can explain why.
Dev’s Load Balancing Checklist

-My service is stateless
-I know my TPS ceiling per node
-I know which balancing algo is in play and its side effects
-My app exposes real health signals
-I’ve added retries + circuit breakers (without doubling traffic)
-I can see TPS per node in metrics and trace requests across nodes

Closing Thought

DevOps gives us the shiny load balancer.
Our job is to make sure our service doesn’t choke when it’s actually balanced.

Do it right, and 1,000 TPS spreads smoothly across the cluster.
Do it wrong, midnight calls.

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/) — learning the hard lessons so you don’t have to.  
