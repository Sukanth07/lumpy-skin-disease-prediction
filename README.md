# Lumpy Skin Disease Prediction System

This project is an AI-based diagnostic system for detecting Lumpy Skin Disease in animals using Machine Learning (ML), Convolutional Neural Networks (CNN), and Large Language Model (LLM) integration. The system allows users to upload images and provide various input features, after which the model analyzes the data and provides a detailed report.

---

## Project Screenshot

![Project Screenshot](screenshots\Screenshot(69).png)

---

## Project Structure (Inside 'app' Directory)

- **app.py** - Main Gradio app script for the user interface.
- **predict.py** - Contains the prediction logic and interacts with both ML and CNN models.
- **llm.py** - Utilizes the LLM to generate detailed diagnostic reports.
- **config.py** - Configuration file with paths and environment variables.
- **utils.py** - Contains other utility functions and properties.
- **exception.py** - Custom exception handling for various error scenarios.
- **logger.py** - Configures logging across the application.

---

## Setup Instructions

### Prerequisites
- Python 3.10
- Virtual environment (recommended)
- `pip` package manager

### Install Dependencies

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Sukanth07/lumpy-skin-disease-prediction.git
    cd lumpy-skin-disease-prediction
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    .\venv\Scripts\activate  # For Windows
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables**:
    Create a `.env` file with your API keys and other sensitive data:
    ```
    GEMINI_API_KEY=your-gemini-api-key
    ```
    You can get the free Gemini API key with this link: https://aistudio.google.com/app/apikey

---

## Usage

### Change to App Directory
```bash
cd app
```

### Running the Gradio App
Start the Gradio app by running the following command:
```bash
python app.py
```

To continuosly run and update the app, use the following command:
```bash
gradio app.py
```

The app will launch in your default browser. You can upload images and provide additional input data to get a comprehensive diagnostic report.

---

## Core Functionality
- **Machine Learning Prediction** - Predicts the presence of Lumpy Skin Disease based on structured input data.
- **CNN Image Analysis** - Analyzes images to classify them as 'Lumpy' or 'Not Lumpy'.
- **LLM Diagnostic Report** - Uses a language model to generate a detailed report based on model predictions and input data.

---

## Project Components

1. **app.py**
   - Main entry point for the Gradio UI.
   - Displays input fields, image upload options, and prediction results.

2. **predict.py**
   - Implements the `DataPreprocessor`, `ML_Model_Predictor`, and `CNN_Model_Predictor` classes.
   - Orchestrates data preprocessing, model prediction, and combines outputs for the LLM report generation.

3. **llm.py**
   - Responsible for configuring and generating predictions using the LLM.
   - Formats the results in a user-friendly diagnostic report.

4. **logger.py**
   - Sets up logging configurations for the project.
   - Ensures that logs are stored in `logs/app.log` with error level and timestamps.

5. **exception.py**
   - Contains custom exceptions for model loading, preprocessing, and inference.
   - Includes a utility function `log_exception` to standardize error logging.

---

## Exception Handling and Logging

- **Logging**: All logs are recorded in `logs/app.log` with timestamps and log levels.

- **Custom Exceptions**: The project uses `exception.py` to handle specific errors, such as:
    - `ModelLoadingError`: Raised when a model fails to load.
    - `PreprocessingError`: Raised during data preprocessing issues.
    - `PredictionError`: Raised for issues in the ML or CNN prediction processes.
    - `APIError`: Raised when the LLM API encounters an error.

---

## Commands

- **Run App**:
    ```bash
    python app.py
    ```

- **Install Packages**:
    ```bash
    pip install -r requirements.txt
    ```

- **Deactivate Virtual Environment**:
    ```bash
    deactivate
    ```

---

## Future Improvements

- **Model Optimization**: Further enhance ML and CNN models for faster predictions.

- **LLM Fine-tuning**: Use domain-specific data to improve the LLM's understanding of Lumpy Skin Disease.

- **Expanded Input**: Integrate more diverse data inputs for robust analysis.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Contributors

- **Sukanth K** - [github.com/Sukanth07](https://github.com/Sukanth07)
