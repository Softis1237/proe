
from camoufox_integration import CamouFoxIntegration
from profile_manager import ProfileManager
from proxy_manager import ProxyManager
from task_automation import TaskAutomation
from monitoring import log_action

class AppController:
    def __init__(self):
        self.profile_manager = ProfileManager()
        self.proxy_manager = ProxyManager()
        self.task_automation = TaskAutomation()
        self.camoufox = CamouFoxIntegration()

    def create_spoofed_profile(self, name):
        spoofed_data = self.camoufox.apply_spoofing()
        profile = {
            "name": name,
            "user_agent": spoofed_data["user_agent"],
            "canvas": spoofed_data["canvas"]
        }
        self.profile_manager.profiles.append(profile)
        self.profile_manager.save_profiles()
        log_action(f"Created spoofed profile: {profile}")
        return profile

# Example usage
if __name__ == "__main__":
    controller = AppController()
    profile = controller.create_spoofed_profile("TestProfile")
    print(profile)


from proxy_manager import ProxyManager

if __name__ == "__main__":
    proxy_manager = ProxyManager()
    print("Fetching free proxies...")
    proxy_manager.fetch_free_proxies()
    print(f"Found working proxies: {proxy_manager.proxies}")
