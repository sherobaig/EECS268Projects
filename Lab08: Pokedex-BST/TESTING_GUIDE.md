# Testing Guide for Pokemon Pokedex Application

This guide explains different ways to test your Pokemon Pokedex application.

## Quick Start Testing

### 1. Manual Testing (Interactive)

Run the main program and test interactively:

```bash
python main.py
```

When prompted, enter: `test_pokemon.txt`

Then try these operations:
- **Search**: Choose option 1, enter a pokedex number (e.g., 25 for Pikachu)
- **Add**: Choose option 2, add a new Pokemon
- **Print**: Choose option 3, try different traversal orders (pre-order, in-order, post-order)
- **Remove**: Choose option 4, enter a pokedex number to delete
- **Copy**: Choose option 5 to create a copy of the tree
- **Quit**: Choose option 6 to exit

### 2. Automated Test Script

Run the comprehensive test script:

```bash
python test_bst.py
```

This will test:
- Pokemon class initialization and comparison operators
- BST add operations (including duplicate prevention)
- BST search operations
- All three traversal methods (pre-order, in-order, post-order)
- BST delete operations
- BST copy operations

### 3. Unit Tests (unittest framework)

Run the unit tests:

```bash
python test_unittest.py
```

Or with verbose output:

```bash
python test_unittest.py -v
```

This uses Python's built-in unittest framework and provides detailed test results.

## Test Data File

The `test_pokemon.txt` file contains sample Pokemon data in the format:
```
AmericanName PokedexNumber JapaneseName
```

Example:
```
Pikachu 25 Pikachuu
Bulbasaur 1 Fushigidane
Charmander 4 Hitokage
```

## What to Test

### Core Functionality
1. **File Loading**: Verify Pokemon are loaded correctly from file
2. **Search**: Test searching for existing and non-existent Pokemon
3. **Add**: Test adding new Pokemon and preventing duplicates
4. **Print**: Test all three traversal orders produce correct output
5. **Remove**: Test deleting Pokemon from the tree
6. **Copy**: Test that copied trees are independent

### Edge Cases
1. **Empty Tree**: Test operations on an empty BST
2. **Single Node**: Test operations on a tree with one node
3. **Invalid Input**: Test handling of invalid user input
4. **File Not Found**: Test error handling for missing files
5. **Duplicate Prevention**: Verify RuntimeError is raised for duplicates

## Expected Behavior

### In-Order Traversal
Should print Pokemon in ascending order by pokedex number:
1, 4, 7, 25, 133, 150...

### Search Operation
- Returns `True` and prints Pokemon info if found
- Returns `False` if not found

### Delete Operation
- Removes the Pokemon from the tree
- Handles three cases: 0 children, 1 child, 2 children

### Copy Operation
- Creates an independent copy of the tree
- Changes to original don't affect copy and vice versa

## Troubleshooting

If tests fail:
1. Check that `test_pokemon.txt` exists in the same directory
2. Verify all Python files are in the same directory
3. Check for syntax errors: `python -m py_compile *.py`
4. Ensure Python 3.x is being used

## Additional Testing Tips

1. **Test with different file sizes**: Try with 1 Pokemon, 5 Pokemon, 10+ Pokemon
2. **Test boundary values**: Try pokedex number 1, very large numbers
3. **Test invalid inputs**: Non-numeric pokedex numbers, empty strings
4. **Test tree structure**: Add Pokemon in different orders to test tree balancing
