import time
from datetime import datetime
from main import load_posts, save_posts
from social_media import SocialMediaManager


def check_scheduled_posts():
    posts = load_posts()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    for post in posts:

        if (
            post["status"] == "scheduled"
            and post["scheduled_time"] <= current_time
        ):

            print("\nScheduled post found!")
            print(f"Platform: {post['platform']}")
            print(f"Message: {post['message']}")

            manager = SocialMediaManager()

            success = manager.create_post(post["message"])

            if success:
                post["status"] = "published"
                post["published_at"] = current_time

                save_posts(posts)

                print("Post automatically published!")


def start_scheduler():

    print("================================")
    print(" SOCIAL MEDIA AUTOMATION")
    print(" Scheduler Started")
    print("================================")
    print("Checking for scheduled posts...")
    print("Press CTRL+C to stop.\n")

    try:

        while True:

            check_scheduled_posts()

            time.sleep(30)

    except KeyboardInterrupt:

        print("\nScheduler stopped.")


if __name__ == "__main__":
    start_scheduler()