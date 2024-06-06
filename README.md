# RAG_POC 
Retrieval-Augmented Generation (RAG) System

This project implements a Retrieval-Augmented Generation (RAG) system using FastAPI, ObjectBox, and transformers. The system stores documents in a database, retrieves relevant documents based on a query, and generates a response using a pre-trained language model.

## Project Structure

```
src/
│
├── app.py
├── main.py
├── models/
│   ├── document.py
│   └── __init__.py
├── services/
│   ├── embedding.py
│   ├── query.py
│   ├── response.py
│   └── __init__.py
├── db/
│   ├── init_db.py
│   ├── schema/
│   │   ├── document.py
│   │   └── __init__.py
│   └── __init__.py
├── utils/
│   ├── similarity.py
│   └── __init__.py
└── documents.json
```

## Setup and Installation

### Prerequisites

- Python 3.8+
- Pip

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Setting Up the Database

Ensure the database directory is correctly accessible and there are no permission issues preventing its creation or modification.

### Run the Application

Set the environment variable to disable tokenizer parallelism warning and run the application:

```sh
export TOKENIZERS_PARALLELISM=false
python src/main.py
```

### Endpoints

- **POST /query**: Submit a query to retrieve relevant documents and generate a response.

## Example Usage

### documents.json

Store the documents in a JSON file:

```json
[
    {
        "text": "Patient John Doe had an appointment on 2024-05-15. The visit included a routine check-up and blood tests. He has been diagnosed with hypertension and prescribed Lisinopril."
    },
    {
        "text": "Jane Smith visited the clinic on 2024-05-20 for a follow-up on her diabetes management. Her blood sugar levels were stable, and she continues on Metformin."
    },
    {
        "text": "Robert Johnson was seen on 2024-05-25 for knee pain. He was advised to rest and prescribed Ibuprofen. A follow-up visit is scheduled in two weeks."
    }
]
```

### Curl Request

Submit a query using curl:

```sh
curl -X POST "http://0.0.0.0:8000/query" -H "Content-Type: application/json" -d '{"query": "What medication was prescribed to John Doe?"}'
```

### Expected Response

```json
{
  "response":"Tylenol (Tetraazole) (Pentafil) Tylopentasil (Cocaine) Lipipril"}
}
```

## Code Explanation

### `src/db/init_db.py`

Encapsulates the database initialization, access, and cleanup logic in a `Database` class.

### `src/services/embedding.py`

Handles the generation of embeddings for documents and storing them in the database.

### `src/services/query.py`

Handles the retrieval of relevant documents based on a query and generating a response using a pre-trained language model.

### `src/app.py`

Sets up the FastAPI application and defines the endpoints.

### `src/main.py`

Initializes the database and stores documents from a JSON file, then starts the FastAPI server.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Explanation

- **Project Structure**: Updated to reflect that the files are located inside the `src` directory.
- **Run the Application**: Updated the command to run the application from the `src` directory.

This README should now correctly represent the structure and setup of your project with the files inside the `src` directory.