Getting random quotes from the dictionary using a quantum random 
number generator aka QRNG by https://qrng.anu.edu.au
Dictionary contains 100 quotes Russian and English lang.

Usage: 
    git clone URL repo
    install requirements: $ pip install -r requirements.txt
    choose your dict at 4 or 5 line by comment and uncomment: 
        "from eng import var as v" or "from rus import var as v"
    run: python main.py and read quote

!!!   Warning   !!!
        For the predictions to work, the entropy needs to be high enough.
    Therefore, do not use this application more than 1 time per day. 
    Good luck)
