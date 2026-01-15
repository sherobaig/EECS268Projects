"""Test runner for the scheduler program"""

from scheduler import Scheduler

def test_with_file(filename):
    """Test the scheduler with a given input file"""
    print(f"\n{'='*60}")
    print(f"Testing with file: {filename}")
    print(f"{'='*60}\n")
    try:
        scheduler = Scheduler(filename)
        scheduler.run()
        print(f"\n{'='*60}")
        print("Test completed successfully!")
        print(f"{'='*60}\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error during execution: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    # Test with various input files
    print("Running test suite...\n")
    
    test_files = [
        "test_input.txt",
        "test_exception_handling.txt",
        "test_multiple_processes.txt"
    ]
    
    for test_file in test_files:
        test_with_file(test_file)
        print("\n")