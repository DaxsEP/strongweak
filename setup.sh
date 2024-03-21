mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"s9128122@cycu.org.tw\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml