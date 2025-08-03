---
title: "⚡ Pay-As-You-Go Distributed Solar"
layout: single
permalink: /projects/payg-solar/
header:
  overlay_image: /assets/images/payg-solar.jpg
  overlay_filter: 0.3
tags: [STM32, Android, PHP, Java Spring, IoT, Solar, Embedded]
---

## ⚡ Pay-As-You-Go Distributed Solar System

A decentralized, token-based solar power solution designed for rural areas, built to deliver electricity to households that can’t afford full monthly bills, one token at a time.

---

### 🏗️ Built Between 2016–2019  
This project came out of a real-world problem: **how do you deliver solar electricity to low-income homes in a way that’s affordable, tamper-proof, and offline-friendly?**

---

### 🔧 Tech Stack (Then & Now)

**2016–2019 (MVP):**
- **Microcontroller**: STM32 (bare-metal C)
- **UI**: Android (Java)
- **Backend**: PHP API + MySQL
- **Comms**: GSM module (SIM800L)
- **Storage**: EEPROM for token caching

**Modernization Plan (2024+):**
- **Backend Rewrite**: Java Spring Boot API (secure + scalable)
- **Mobile UI Refresh**: Kotlin/Jetpack Compose or Flutter
- **Add-ons**: QR token scanning, OTA firmware updates, mobile-based admin dashboard

---

### 🔋 What It Does

1. **Customer buys a token** using mobile USSD or app.
2. **PHP API (legacy)** or **Java Spring (new)** generates a unique token.
3. **User enters token** into the Android interface via Bluetooth or keypad.
4. **STM32 controller verifies the token**, energizes a relay, and powers the load.
5. When the token expires, **power is cut automatically**.

---

### ✅ Highlights

- **Offline-ready**: Works with GSM or SMS , no internet required.
- **Tamper detection**: Interrupts power on bypass attempts.
- **Micro-payments**: Enables buying power in small units (e.g., $0.5 at a time because Zimbabwe and our US dollars).
- **Low-power design**: Optimized for 12V DC solar systems.
- **EEPROM caching**: Retains balance and token data during blackouts.

---

### 🧠 Lessons Learned

- Real-world GSM is messy: signal strength and latency matter.
- Token generation must be **secure but lightweight**.
- STM32 with direct relay control is powerful but needs precise timing.
- Building a UX for non-tech-savvy users means **simplicity is everything**.
- PHP was fast to prototype but **not scalable** , hence the Spring Boot rewrite.

---

### 🔭 Future Potential

- Integrate **blockchain or token ledger** for village-level energy credits.
- Add **remote monitoring** via LoRa or NB-IoT.
- Community energy-sharing between users with surplus.

---

> _“This project taught me that real-world innovation isn’t always about bleeding-edge tech , sometimes it’s about solving fundamental problems with whatever tools you’ve got.”_


📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/). I’m documenting the grind so you don’t have to make the same mistakes I did.
