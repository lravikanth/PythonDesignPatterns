import threading
import unittest

from creational.singleton import AppConfig, SingletonMeta


class SingletonTest(unittest.TestCase):
    def test_same_instance(self):
        self.assertIs(AppConfig(), AppConfig())

    def test_state_is_shared(self):
        AppConfig().set("mode", "test")
        self.assertEqual(AppConfig().get("mode"), "test")

    def test_separate_classes_get_separate_instances(self):
        class Other(metaclass=SingletonMeta):
            pass

        self.assertIsNot(Other(), AppConfig())
        self.assertIs(Other(), Other())

    def test_thread_safe(self):
        class Counter(metaclass=SingletonMeta):
            pass

        results = []
        threads = [threading.Thread(target=lambda: results.append(Counter())) for _ in range(50)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(len({id(r) for r in results}), 1)


if __name__ == "__main__":
    unittest.main()
