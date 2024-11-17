import subprocess
import site
from src.config import *

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