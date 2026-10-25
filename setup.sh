#!/usr/bin/env bash

echo "🛠️ Connecting tool components..."

chmod +x src/scanner.py
chmod +x pre-commit

cp pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

echo "🔗 Success: Everything is connected and ready!"
