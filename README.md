# api-load-testing-locust
API LOAD TESTING FRAMEWORK USING LOCUST

Overview:
This project performs load testing of CRM-related APIs using Locust. It simulates realistic user traffic patterns such as viewing the dashboard, creating leads, and fetching a user profile. The Locust web UI provides real-time performance metrics.

Features:

User behavior simulation using Locust tasks

Adjustable user count and spawn rate

Real-time performance dashboard (RPS, latency, errors)

HTML reports exportable from Locust

Folder Structure:
api-load-testing-locust/
locustfile.py
test_scenarios.md
results/
sample_report.html
README.md

Technologies Used:

Locust

Python

REST APIs

Test Architecture:

Locust master provides UI to configure tests

Users are spawned as virtual clients

Tasks are executed against CRM API endpoints

Metrics are collected and displayed live

Setup Instructions:

Install Locust:
pip install locust

Running Tests:
Start Locust:
locust -f locustfile.py

Open UI in browser:
http://localhost:8089

Enter:

Number of users: example 500

Spawn rate: example 20

Host: https://example-crm.com

Test Scenarios:

500 concurrent users

Each user performs dashboard load, lead creation, and profile fetch

Duration: 10 minutes

Metrics collected: RPS, latency percentiles, error percentage

Sample Results:
Requests per second: 450 to 520
p95 latency: 180 ms
Failure rate: 0.2%

Future Improvements:

Add authentication token for secure APIs

Support distributed Locust workers

Dockerize the entire load testing environment

Push results to Prometheus and Grafana
