import unittest
from src.mymerkletree.core import merkletree




class TestMerkleTree(unittest.TestCase):

    def test_short_message(self):
        """Message shorter than λ should return itself."""
        m = "short"       # 5 bytes
        s = "salt" * 8    # 32 bytes
        result = merkletree(m, s)
        self.assertEqual(result, m.encode())

    def test_exactly_lambda(self):
        """Message exactly λ bytes should return itself."""
        m = "a" * 32      # 32 bytes
        s = "s" * 32
        result = merkletree(m, s)
        self.assertEqual(result, m.encode())

    def test_long_message(self):
        """Message longer than λ bytes should return a 32-byte hash."""
        m = "abcdefghijklmnopqrstuvwxyz1234567"
        s = "salt12345678901234567890123456"
        result = merkletree(m, s)
        self.assertEqual(len(result), 32)
        self.assertIsInstance(result, bytes)

    def test_different_salts(self):
        """Different salts produce different hashes."""
        m = "HI HOW ARE Y0U ? WHAT IS YOUR NAME ??"
        s1 = "salt0000000000000000000000000001"
        s2 = "salt0000000000000000000000000002"
        hash1 = merkletree(m, s1)
        hash2 = merkletree(m, s2)
        self.assertNotEqual(hash1, hash2)

    def test_different_messages(self):
        """Different messages produce different hashes."""
        m1 = "message one"
        m2 = "message two"
        s = "saltysaltsaltysaltsaltysalt1234"
        hash1 = merkletree(m1, s)
        hash2 = merkletree(m2, s)
        self.assertNotEqual(hash1, hash2)

    

if __name__ == "__main__":
    unittest.main()
