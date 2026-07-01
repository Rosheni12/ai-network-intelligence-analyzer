# AI Network Intelligence Analyzer

An AI-powered Network Intelligence and Sustainability Platform that transforms raw network traffic into actionable cybersecurity insights using Machine Learning, Intelligent Analytics, and Generative AI.

Developed as part of the **IBM SkillsBuild AI Internship**, this project demonstrates the practical application of Artificial Intelligence, Machine Learning, and Generative AI in intelligent network monitoring, anomaly detection, security analytics, and executive-level cybersecurity reporting.

---

## Live Demo

**Streamlit Application**

https://ai-network-intelligence-analyzer-nxzbyhw6kagqcg8zcndhey.streamlit.app/

---

# Overview

Modern enterprise networks generate thousands of packets every second, making manual monitoring increasingly complex and time-consuming. Traditional monitoring solutions primarily display raw statistics and logs, requiring significant manual effort to identify abnormal behaviour, assess network health, and detect potential security risks.

The AI Network Intelligence Analyzer automates this process by capturing live network traffic, performing intelligent analytics, classifying network traffic using Machine Learning, detecting anomalous behaviour, evaluating overall network health, estimating privacy and sustainability metrics, and generating structured AI-powered cybersecurity reports through an interactive Streamlit dashboard.

---

# Project Highlights

- Live network traffic capture using Scapy
- Intelligent feature engineering pipeline
- Random Forest-based traffic classification
- Isolation Forest anomaly detection
- Custom Network Health Score
- Privacy Score evaluation
- Carbon Footprint estimation
- AI-generated cybersecurity reports using Google Gemini Flash
- Lightweight Streamlit deployment
- Interactive visual analytics dashboard

---

# Key Features

- Live Network Packet Capture using Scapy
- Automated Network Traffic Analysis
- Machine Learning-based Traffic Classification
- Unsupervised Anomaly Detection
- Custom Network Health Score
- Health Grade and Risk Assessment
- Privacy Score Evaluation
- Estimated Network Carbon Footprint
- Interactive Streamlit Dashboard
- AI-generated Cybersecurity Reports using Google Gemini Flash
- Exportable Network Analytics and Summary Reports

---

# Architecture Highlights

- Modular project architecture for scalability and maintainability
- Live packet acquisition using Scapy
- Automated preprocessing and feature engineering pipeline
- Hybrid Machine Learning architecture combining supervised and unsupervised learning
- Intelligent analytics engine for network health, privacy, sustainability, and risk evaluation
- Google Gemini Flash integration for executive-level cybersecurity reporting
- Lightweight Streamlit deployment for browser-based access

---

# System Architecture

```
                 Live Network Traffic
                         │
                         ▼
              Packet Capture (Scapy)
                         │
                         ▼
               Raw Dataset (CSV)
                         │
                         ▼
              Data Preprocessing
                         │
                         ▼
             Feature Engineering
                         │
                         ▼
        Machine Learning Models
         ┌──────────────────────┐
         │                      │
         ▼                      ▼
 Random Forest          Isolation Forest
 Traffic Classification  Anomaly Detection
         │                      │
         └──────────┬───────────┘
                    ▼
         Network Analytics Engine
                    │
                    ▼
      Gemini AI Report Generation
                    │
                    ▼
      Interactive Streamlit Dashboard
```

---

# Technology Stack

## Programming Language

- Python

## Data Processing

- Pandas
- NumPy

## Machine Learning

- Scikit-learn
- Random Forest Classifier
- Isolation Forest
- Joblib

## Network Analysis

- Scapy

## Data Visualization

- Plotly

## Web Application

- Streamlit

## Generative AI

- Google Gemini Flash API

---

# Requirements

- Python 3.11+
- Streamlit
- Google Gemini API Key
- Internet connection for AI report generation

---

# Dataset

Unlike projects that rely on publicly available datasets, this platform uses **live network traffic captured directly from a real local network environment** using the Scapy packet manipulation library.

The captured packets are converted into a structured CSV dataset (`network_traffic.csv`) before entering the preprocessing pipeline.

## Captured Network Attributes

- Timestamp
- Source IP Address
- Destination IP Address
- Protocol (TCP / UDP)
- Source Port
- Destination Port
- Packet Size

---

# Feature Engineering

To improve analytical capability and Machine Learning performance, raw packet data is enriched using domain-specific engineered features.

