"""Unit tests using Python's unittest framework"""

import unittest
from binarysearchtree import BinarySearchTree
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    """Test cases for Pokemon class"""
    
    def test_pokemon_initialization(self):
        """Test Pokemon initialization"""
        p = Pokemon("Pikachu", 25, "Pikachuu")
        self.assertEqual(p.american_name, "Pikachu")
        self.assertEqual(p.number, 25)
        self.assertEqual(p.japanese_name, "Pikachuu")
    
    def test_pokemon_comparison_operators(self):
        """Test Pokemon comparison magic methods"""
        p1 = Pokemon("Bulbasaur", 1, "Fushigidane")
        p2 = Pokemon("Pikachu", 25, "Pikachuu")
        
        # Test __lt__
        self.assertTrue(p1 < 4)
        self.assertFalse(p2 < 4)
        
        # Test __gt__
        self.assertTrue(p2 > 4)
        self.assertFalse(p1 > 4)
        
        # Test __eq__
        self.assertTrue(p1 == 1)
        self.assertTrue(p2 == 25)
        self.assertFalse(p1 == 25)

class TestBinarySearchTree(unittest.TestCase):
    """Test cases for BinarySearchTree class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bst = BinarySearchTree()
        self.bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
        self.bst.add(Pokemon("Charmander", 4, "Hitokage"))
        self.bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
        self.bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    def test_add_operation(self):
        """Test adding nodes to BST"""
        empty_bst = BinarySearchTree()
        empty_bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
        self.assertIsNotNone(empty_bst.root)
    
    def test_duplicate_prevention(self):
        """Test that duplicates raise RuntimeError"""
        with self.assertRaises(RuntimeError):
            self.bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    
    def test_search_existing(self):
        """Test searching for existing Pokemon"""
        result = self.bst.search(25)
        self.assertTrue(result)
    
    def test_search_nonexistent(self):
        """Test searching for non-existent Pokemon"""
        result = self.bst.search(999)
        self.assertFalse(result)
    
    def test_delete_existing(self):
        """Test deleting an existing Pokemon"""
        self.bst.delete(4)  # Delete Charmander
        result = self.bst.search(4)
        self.assertFalse(result)
    
    def test_copy_operation(self):
        """Test copying BST"""
        copy_bst = self.bst.copy()
        
        # Verify copy has same structure
        self.assertTrue(copy_bst.search(1))
        self.assertTrue(copy_bst.search(25))
        
        # Verify they are independent
        self.bst.add(Pokemon("Eevee", 133, "Eievui"))
        self.assertFalse(copy_bst.search(133))  # Copy should not have Eevee

class TestFileAndMenu(unittest.TestCase):
    """Test cases for FileAndMenu class"""
    
    def test_file_loading(self):
        """Test loading Pokemon from file"""
        from fileandmenu import FileAndMenu
        
        # This test requires test_pokemon.txt to exist
        try:
            file_menu = FileAndMenu("test_pokemon.txt")
            self.assertIsNotNone(file_menu.my_bst)
            self.assertIsNotNone(file_menu.my_bst.root)
        except FileNotFoundError:
            self.skipTest("test_pokemon.txt not found")

if __name__ == "__main__":
    unittest.main()
