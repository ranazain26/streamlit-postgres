# Streamlit Postgres Assignment

Starter scaffold for the Streamlit + PostgreSQL assignment. This repository contains a Streamlit app that connects to PostgreSQL and implements CRUD operations for "opportunities" plus analytics and utility pages.

Structure
```
streamlit-postgres-assignment/
├── app/
│   ├── main.py
│   ├── db.py
│   ├── queries.py
│   ├── auth.py
│   ├── utils.py
│   └── pages/
│       ├── 1_Add_Opportunity.py
│       ├── 2_View_Search.py
│       ├── 3_Update_Opportunity.py
│       ├── 4_Delete_Opportunity.py
│       ├── 5_Analytics_Dashboard.py
│       ├── 6_CSV_Upload_Export.py
│       ├── 7_Duplicate_Detection.py
│       ├── 8_Deadline_Alerts.py
│       └── 9_Database_Health_Check.py
├── database/
│   ├── init.sql
│   └── seed_data.sql
├── screenshots/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
├── README.md
└── report.pdf
```

How to run (development):

1. Create a Python virtual environment and install dependencies from `requirements.txt`.
2. Provide a `.env` file based on `.env.example` with your Postgres credentials.
3. Start Postgres (locally or via docker-compose) and run `database/init.sql` and `database/seed_data.sql`.
4. Run the Streamlit app:

```powershell
streamlit run app/main.py
```

Files added are minimal starters. Update queries and connection settings to match your environment.
