from locust import HttpUser, between, task


class AppUser(HttpUser):
    wait_time = between(2, 5)

    # Endpoint
    @task
    def home_page(self):
        self.client.get("/")
