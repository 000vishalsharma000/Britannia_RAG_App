# Rag App README

## Demo

**Deployed App**: [Rag App on Hugging Face Spaces](https://huggingface.co/spaces/vishal-sharma/Britannia_RAG_App)

**Video Tutorial**:  
[![Rag App Tutorial](https://github.com/000vishalsharma000/bechdo/assets/132067848/58d451f6-473b-45c1-af34-497e02fa0f8e)](https://drive.google.com/file/d/1Z8EjS_zpqun7Nhd2HjqEnDBMncluB8i8/view?usp=drivesdk)

## Overview

Rag App is a Streamlit application that uses the Allama model, ChromaDB, and Hugging Face embeddings to answer queries from a provided knowledge base.

## Features

- Allama Model for advanced natural language understanding.
- ChromaDB for efficient and scalable database management.
- Hugging Face Embeddings for precise query matching.
- User-friendly Streamlit interface.

## Installation

### Prerequisites

- Python 3.8 or higher
- Pip
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/rag-app.git
   cd rag-app
   ```

2. **Install Dependencies:**:
   ```bash
    pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:**:
   ```bash
    export HF_API_TOKEN=your_hugging_face_api_token
   ```

## Usage

### Run the App

```bash
streamlit run app.py
```

## Access the App

Open your browser and go to [http://localhost:8501](http://localhost:8501).

## Configuration

### Environment Variables

- `HF_API_TOKEN`: Your Hugging Face API token.
- `CHROMADB_URI`: The URI for connecting to your ChromaDB instance.

### Configuration File

You can also configure the application settings in the `config.yaml` file. Make sure to update this file with your specific settings for the Allama model, ChromaDB, and Hugging Face embeddings.

## Deployment

Deploy the app on Hugging Face Spaces:

1. **Create a Space** on Hugging Face.
2. **Upload Repository files**.
3. **Set Environment Variables** in the space settings.
4. **Deploy** the app.

**Deployed App Link**: [Rag App on Hugging Face Spaces](https://huggingface.co/spaces/your-username/rag-app)

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Credits

- **Allama Model**: [Allama](https://allama.ai)
- **ChromaDB**: [ChromaDB](https://chromadb.org)
- **Hugging Face**: [Hugging Face](https://huggingface.co)
