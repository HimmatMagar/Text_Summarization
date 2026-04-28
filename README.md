# Text Summarization Pipeline

A machine learning pipeline for automatic text summarization built with Python, Hugging Face Transformers, and PyTorch. This project implements a structured ML pipeline with modular components for data ingestion, validation, and future model training stages.

## Project Overview

This pipeline automates the process of:
1. **Data Ingestion** - Downloading and extracting summarization datasets from Google Drive
2. **Data Validation** - Validating dataset schema and column structure
3. **Model Training** - (Planned) Fine-tuning transformer models for text summarization
4. **Evaluation** - (Planned) Evaluating model performance using ROUGE metrics

## Installation

### Prerequisites
- Python 3.13+
- Conda (recommended for environment management)

### Setup Steps

1. **Create a conda environment**
   ```bash
   conda create -p venv python==3.13 -y
   ```

2. **Activate the environment**
   ```bash
   conda activate venv/
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
Text_Summarization/
├── config/                 # Configuration files
│   ├── config.yaml        # Pipeline paths and settings
│   ├── params.yaml        # Hyperparameters and artifact settings
│   └── schema.yaml        # Data schema validation rules
├── src/textSummarize/     # Source code
│   ├── components/        # Pipeline components (ingestion, validation, etc.)
│   ├── pipeline/          # Pipeline orchestration scripts
│   ├── entity/            # Data classes for configuration
│   ├── config/            # Configuration manager
│   ├── utils/             # Utility functions (YAML loading, file operations)
│   ├── constants/         # Path constants
│   └── __init__.py        # Logger setup
├── artifact/              # Generated artifacts (created at runtime)
├── logging/               # Log files
├── requirements.txt       # Python dependencies
└── README.md
```

## Configuration

### config.yaml
Defines paths and URLs for each pipeline stage:
- `artifact_root`: Base directory for all artifacts
- `data_ingestion`: Source URL, download paths, extraction directory
- `data_validation`: Data path, validation status file location

### params.yaml
Stores pipeline parameters and artifact settings.

### schema.yaml
Defines expected data schema for validation:
```yaml
columns:
  article: str
  highlights: str
```

## Pipeline Components

### 1. Data Ingestion Pipeline
Downloads dataset from Google Drive and extracts the zip file.

**Run:**
```bash
python src/textSummarize/pipeline/data_ingestion_pipeline.py
```

**Output:**
- `artifact/data_ingestion/summarization.csv` - Extracted dataset

### 2. Data Validation Pipeline
Validates that the dataset contains required columns (`article`, `highlights`).

**Run:**
```bash
python src/textSummarize/pipeline/data_validation_pipeline.py
```

**Output:**
- `artifact/data_validation/status.txt` - Validation status (True/False)

## Dependencies

| Package | Purpose |
|---------|---------|
| transformers | Hugging Face models for summarization |
| torch | Deep learning framework |
| pandas | Data manipulation |
| gdown | Google Drive file downloads |
| dvc | Data version control |
| mlflow | Experiment tracking |
| accelerate | Distributed training |
| datasets | Hugging Face datasets library |
| evaluate | Model evaluation metrics |
| rouge-score | ROUGE metrics for summarization |
| python-box | ConfigBox for YAML access |
| ensure | Type annotation enforcement |
| pyYAML | YAML parsing |

## Logging

All pipeline operations are logged to:
- Console (stdout)
- `logging/running_log.log` (file)

Log format: `[timestamp: level: module: message]`

## Usage Example

```bash
# Activate environment
conda activate venv/

# Run data ingestion
python src/textSummarize/pipeline/data_ingestion_pipeline.py

# Run data validation
python src/textSummarize/pipeline/data_validation_pipeline.py

# Check validation status
cat artifact/data_validation/status.txt
```

## Dataset

The pipeline downloads a summarization dataset containing:
- **article**: Input text to be summarized
- **highlights**: Reference summary/ground truth

Source: Google Drive (configured in `config/params.yaml`)

## Future Stages (Planned)

- **Data Preprocessing**: Tokenization and text cleaning
- **Model Training**: Fine-tuning BART/T5 models
- **Model Evaluation**: ROUGE score calculation
- **Model Export**: Saving trained models for inference

## License

MIT
