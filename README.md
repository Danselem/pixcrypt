# PixCrypt GPT
An AI product for describing product images.


### Version 0.1.1

   Initial release of the application.
</details>

## Installation
### Option 1: Using `uv` and `Makefile`

To get started with the `Pixcrypt`, follow these steps:

1. Clone the repository:
```bash
   git clone https://github.com/Danselem/pixcrypt.git
   cd nvidia_blueprint/research_assistant
```

2. Installing **uv**

Use the [link](https://docs.astral.sh/uv/getting-started/installation/) to install `uv` depending on your platform.

>⚠️ **Note:** Ensure you have `make` installed on your PC. If you do not have `make` installed, kindly follow the instructions for [Windows](https://gnuwin32.sourceforge.net/packages/make.htm)
 and [Linux](https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/).

3. Install dependencies
```bash
    make install-python
    make install
```

4. Set up environmental variables
```bash 
    make env
```
Then fill in the required API keys in the `.env` file in your project directory.

5. Start the app
```bash
    make run
```

### Option 2: Using pip only

1. Clone this repository:

    ```bash
    git clone https://github.com/Danselem/pixcrypt.git
    ```

2. Change to the cloned repository directory:

    ```bash
    cd pixcrypt
    ```

3. Create a virtual environment

    ```bash
    python3.10 -m venv .venv
    ```

4. Activate the virtual environment

    ```bash
    source .venv/bin/activate
    ```

5. Install the required Python packages:

    ```bash
    pip install --upgrade pip && pip install -r requirements.txt
    ```


## Usage

### Option 1: Running the Streamlit App Locally

1. Run the Streamlit app:

    ```bash
    streamlit run app.py &
    ```

2. Open a web browser and navigate to `http://localhost:8501` to access the app running inside the container.

3. Follow the steps in the Streamlit interface to use PixCrypt GPT.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](./LICENSE)