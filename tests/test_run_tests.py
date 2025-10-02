from src import Module1, Module2

class TestRunModules:
    def test_module1_greet(self, sample_fixture):
        assert sample_fixture == "sample data1", f"Fixture did not yield expected data but: {sample_fixture}"
        mod1 = Module1()
        assert mod1.greet() == "Hello from Module 1!"

    def test_module2_greet(self):
        mod2 = Module2()
        assert mod2.greet() == "Hello from Module 2!"

    def test_module1_negative(self):
        mod1 = Module1()
        assert mod1.greet() != "Hello from Module 2!"

    def test_module2_negative(self):
        mod2 = Module2()
        assert mod2.greet() != "Hello from Module 1!"

    def test_module1_negative_by_text(self):
        mod1 = Module1()
        assert mod1.greet() != "Hello from Module 1 again!"
