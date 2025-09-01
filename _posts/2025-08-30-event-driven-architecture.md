---
title: "Event-Driven Architecture with Spring Boot"
date: 2025-08-30
layout: single
author_profile: true
header:
  overlay_image: /assets/image/clean-code-banner.jpg
  overlay_filter: 0.3
categories: [Architecture]
tags: [Java, Spring, Clean Code, Best Practices, Architecture]
---

## Event-Driven Architecture with Spring Boot: Building Scalable and Responsive Systems

In this post, I explore how to implement EDA using **Spring Boot**, complete with practical examples and best practices. It's a little bit long becasue of code snippets that I had to strip down just to illustratw.

---

## What is Event-Driven Architecture?

Event-Driven Architecture is a software design pattern that promotes the **production, detection, consumption, and reaction to events**.  
An event is a significant change in state that occurs at a point in time. For example:

- A user places an order  
- A payment is processed successfully  
- Inventory stock drops below a threshold  

In EDA, components communicate through **events** rather than direct API calls, leading to looser coupling and better scalability.

---

## Key Benefits of EDA

- **Loose Coupling**: Services don't need to know about each other  
- **Scalability**: Components can be scaled independently  
- **Resilience**: Failure in one service doesn't necessarily break the entire system  
- **Responsiveness**: Systems can react to events in real-time  
- **Extensibility**: New consumers can be added without modifying producers  

---

## Implementing EDA with Spring Boot

Spring Boot provides excellent support for building event-driven systems through **Spring Events** and integrations with messaging platforms like **Kafka** or **RabbitMQ**.

---

### 1. Basic Spring Events

Spring Framework has a built-in event mechanism that works within a single application context:

    // 1. Define a custom event
    public class OrderCreatedEvent extends ApplicationEvent {
        private final Order order;
        
        public OrderCreatedEvent(Object source, Order order) {
            super(source);
            this.order = order;
        }
        
        public Order getOrder() {
            return order;
        }
    }

    // 2. Create an event publisher
    @Service
    public class OrderService {
        private final ApplicationEventPublisher eventPublisher;
        
        public OrderService(ApplicationEventPublisher eventPublisher) {
            this.eventPublisher = eventPublisher;
        }
        
        public Order createOrder(OrderRequest request) {
            Order order = // create order logic
            eventPublisher.publishEvent(new OrderCreatedEvent(this, order));
            return order;
        }
    }

    // 3. Create an event listener
    @Component
    public class OrderEventListener {
        
        @EventListener
        public void handleOrderCreatedEvent(OrderCreatedEvent event) {
            // Process the event, e.g., send notification, update inventory, etc.
            Order order = event.getOrder();
            System.out.println("Order created: " + order.getId());
        }
    }

### 2. Using ApplicationEventPublisher

For more complex scenarios, you can use the ApplicationEventPublisher directly:

    @Component
    public class CustomEventPublisher {
        
        private final ApplicationEventPublisher applicationEventPublisher;
        
        public CustomEventPublisher(ApplicationEventPublisher applicationEventPublisher) {
            this.applicationEventPublisher = applicationEventPublisher;
        }
        
        public void publishCustomEvent(final String message) {
            System.out.println("Publishing custom event. ");
            CustomEvent customEvent = new CustomEvent(this, message);
            applicationEventPublisher.publishEvent(customEvent);
        }
    }

    public class CustomEvent extends ApplicationEvent {
        private String message;
        
        public CustomEvent(Object source, String message) {
            super(source);
            this.message = message;
        }
        
        public String getMessage() {
            return message;
        }
    }

### 3. Asynchronous Event Processing

To process events asynchronously and avoid blocking the main thread:   

    @Configuration
    @EnableAsync
    public class AsyncConfig {
        
        @Bean(name = "eventTaskExecutor")
        public TaskExecutor taskExecutor() {
            ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
            executor.setCorePoolSize(5);
            executor.setMaxPoolSize(10);
            executor.setQueueCapacity(25);
            executor.setThreadNamePrefix("event-executor-");
            executor.initialize();
            return executor;
        }
    }

    @Component
    public class AsyncEventListener {
        
        @Async("eventTaskExecutor")
        @EventListener
        public void handleAsyncEvent(OrderCreatedEvent event) {
            // Process event asynchronously
            System.out.println("Processing order asynchronously: " + event.getOrder().getId());
        }
    }

