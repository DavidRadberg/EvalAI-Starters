import subprocess
import sys
from pathlib import Path

#dirname = os.path.dirname(__file__)
#req_name = os.path.join(dirname, "requirements.txt")
#print(req_name)
#numpy==1.18.1
#pandas==0.25.3
#keras==2.2.4
#tensorflow==1.14.0
#tqdm==4.41.1
#flask==1.1.1
#flask-cors==3.0.8
#waitress==1.4.2
#matplotlib==3.1.2

#subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy==1.18.1"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas==0.25.3"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "keras==2.2.4"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "tensorflow==1.14.0"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm==4.41.1"])
subprocess.check_output([sys.executable, "-m", "pip", "install", "-r", str(Path(__file__).parent.absolute())+"/requirements.txt"])
#subprocess.check_call([sys.executable, "-m", "pip", "install", "h5py==2.10.0"])

from .main import evaluate
