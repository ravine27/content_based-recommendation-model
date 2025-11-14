mkdir -p ~/.streamlit/

#!/bin/bash
# setup.sh

# Create README.MD if it doesn't exist but README.md does
if [ ! -f "README.MD" ] && [ -f "README.md" ]; then
    cp README.md README.MD
fi

# Install the package
pip install -e .

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml