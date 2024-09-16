import unittest
from project.furniture import Furniture

class TestFurniture(unittest.TestCase):

    def test_constructor_and_properties(self):
        furniture = Furniture("Chair", 150.0, (120, 80, 100), in_stock=True, weight=30.0)
        self.assertEqual(furniture.model, "Chair")
        self.assertEqual(furniture.price, 150.0)
        self.assertEqual(furniture.dimensions, (120, 80, 100))
        self.assertTrue(furniture.in_stock)
        self.assertEqual(furniture.weight, 30.0)

    def test_model_validation(self):
        with self.assertRaises(ValueError) as model:
            Furniture("", 100.0, (45, 45, 90))
        self.assertEqual(str(model.exception),
                         "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError) as model:
            Furniture("x" * 51, 100.0, (45, 45, 90))
        self.assertEqual(str(model.exception),
                         "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_price_validation(self):
        with self.assertRaises(ValueError) as price:
            Furniture("Table", -1, (100, 50, 30))
        self.assertEqual(str(price.exception), "Price must be a non-negative number.")

    def test_dimensions_validation(self):
        with self.assertRaises(TypeError) as cm:
            Furniture("Desk", 200.0, ('150', 75, 40))
        self.assertIn("not supported between instances of 'str' and 'int'", str(cm.exception))

        with self.assertRaises(ValueError) as cm:
            Furniture("Desk", 200.0, (150, 75))
        self.assertEqual(str(cm.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as cm:
            Furniture("Desk", 200.0, (150, 75, 40, 10))
        self.assertEqual(str(cm.exception), "Dimensions tuple must contain 3 integers.")

    def test_weight_validation(self):
        with self.assertRaises(ValueError) as weight:
            Furniture("Desk", 200.0, (120, 60, 75), weight=-10)
        self.assertEqual(str(weight.exception), "Weight must be greater than zero.")

    def test_available_status(self):
        furniture_out_of_stock = Furniture("Couch", 300.0, (200, 100, 90), in_stock=False)
        status_out_of_stock = furniture_out_of_stock.get_available_status()
        self.assertEqual(status_out_of_stock, "Model: Couch is currently unavailable.")

        furniture_in_stock = Furniture("Couch", 300.0, (200, 100, 90), in_stock=True)
        status_in_stock = furniture_in_stock.get_available_status()
        self.assertEqual(status_in_stock, "Model: Couch is currently in stock.")

    def test_get_specifications(self):
        furniture_with_weight = Furniture("Desk", 200.0, (150, 75, 70), weight=30.5)
        expected_with_weight = "Model: Desk has the following dimensions: 150mm x 75mm x 70mm and weighs: 30.5"
        actual_with_weight = furniture_with_weight.get_specifications()
        self.assertEqual(actual_with_weight, expected_with_weight)

        furniture_without_weight = Furniture("Desk", 200.0, (150, 75, 70))
        expected_without_weight = "Model: Desk has the following dimensions: 150mm x 75mm x 70mm and weighs: N/A"
        actual_without_weight = furniture_without_weight.get_specifications()
        self.assertEqual(actual_without_weight, expected_without_weight)


if __name__ == "__main__":
    unittest.main()
