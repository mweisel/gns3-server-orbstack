# Check if Python is installed
if ! hash python3; then
  printf 'Python is not installed.\n'
  return 1
fi

# Check if Python is version 3.8 or later
python3 -c 'import sys; assert sys.version_info >= (3,8)' &> /dev/null
if [ $? -ne 0 ]; then
  printf 'Python version 3.8 or later is required.\n'
  return 1
fi

# Create a virtual environment
if [ -d '.venv' ]; then
  rm -rf .venv
fi
python3 -m venv .venv && source .venv/bin/activate

# Upgrade packaging tools
pip install --upgrade pip setuptools
deactivate && source .venv/bin/activate

# Install packages
pip install --requirement requirements.txt
deactivate && source .venv/bin/activate
