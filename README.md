# 🎓 Internship & Job Tracking Dashboard

A containerized, multi-page web application built with Streamlit and PostgreSQL to help university departments track, manage, and analyze student internship and job opportunities.

## 👥 Team Members
* Rana M. Zain Zahid
* Usman Butt
* Muhammad Abdullah

## 🏗️ System Architecture
The application runs entirely within Docker Compose, orchestrating three main services:

User Browser    |    
v
Streamlit App Container (Port 8501)    |
v
PostgreSQL Container (Port 5432)  <---->  pgAdmin Container (Port 5050)    |
v
Docker Volume for Persistent Data

## 🚀 Setup & Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ranazain26/streamlit-postgres
   cd streamlit-postgres
