#!/bin/bash

echo "🔧 Initializing Genesis Block 0 environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

echo "✅ Environment setup complete."
