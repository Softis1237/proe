
import json

class ProfileManager:
    def __init__(self, profiles_file='profiles.json'):
        self.profiles_file = profiles_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.profiles_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_profiles(self):
        try:
            with open(self.profiles_file, 'w') as f:
                json.dump(self.profiles, f, indent=4)
        except Exception as e:
            print(f"Error saving profiles: {e}")

    def create_profile(self, name):
        profile = {
            "name": name,
            "user_agent": self.generate_user_agent(),
            "timezone": "GMT+0",
            "canvas_spoofing": True
        }
        self.profiles.append(profile)
        self.save_profiles()
        return profile

    def generate_user_agent(self):
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

# Example usage
if __name__ == "__main__":
    manager = ProfileManager()
    profile = manager.create_profile("TestProfile")
    print(f"Created profile: {profile}")
