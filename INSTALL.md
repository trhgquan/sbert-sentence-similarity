# Installation
Create virtual environment so that you don't have to install any additional packages in your real workspace:
```
python -m venv venv
```

Activate virtual environment 
- on Windows:
    ```
    venv\Scripts\activate
    ```

- on Linux:
    ```
    venv/bin/activate
    ```

You can deactivate it by replacing `activate` with `deactivate` (i.e `venv/bin/deactivate` on Linux).

Finally, install required packages in `requirements.txt`:
```
pip install -r requirments.txt
```

Now everything should fine. To run the demo server on Windows, run `run.bat`. On Linux, run `run.sh`.