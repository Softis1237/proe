
import logging

logging.basicConfig(level=logging.INFO, filename='app.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(action, status="Success"):
    logging.info(f"{action}: {status}")

# Example usage
if __name__ == "__main__":
    log_action("Task Execution", "Success")
