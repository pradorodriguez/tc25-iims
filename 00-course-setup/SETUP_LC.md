# Setup Your Local Environment

> [!WARNING]
> During the workshop session the speakers will not be able to provide assistance if you select this path.

## How to Run locally on your computer

> [!IMPORTANT]
> If you are using Github Codespaces you can skip **this section** and its substeps.

To run the code locally on your computer, you need to have locally installed the following tools:

* Git
* Version 3.12 of [Python](https://www.python.org/downloads/)
  * Python packages: check the **[requirements file](../requirements.txt)**

To then use the repository, you need to clone it:

```shell
git clone https://github.com/pradorodriguez/tc25-iims.git
cd tc25-iims
```

### Using a local Visual Studio Code with the Python support extension

We recommend using the [Visual Studio Code (VS Code)](https://code.visualstudio.com/) editor with the [Python support extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) installed for this course. This is, however, more of a recommendation and not a definite requirement

> [!NOTE]  
> Once you clone and open the directory in VS Code, it will automatically suggest you install a Python support extension.
>
> If VS Code suggests you re-open the repository in a container, decline this request in order to use the locally installed version of Python.

### Create `.env` file

The next step is to configure your **local environment variables** as follows:

* Inside the online Visual Studio Code **Explorer** section (to the left), look in the **labs** folder for a `.env-example` file.
* Copy `.env-example` file to `.env`. Open the Codespaces Visual Studio Code **Terminal** cli and execute the following command:

   ```bash
   cp .env-example .env
   ```

> [!NOTE]  
> _.env_ file is _gitignore-d_, keeping secrets safe.

* Fill in the values (replace placeholders on right side of `=`) as described in the next section.

### Populate `.env` file

Update the environment variables from the `.env` file using the provided values by the speakers.Example:

```bash
## Azure OpenAI
AZURE_SEARCH_SERVICE="https://FAKE-ACCOUNT.search.windows.net"
AZURE_SEARCH_KEY="<Azure AI Search Key>"
AZURE_OPENAI_ACCOUNT="https://FAKE-ACCOUNT.openai.azure.com/"
AZURE_OPENAI_KEY="<Azure OpenAI Key>"
AZURE_AI_MULTISERVICE_ENDPOINT="https://FAKE-ACCOUNT.cognitiveservices.azure.com/"
AZURE_AI_MULTISERVICE_KEY="<Azure AI Multi-Service (Cognitive Services) Key>"
AZURE_STORAGE_CONNECTION="ResourceId=/subscriptions/FAKE-SUBCRIPTION=ID/resourceGroups/FAKE-RESOURCE-GROUP/providers/Microsoft.Storage/storageAccounts/FAKE-ACCOUNT;"
AZURE_STORAGE_CONTAINER="<Azure Storage Container Name>"
```

> [!WARNING]  
> **Don't forget to save the .env file when done BUT NEVER COMMIT THE CHANGES TO YOUR PUBLIC BRANCH!!!**. You can now exit the file and follow your instructor's instructions.

## Let's Get Started

The code and demos are located in the **[./labs folder](../labs/)**
