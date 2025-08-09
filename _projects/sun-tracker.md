---
title: "Sun-Tracking Solar System"
layout: single
permalink: /projects/sun-tracker/
header:
  overlay_image: /assets/images/sun-tracker.jpg
  overlay_filter: 0.3
tags: [STM32, Embedded Systems, Solar, IoT, C]
---

##  Sun-Tracking Solar System

This project maximizes solar panel efficiency by automatically rotating the panel to face the sun throughout the day using real-time light sensing and servo actuation.

---

### 🔧 Tech Stack

- **Microcontroller**: STM32 (ARM Cortex-M series)
- **Sensors**: Light-sensing diodes (LDRs)
- **Control**: Direction-switching IC (exact chip name TBD)
- **Actuation**: Servo motors
- **Firmware**: Bare-metal C

---

###  What It Does

The system detects sunlight intensity from multiple angles using light-sensing diodes. Based on this input, it determines where the sun is and rotates the panel toward it using dual-axis motion.

The goal: **maximize solar energy capture without using GPS or time-based algorithms.**

---

###  Highlights

- **Dual-axis tracking** for full daylight coverage
- **Real-time analog feedback** from LDRs
- **Efficient energy usage**: Only moves when the sun’s position changes significantly
- **Improved yield**: Up to 30% more solar energy compared to fixed panels
- **Low-cost components**, designed with scalability in mind for rural deployment

---

###  What I Learned

- Fine-tuning analog signal thresholds in harsh sunlight
- Using PWM with STM32 timers for motor control
- Balancing responsiveness with power efficiency
- Debugging servo jitter and feedback noise

---

> _This system is still evolving. I'm exploring adding weather-awareness, IoT logging, and auto-calibration based on seasonal shifts._

📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/). I’m documenting the grind so you don’t have to make the same mistakes I did.
