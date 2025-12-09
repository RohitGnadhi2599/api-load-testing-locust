from locust import HttpUser, task, between

class CRMUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_dashboard(self):
        self.client.get("/api/dashboard")

    @task
    def create_lead(self):
        self.client.post("/api/lead", json={
            "name": "Test User",
            "email": "test@load.com"
        })

    @task
    def user_profile(self):
        self.client.get("/api/user/profile")
