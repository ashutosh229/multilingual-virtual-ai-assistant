import os 
from pathlib import Path
import logging

logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s]: %(message)s:"
)

listOfFiles = [
  "src/__init__.py",
  "src/helper.py",
  ".env",
  "requirements.txt",
  "setup.py",
  "app.py",
  "research/trials.ipynb"
]

for filepath in listOfFiles:
  filePath = Path(filepath)
  filedir,filename = os.path.split(filePath)
  
  if filedir!="":
    os.makedirs(filedir,exist_ok=True)
    logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
  if (not os.path.exists(filePath)) or (os.path.getsize(filePath)==0):
    with open(filePath,"w") as f:
      pass
      logging.info(f"Creating empty file: {filePath}")
  else:
    logging.info(f"{filename} is already exists")
    

