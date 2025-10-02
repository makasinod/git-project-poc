from src import Module1, Module2, logger

def main():
    mod1 = Module1()
    mod2 = Module2()

    logger.info(f"Module1: {mod1.greet()}")
    logger.info(f"Module2: {mod2.greet()}")

print('hello')