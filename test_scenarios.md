Test Scenario for Locust:

1. 500 Users Spawn Rate: 20 users/sec
2. Each user performs:
    - Dashboard load
    - Lead creation
    - Profile fetch
3. Test duration: 10 minutes
4. Metrics to collect:
    - RPS (Requests per second)
    - Latency p50, p90, p95, p99
    - Failure rate
    - Max concurrent users
