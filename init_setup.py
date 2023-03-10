echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with version 3.8"
conda create --prefix ./venv python=3.8 -y
echo [$(date)]: "Activate env"
source activate ./venv
echo [$(date)]: "install dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"