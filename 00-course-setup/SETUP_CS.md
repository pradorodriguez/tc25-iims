# Setup Your CodeSpace Environment

## Create CodeSpaces Secrets

To properly execute the code and demos of this workshop, several Azure Keys and Values must be created as environment variables (CodeSpaces Secrets).

> [!NOTE]
>
> The Keys and Values will be provided by the speaker at the beginning of the session.

* In your fork of the main repo, go to the **Settings** button in the top menu bar.

![Terminal](./images/cs5.jpg)

* In the left navigation panel, go to: **Security**, **Secrets and Variables** and **Codespaces**.
* Create each secret below by clicking the **New repository secret**.  Take care to name them exactly as shown, as these will be the names of the variables inside of the codespaces environment.

![Terminal](./images/cs2.jpg)

* These are the keys for the secrets: (do not use quotes or blank spaces):

| Key/Secret  | Value  |
| :--- | :--- |
| AZURE_SEARCH_SERVICE | https://FAKE-ACCOUNT.search.windows.net |
| AZURE_SEARCH_KEY | <key_value_provided_by_speaker> |
| AZURE_OPENAI_ACCOUNT | https://FAKE-ACCOUNT.openai.azure.com/ |
| AZURE_OPENAI_KEY | <key_value_provided_by_speaker> |
| AZURE_AI_MULTISERVICE_ENDPOINT | https://FAKE-ACCOUNT.cognitiveservices.azure.com/ |
| AZURE_AI_MULTISERVICE_KEY | <key_value_provided_by_speaker> |
| AZURE_STORAGE_CONNECTION | <key_value_provided_by_speaker> |
| AZURE_STORAGE_CONTAINER | <key_value_provided_by_speaker> |
| | |

## Create the CodeSpaces environment

Select the **Code** option on your forked version of this repo, select the **Codespaces** tab and select the **Create codespace on main** option.

> [!NOTE]
>
> This step will automatically open a new browser explorer tab with an online version of Visual Studio Code. This will be your CodeSpaces environment.

![Dialog showing buttons to create a codespace](./images/cs1.jpg)

### Configure the CodeSpaces VSCode environment

* **Enable the Jupyter extension**: click the **Extensions** buttom located in the left Visual Studio navigation bar, in the upper search box, type **Jupyter** and click the **Install** buttom.

![Jupyter](./images/jupyter.jpg)

### How to run the labs/code?

* The demos are provided as Jupyter notebooks (`.ipynb` files).
* **To run the Jupyter Notebook**, inside Github Codespaces Visual Studio Code, select the demo inside the **labs** folder, then click **Select Kernel** (at top right of the jupyter notebook) and select the default **Python 3.12.1** option shown.
* You can now **Run** each action or **Run All** to execute the whole notebook.

![VSC Python Kernel](./images/kernel.jpg)

### ALTERNATIVE OPTION TO CODESPACES VISUAL STUDIO CODE: 

## Let's Get Started

The code and demos are located in the **[./labs folder](../labs/)**




# 2.5 Alternative:  Local Computer Setup

If you are running the code locally on your computer, complete the steps below.  **Codespace users can ignore this step.**

### Create `.env` file

We assume that you have already read the guidance above, created the Azure OpenAI service, obtained the required authentication credentials (API_KEY) and have the endpoint URL.

The next step is to configure your **local environment variables** as follows:

1. Inside the online Visual Studio Code **Explorer** section (to the left), look in the root folder for a `.env.copy` file
2. Copy that file to `.env` using the command below. This file is _gitignore-d_, keeping secrets safe.

Open the Codespaces Visual Studio Code **Terminal** cli and execute the following command:

   ```bash
   cp .env.copy .env
   ```

3. Fill in the values (replace placeholders on right side of `=`) as described in the next section.

### Populate `.env` file

Now update the environment variables from the `.env` file to reflect the **Deployment name** used from above. This will typically be the same as the model name unless you changed it explicitly. So, as an example, you might have:

```bash
## Azure OpenAI
AZURE_OPENAI_API_VERSION='2024-02-15-preview' # Default is set!
AZURE_OPENAI_API_KEY='<API-KEY-STRING>'
AZURE_OPENAI_ENDPOINT='https://<endpoint-url>.openai.azure.com/'
AZURE_OPENAI_DEPLOYMENT='gpt-4 turbo-2024-04-09' 
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT='text-embedding-ada-002'
```

**Don't forget to save the .env file when done BUT NEVER COMMIT THE CHANGES TO YOUR PUBLIC BRANCH!!!**. You can now exit the file and follow your instructor's instructions.


## Disclaimer
