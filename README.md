# Twitter Giveaway Bot

## About this Project
This project streams Tweets to find giveaways and enters them.



## Installation
Consider this a warning.
1. Ensure you have a [Twitter Developer account](https://developer.twitter.com).

2. Place the *consumer key*, *consumer secret*, *access token* and *access secret token* into a `config.py` file.

3. Setup a virtual environment
    - Create virtual environment 
    
        ```
        $ python -m venv venv
        ```

    - Activate virtual environment
        - For Windows
 
            ```
            $ .\venv\Scripts\activate.bat
            ```

        - For Mac/Linux
            
            ```
            $ source venv\bin\activate
            ```

    - Install dependencies

        ```
        $ pip install -r requirements.txt
        ```


4. Run Python script

```
$ python bot.py
``` 