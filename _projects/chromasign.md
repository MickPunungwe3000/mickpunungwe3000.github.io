---
title: "ChromaSign – LED Billboard Engine"
layout: single
permalink: /projects/chromasign/
header:
  overlay_image: /assets/images/chromasign-banner.jpg
  overlay_filter: 0.3
tags: [Java, JavaFX, RTMP, WebSocket, Digital Signage, Embedded]
---

##  ChromaSign – LED Billboard Engine

**ChromaSign** is a custom-built digital signage platform powering LED billboards across South Africa, designed for reliability, speed, and full control in environments where failure is not an option.

---

###  What I Built

A full-stack signage system with:

- A **desktop player** that runs on cheap hardware
- A **content manager** for scheduling text, video, and images
- A **real-time control API** for live updates and sync

Designed to replace clunky, expensive commercial signage solutions, and it works in the wild today.

---

###  Tech Stack

- **Frontend**: JavaFX for the media player UI
- **Backend**: Java (Spring Boot for control API)
- **Protocols**: WebSocket for real-time content push
- **Streaming**: RTMP for live video injection
- **Storage**: SQLite (lightweight + portable)
- **Other**: Electron UI wrapper for cross-platform compatibility

---

###  What It Does

- Plays video, image, and text content on digital LED billboards
- Allows operators to schedule playlists and override them live
- Syncs time-based events across multiple displays
- Runs on low-spec machines for edge-based control

---

###  Key Features

- **Real-time control** via WebSocket or admin panel
- **Drag-and-drop playlist manager**
- **Offline fallback**: cached content plays during network loss
- **Hot reload**: push updated content without restarting the app
- **Cross-platform**: Linux & Windows support

---

###  Engineering Wins

- Built a **custom animation engine** using JavaFX for precise timing
- Handled **frame-perfect media playback**
- Wrote my own **RTMP ingestion module** to support video mixing
- Designed an **electron-wrapped manager** for non-tech operators
- Survived real-world use with **zero major crashes** in the field

---

###  In Production

- Used by **multiple billboard operators** across South Africa
- Powers **street-level LED signs, mall screens, and event displays**
- Built for rugged environments , low power, minimal maintenance

---

> _"The commercial signage space is bloated and overpriced. I built a remote signage system to give clients full control - and save them a ton of money."_  

---
📌 Follow along weekly right here or catch me on [LinkedIn](https://www.linkedin.com/in/maverikpunungwe/). I’m documenting the grind so you don’t have to make the same mistakes I did.
