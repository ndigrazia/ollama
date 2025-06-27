# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate


# Ollama

python3 -m venv ~/projects/dev/ollama

source ./projects/dev/ollama/bin/activate

pip install notebook

pip install ollama

pip install requests

pip install pillow

pip install langchain_community
 
sudo service ollama stop

sudo service ollama start

ollama -v

ollama list

ollama run gemma2:2b

ollama pull <model-name>

ollama stop <model-name>

curl http://localhost:11434/api/chat -d '{ "model": "gemma2:2b", "messages": [{"role": "user", "content": "what is the EEUU capital?", "stream": "false"}]}'

# Android Ollama

Termux application

https://github.com/termux/termux-app

termux-app_v0.119.0-beta.1+apt-android-7-github-debug_arm64-v8a.apk

deepseek-r1 (llm)

run app

run termux-setup-storage

pkg upgrade

pkg install git cmake golang

git clone --depth 1 https://github.com/ollama/ollama.git

cd ollama

go build .

./ollama serve & (generate private key and run ollama)

./ollama run deepseek-r1:1.5b

Article: Running llama3.2 on Android: A step-by-step guide using ollama (dev.to)

https://dev.to/koolkamalkishor/running-llama-32-on-android-a-step-by-step-guide-using-ollama-54ig 



