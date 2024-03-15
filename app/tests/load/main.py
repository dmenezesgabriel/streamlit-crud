from locust import HttpUser, between, task  # type: ignore


class AppUser(HttpUser):  # type: ignore
    wait_time = between(2, 5)

    # Endpoint
    @task  # type: ignore
    def home_page(self) -> None:
        self.client.get("/")
