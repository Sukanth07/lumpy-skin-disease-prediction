import subprocess
import site
from config import *

def copy_builder():
    try:
        site_packages_path = site.getsitepackages()[0]
        destination_path = os.path.join(site_packages_path, 'google/protobuf/internal/')
        subprocess.run(["cp", "./builder.py", destination_path], shell=True, check=True)
    except Exception as e:
        return f"An error occurred: {e}"

css="""
    .container { 
        max-width: 90%; 
    }

    .title {
        font-family: 'Trebuchet MS';
        text-align: center;
        font-size: 2em;
        font-weight: bold;
        padding: 10px 0;
        background-color: #1f2121;
    }

    input, textarea{
        background-color: #18191a;
    }

    #output-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

"""