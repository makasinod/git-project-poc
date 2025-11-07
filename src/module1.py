from logger import Logger

class Module1:
    def __init__(self):
        # Initialize logger with class name
        self.logger = Logger(self.__class__.__name__).get_logger()
        self.logger.info("Module1 initialized")
        self.name = "Module 1"

    def greet(self):
        return f"Hello from {self.name}!"
    
if __name__ == "__main__":
    module = Module1()
    print(module.greet())
