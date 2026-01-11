"""
Test script to verify workspace setup without requiring external dependencies
"""
import sys
from pathlib import Path

def test_structure():
    """Test that all required directories and files exist"""
    print("Testing workspace structure...")
    
    base = Path(__file__).parent
    
    required_files = [
        'main.py',
        'requirements.txt',
        'README.md',
        'setup.sh',
        'configs/model.yaml',
        'configs/inference.yaml',
    ]
    
    required_dirs = [
        'models/speech_encoder',
        'models/expression_model',
        'models/motion_model',
        'models/renderer',
        'preprocessing',
        'inference',
        'optimization',
        'api',
        'evaluation',
        'data',
        'demo',
        'deployment',
    ]
    
    errors = []
    
    for file_path in required_files:
        if not (base / file_path).exists():
            errors.append(f"Missing file: {file_path}")
    
    for dir_path in required_dirs:
        if not (base / dir_path).exists():
            errors.append(f"Missing directory: {dir_path}")
    
    if errors:
        print("❌ Structure test failed:")
        for error in errors:
            print(f"  - {error}")
        return False
    
    print("✓ All required files and directories present")
    return True


def test_imports():
    """Test that all modules can be imported"""
    print("\nTesting module imports...")
    
    try:
        # Test package imports (checking __init__.py structure only)
        sys.path.insert(0, str(Path(__file__).parent))
        
        # Check if __init__.py files exist and are valid Python
        base = Path(__file__).parent
        
        test_packages = [
            'preprocessing',
            'inference',
            'optimization',
            'api',
            'evaluation',
        ]
        
        for package in test_packages:
            init_file = base / package / '__init__.py'
            if not init_file.exists():
                raise FileNotFoundError(f"Missing {package}/__init__.py")
            
            # Try to parse the file (check syntax)
            import ast
            with open(init_file, 'r') as f:
                ast.parse(f.read())
        
        print("✓ All package __init__.py files are valid")
        return True
        
    except Exception as e:
        print(f"❌ Import test failed: {e}")
        return False


def test_config():
    """Test that configuration files are valid YAML"""
    print("\nTesting configuration files...")
    
    try:
        import yaml
        
        base = Path(__file__).parent
        
        with open(base / 'configs' / 'model.yaml') as f:
            model_config = yaml.safe_load(f)
            assert 'speech_encoder' in model_config
            assert 'expression_model' in model_config
            assert 'motion_model' in model_config
            assert 'renderer' in model_config
            assert 'fps' in model_config
        
        with open(base / 'configs' / 'inference.yaml') as f:
            inference_config = yaml.safe_load(f)
            assert 'device' in inference_config
            assert 'precision' in inference_config
            assert 'batch_size' in inference_config
        
        print("✓ Configuration files are valid")
        return True
        
    except ImportError:
        print("⚠ PyYAML not installed, skipping config validation")
        return True
    except Exception as e:
        print(f"❌ Config test failed: {e}")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("Avatar System Workspace Tests")
    print("=" * 60)
    
    results = []
    results.append(test_structure())
    results.append(test_imports())
    results.append(test_config())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✓ All tests passed!")
        print("=" * 60)
        sys.exit(0)
    else:
        print("❌ Some tests failed")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()
