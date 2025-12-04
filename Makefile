VENV = venv
PYTHON = $(VENV)/Scripts/python.exe
PIP = $(VENV)/Scripts/pip.exe

start:
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install flask uvicorn
	$(VENV)/Scripts/uvicorn.exe example:app --reload --host 127.0.0.1 --port 8000