The engineered features include:

- Protocol Encoding
- HTTPS Detection
- DNS Detection
- Rule-based Traffic Type Classification
- Packet Size Categorization
- Traffic Volume Calculation
- Privacy Score Estimation
- Estimated Network Carbon Footprint

These engineered features enable more meaningful analytics and improve the effectiveness of the Machine Learning models.

---

# Machine Learning Models

## Random Forest Classifier

### Purpose

Performs supervised multi-class network traffic classification.

### Output Classes

- Browsing
- Communication
- System
- Unknown

### Configuration

- 200 Decision Trees

---

## Isolation Forest

### Purpose

Performs unsupervised anomaly detection by identifying abnormal network behaviour that deviates from normal traffic patterns.

### Configuration

- Contamination Rate = 5%

The combination of supervised and unsupervised learning enables the platform to accurately classify normal traffic while simultaneously detecting anomalous network behaviour.

---

# Intelligent Analytics Dashboard

The analytics engine automatically computes multiple network intelligence metrics.

## Network Intelligence

- Network Health Score
- Health Grade
- Risk Level
- Overall Network Status

## Privacy & Sustainability

- Privacy Score
- HTTPS Adoption Percentage
- Estimated Network Carbon Footprint

## Traffic Analytics

- Total Network Packets
- Active Clients
- Protocol Distribution
- Traffic Type Distribution
- Packet Category Distribution
- Top Client
- Top Protocol

These analytics are presented through an interactive Streamlit dashboard with dynamic Plotly visualizations.

---

# Generative AI Integration

Google Gemini Flash is integrated into the platform to automatically convert network analytics into structured cybersecurity reports.

Each generated report includes:

- Executive Summary
- Network Health Assessment
- Security Analysis
- Root Cause Analysis
- Risk Assessment
- Actionable Recommendations
- Predicted Network Outlook

The AI-generated reports eliminate manual report preparation by presenting technical findings in a structured, management-friendly format, enabling faster understanding and informed decision-making.

---

# How It Works

1. Capture live network packets using Scapy.
2. Preprocess and clean the captured traffic data.
3. Perform feature engineering.
4. Classify network traffic using Random Forest.
5. Detect anomalous behaviour using Isolation Forest.
6. Calculate network health, privacy, and sustainability metrics.
7. Generate AI-powered cybersecurity reports using Google Gemini Flash.
8. Display results through an interactive Streamlit dashboard.

---

# Deployment

The application is deployed using **Streamlit Community Cloud**, providing a lightweight browser-based interface without requiring local software installation.

### Live Application

https://ai-network-intelligence-analyzer-nxzbyhw6kagqcg8zcndhey.streamlit.app/

Users can:

- Upload captured network traffic
- Analyze network intelligence metrics
- View interactive visualizations
- Generate AI-powered cybersecurity reports
- Export network summaries

The lightweight deployment model reduces infrastructure requirements while enabling rapid access, simplified maintenance, and seamless demonstration.

---

# Project Structure

```
AI-Network-Intelligence-Analyzer
│
├── dashboard/
│   ├── app.py
│   ├── components/
│   ├── core/
│   └── assets/
│
├── src/
├── models/
├── data/
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/Rosheni12/AI-Network-Intelligence-Analyzer.git

cd AI-Network-Intelligence-Analyzer
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

**Important:** Never upload your `.env` file or API key to GitHub.

## Run the Application

```bash
streamlit run dashboard/app.py
```

---

# Future Scope

Potential future enhancements include:

- Continuous real-time packet monitoring
- Historical trend analysis
- Predictive network analytics
- Integration with IBM QRadar and enterprise SIEM platforms
- Automated alert notifications
- Role-Based Access Control (RBAC)
- Enterprise-scale cloud deployment

---

# Repository

GitHub Repository

https://github.com/Rosheni12/AI-Network-Intelligence-Analyzer

---

# Developer

**Rosheni Balaji**

B.C.A. Data Science (Third Year)

SRM University of Science and Technology, Ramapuram

IBM SkillsBuild AI Internship

---

# Disclaimer

This project was developed solely for academic and educational purposes as part of the IBM SkillsBuild AI Internship. It demonstrates the practical application of Artificial Intelligence, Machine Learning, Intelligent Analytics, and Generative AI in network monitoring and cybersecurity analytics.

---

# License

This project is licensed under the MIT License.
