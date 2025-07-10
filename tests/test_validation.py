import unittest

from idx_normalizator import (
    normalize_idx, 
    validate_idx
)

class TestValidation(unittest.TestCase):
    def test_normalize_idx(self):
        names={
            "Example Cammel Name": "example-cammel-name",
        }
        for name, idx in names.items():
            nornalized = normalize_idx(name)
            self.assertEqual(nornalized, idx)

if __name__ == "__main__":
    unittest.main()