### 4. Transaction-Bound Events

Spring allows you to publish events that are tied to transaction phases:

    @Service
    public class OrderService {
        
        private final ApplicationEventPublisher eventPublisher;
        
        public OrderService(ApplicationEventPublisher eventPublisher) {
            this.eventPublisher = eventPublisher;
        }
        
        @Transactional
        public Order createOrder(OrderRequest request) {
            Order order = // create order logic
            
            // Event will be published only if transaction commits successfully
            eventPublisher.publishEvent(new OrderCreatedEvent(this, order));
            
            return order;
        }
    }

    // Listen for events only after transaction commit
    @Component
    public class TransactionalEventListener {
        
        @TransactionalEventListener(phase = TransactionPhase.AFTER_COMMIT)
        public void handleAfterCommit(OrderCreatedEvent event) {
            // This will execute only after the transaction commits
            System.out.println("Order created after transaction commit: " + event.getOrder().getId());
        }
    }

### 5. Integrating with Messaging Systems (Kafka Example)

For distributed systems, you'll want to use a messaging platform like Kafka, RabbitMQ, or AWS SNS/SQS:

    // Add to pom.xml
    // <dependency>
    //     <groupId>org.springframework.kafka</groupId>
    //     <artifactId>spring-kafka</artifactId>
    // </dependency>

    @Configuration
    public class KafkaConfig {
        
        @Value("${spring.kafka.bootstrap-servers}")
        private String bootstrapServers;
        
        @Bean
        public ProducerFactory<String, String> producerFactory() {
            Map<String, Object> configProps = new HashMap<>();
            configProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
            configProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
            configProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, JsonSerializer.class);
            return new DefaultKafkaProducerFactory<>(configProps);
        }
        
        @Bean
        public KafkaTemplate<String, String> kafkaTemplate() {
            return new KafkaTemplate<>(producerFactory());
        }
    }

    @Service
    public class KafkaEventPublisher {
        
        private final KafkaTemplate<String, Object> kafkaTemplate;
        
        public KafkaEventPublisher(KafkaTemplate<String, Object> kafkaTemplate) {
            this.kafkaTemplate = kafkaTemplate;
        }
        
        public void publishOrderCreatedEvent(Order order) {
            kafkaTemplate.send("order-created-topic", order);
        }
    }

    @Component
    public class KafkaEventListener {
        
        @KafkaListener(topics = "order-created-topic", groupId = "notification-service")
        public void listenOrderCreatedEvent(Order order) {
            System.out.println("Received Order Created Event: " + order.getId());
            // Process the event
        }
    }

## Best Practices for Event-Driven Architecture

- **Design Events Carefully**: Events should represent *facts* about something that happened, not commands.  
- **Use Schema Evolution**: Plan for how your events will evolve over time without breaking consumers.  
- **Implement Idempotency**: Make sure processing the same event multiple times doesn’t cause duplicate side effects.  
- **Monitor Event Flows**: Add comprehensive monitoring and logging for producers and consumers.  
- **Consider Event Sourcing**: For critical operations, store all state changes as a sequence of events.  
- **Handle Dead Letter Queues**: Plan for unprocessable events to avoid data loss.  
- **Secure Your Events**: Protect sensitive data inside events with proper encryption and access control.  

---

## Common Pitfalls to Avoid

- **Over-engineering**: Not every system needs event-driven architecture.  
- **Event Spaghetti**: Too many events can make the system hard to understand and debug.  
- **Lack of Monitoring**: Without observability, async systems quickly become black boxes.  
- **Ignoring Event Ordering**: Some workflows require strict sequencing—don’t overlook this.  
- **Infinite Loops**: Avoid circular event triggers that can cause runaway processing.  

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/)