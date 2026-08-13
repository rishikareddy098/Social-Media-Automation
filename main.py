import json
from datetime import datetime
from social_media import SocialMediaManager

POSTS_FILE = "posts.json"


def load_posts():
    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_posts(posts):
    with open(POSTS_FILE, "w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


def add_post():
    print("\n--- Create Social Media Post ---")

    platform = input("Platform: ").strip() or "demo"
    message = input("Message: ").strip()
    scheduled_time = input(
        "Scheduled time (YYYY-MM-DD HH:MM): "
    ).strip()

    if not message:
        print("Message cannot be empty.")
        return

    try:
        datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid date/time format.")
        return

    posts = load_posts()

    new_post = {
        "id": len(posts) + 1,
        "platform": platform,
        "message": message,
        "scheduled_time": scheduled_time,
        "status": "scheduled"
    }

    posts.append(new_post)
    save_posts(posts)

    print("\nPost scheduled successfully!")


def view_posts():
    posts = load_posts()

    print("\n--- Scheduled Posts ---")

    if not posts:
        print("No posts found.")
        return

    for post in posts:
        print(f"\nID: {post['id']}")
        print(f"Platform: {post['platform']}")
        print(f"Message: {post['message']}")
        print(f"Scheduled: {post['scheduled_time']}")
        print(f"Status: {post['status']}")


def publish_post():
    posts = load_posts()

    if not posts:
        print("No posts available.")
        return

    view_posts()

    try:
        post_id = int(input("\nEnter post ID to publish: "))
    except ValueError:
        print("Invalid ID.")
        return

    for post in posts:
        if post["id"] == post_id:

            manager = SocialMediaManager()

            success = manager.create_post(post["message"])

            if success:
                post["status"] = "published"
                save_posts(posts)
                print("Post published successfully.")

            return

    print("Post not found.")


def main():
    while True:

        print("\n==============================")
        print(" SOCIAL MEDIA AUTOMATION")
        print("==============================")

        print("1. Create Post")
        print("2. View Posts")
        print("3. Publish Post")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_post()

        elif choice == "2":
            view_posts()

        elif choice == "3":
            publish_post()

        elif choice == "4":
            print("Exiting Social Media Automation.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()