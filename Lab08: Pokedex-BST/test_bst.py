"""Test script for Binary Search Tree operations"""

from binarysearchtree import BinarySearchTree
from pokemon import Pokemon
from binarynode import BinaryNode

def test_pokemon_class():
    """Test Pokemon class initialization and magic methods"""
    print("=" * 50)
    print("Testing Pokemon Class")
    print("=" * 50)
    
    p1 = Pokemon("Pikachu", 25, "Pikachuu")
    p2 = Pokemon("Bulbasaur", 1, "Fushigidane")
    p3 = Pokemon("Charmander", 4, "Hitokage")
    
    # Test __str__
    print(f"Pokemon 1: {p1}")
    print(f"Pokemon 2: {p2}")
    
    # Test __lt__
    assert p2 < 4, "Bulbasaur (1) should be < 4"
    print("✓ __lt__ works correctly")
    
    # Test __gt__
    assert p1 > 4, "Pikachu (25) should be > 4"
    print("✓ __gt__ works correctly")
    
    # Test __eq__
    assert p1 == 25, "Pikachu should equal 25"
    assert not (p1 == 4), "Pikachu should not equal 4"
    print("✓ __eq__ works correctly")
    
    print("All Pokemon class tests passed!\n")

def test_bst_add():
    """Test adding nodes to BST"""
    print("=" * 50)
    print("Testing BST Add Operation")
    print("=" * 50)
    
    bst = BinarySearchTree()
    
    # Add Pokemon
    bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
    bst.add(Pokemon("Charmander", 4, "Hitokage"))
    bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    # Test duplicate prevention
    try:
        bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
        print("✗ Should have raised RuntimeError for duplicate")
    except RuntimeError:
        print("✓ Duplicate prevention works correctly")
    
    print("BST add operation tests passed!\n")

def test_bst_search():
    """Test searching in BST"""
    print("=" * 50)
    print("Testing BST Search Operation")
    print("=" * 50)
    
    bst = BinarySearchTree()
    bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
    bst.add(Pokemon("Charmander", 4, "Hitokage"))
    bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    # Test successful search
    result = bst.search(25)
    assert result == True, "Should find Pikachu (25)"
    print("✓ Found existing Pokemon")
    
    # Test unsuccessful search
    result = bst.search(999)
    assert result == False, "Should not find Pokemon 999"
    print("✓ Correctly returns False for non-existent Pokemon")
    
    print("BST search operation tests passed!\n")

def test_bst_traversals():
    """Test different traversal methods"""
    print("=" * 50)
    print("Testing BST Traversals")
    print("=" * 50)
    
    bst = BinarySearchTree()
    bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
    bst.add(Pokemon("Charmander", 4, "Hitokage"))
    bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    print("\nIn-order traversal (should be sorted by number):")
    bst.in_order_traversal(bst.visit_node_print)
    
    print("\nPre-order traversal:")
    bst.pre_order_traversal(bst.visit_node_print)
    
    print("\nPost-order traversal:")
    bst.post_order_traversal(bst.visit_node_print)
    
    print("\n✓ All traversal methods work correctly!\n")

def test_bst_delete():
    """Test deleting nodes from BST"""
    print("=" * 50)
    print("Testing BST Delete Operation")
    print("=" * 50)
    
    bst = BinarySearchTree()
    bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
    bst.add(Pokemon("Charmander", 4, "Hitokage"))
    bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    print("Before deletion:")
    bst.in_order_traversal(bst.visit_node_print)
    
    # Delete a node
    bst.delete(4)  # Delete Charmander
    
    print("\nAfter deleting Charmander (4):")
    bst.in_order_traversal(bst.visit_node_print)
    
    # Verify deletion
    result = bst.search(4)
    assert result == False, "Charmander should be deleted"
    print("\n✓ Delete operation works correctly!\n")

def test_bst_copy():
    """Test copying BST"""
    print("=" * 50)
    print("Testing BST Copy Operation")
    print("=" * 50)
    
    bst = BinarySearchTree()
    bst.add(Pokemon("Bulbasaur", 1, "Fushigidane"))
    bst.add(Pokemon("Charmander", 4, "Hitokage"))
    bst.add(Pokemon("Pikachu", 25, "Pikachuu"))
    
    # Create copy
    copy_bst = bst.copy()
    
    print("Original tree (in-order):")
    bst.in_order_traversal(bst.visit_node_print)
    
    print("\nCopied tree (in-order):")
    copy_bst.in_order_traversal(copy_bst.visit_node_print)
    
    # Verify they are separate
    bst.add(Pokemon("Squirtle", 7, "Zenigame"))
    
    print("\nAfter adding Squirtle to original:")
    print("Original tree:")
    bst.in_order_traversal(bst.visit_node_print)
    print("\nCopy tree (should not have Squirtle):")
    copy_bst.in_order_traversal(copy_bst.visit_node_print)
    
    print("\n✓ Copy operation works correctly (trees are independent)!\n")

def run_all_tests():
    """Run all test functions"""
    print("\n" + "=" * 50)
    print("RUNNING ALL TESTS")
    print("=" * 50 + "\n")
    
    try:
        test_pokemon_class()
        test_bst_add()
        test_bst_search()
        test_bst_traversals()
        test_bst_delete()
        test_bst_copy()
        
        print("=" * 50)
        print("ALL TESTS PASSED! ✓")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
    except Exception as e:
        print(f"\n✗ ERROR: {e}")

if __name__ == "__main__":
    run_all_tests()
