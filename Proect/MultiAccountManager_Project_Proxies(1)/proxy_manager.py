
import requests
import time

class ProxyManager:
    def __init__(self):
        self.proxies = []

    def add_proxy(self, proxy):
        self.proxies.append(proxy)

    def test_proxy(self, proxy):
        try:
            response = requests.get("http://httpbin.org/ip", proxies={"http": proxy}, timeout=5)
            return response.status_code == 200
        except:
            return False

    def rotate_proxies(self):
        return self.proxies[0] if self.proxies else None

    def remove_dead_proxies(self):
        self.proxies = [proxy for proxy in self.proxies if self.test_proxy(proxy)]

    def fetch_free_proxies(self):
        url = "https://www.proxy-list.download/api/v1/get?type=http"  # Example public API for proxies
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                raw_proxies = response.text.split("\n")
                for proxy in raw_proxies:
                    if self.test_proxy(proxy.strip()):
                        self.add_proxy(proxy.strip())
        except Exception as e:
            print(f"Error fetching proxies: {e}")

# Example usage
if __name__ == "__main__":
    manager = ProxyManager()
    manager.fetch_free_proxies()
    print(f"Working proxies: {manager.proxies}")
