import os
import requests
from dotenv import load_dotenv

load_dotenv()


class SocialMediaManager:
    def __init__(self):
        self.platform = os.getenv("PLATFORM", "demo")
        self.access_token = os.getenv("ACCESS_TOKEN", "")

    def create_post(self, message):
        """
        Creates a social media post.

        In demo mode, the post is printed instead of being
        published to a real social media account.
        """

        if not message.strip():
            print("Error: Post message cannot be empty.")
            return False

        if self.platform == "demo":
            print("\n--- SOCIAL MEDIA POST ---")
            print(message)
            print("-------------------------")
            print("Demo post created successfully!")
            return True

        if not self.access_token:
            print("Error: ACCESS_TOKEN is not configured.")
            return False

        print(f"Preparing post for platform: {self.platform}")

        # API integration will be added here for the selected platform.
        return True


def test_connection():
    manager = SocialMediaManager()

    print("Social Media Automation")
    print(f"Platform: {manager.platform}")

    if manager.platform == "demo":
        print("Demo mode is active.")
        return True

    if manager.access_token:
        print("Access token found.")
        return True

    print("No access token configured.")
    return False


if __name__ == "__main__":
    test_connection()