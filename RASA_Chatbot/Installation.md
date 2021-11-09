# Windows Install:
                1) Install Anaconda Navigator from the app store with Python 3.6+
                2) Click Environments
                3) Click create
                4) Name the environment (rasax), select python 3.7, click create
                5) Once the environment is created click the play button next to it and select 'open terminal'
                6) From the command line run: conda install -c conda-forge httptools
                                a. Type y to proceed
                7) From the command line run: conda install -c anaconda git
                                a. Type y to proceed
                8) From the command line run: pip install --upgrade multidict==4.6.1
                9) From the command line run: pip install rasa-x==0.28.3 --trusted-host storage.googleapis.com --extra-index-url https://pypi.rasa.com/simple
                10) From the command line run: mkdir rasa_test
                11) From the command line run: cd rasa_test
                12) From the command line run: rasa init
                13) From the command line run: rasa x
