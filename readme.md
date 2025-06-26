# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate


Ollama
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
