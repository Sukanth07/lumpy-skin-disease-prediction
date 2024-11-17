from src.exception import log_exception, APIError
import google.generativeai as genai
from src.config import *
from src.logger import get_logger

logger = get_logger(__name__)

class LLM:
    def __init__(self):
        try:
            # Configure and initialize the Generative AI model
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel(GEMINI_MODEL_NAME)
            logger.info("LLM model initialized successfully.")
        except Exception as e:
            log_exception(e, "Failed to initialize the LLM model in LLM class.")
            raise APIError("Error initializing LLM model. Check API key and model name.") from e

    def prompt_template(self, result):
        # Generates a structured prompt for the LLM based on the provided data
        prompt = f"""You are a medical assistant with expertise in diagnosing and explaining Lumpy Skin Disease in animals. Based on provided data, generate a detailed report covering the following sections:

- Prediction Output: State if the case is classified as 'Lumpy' or 'Not Lumpy'.
- Key Observations: Summarize important symptoms and indicators.
- Cause Analysis: Explain the main reasons contributing to the prediction.
- Precautions & Solutions: Suggest any preventive measures and potential treatments for the condition.

Instructions: Carefully analyze the provided image, input data, and ML model predictions to generate a clear and comprehensive report.

Input Data:
{result}

Output Report:
- Prediction Output: Provide the final classification as **Lumpy** or **Not Lumpy** based on your analysis.
  
- Key Observations: List the notable symptoms from the image and input data that influenced the classification.

- Cause Analysis: Explain the likely cause(s) contributing to this prediction, highlighting specific symptoms or environmental factors.

- Precautions & Solutions: Outline preventive measures to avoid the spread of Lumpy Skin Disease, and suggest any possible treatments or care strategies to manage the condition.

"""
        return prompt

    def inference(self, image, result):
        try:
            # Prepare and send the request to the LLM model
            refined_prompt = self.prompt_template(result)
            prompt = [{'role': 'user', 'parts': [image, refined_prompt]}]
            
            response = self.model.generate_content(prompt)

            if response.text:
                logger.info("LLM inference successful.")
                return response.text
            else:
                logger.warning("LLM did not return any text.")
                raise APIError("LLM response is empty. Please check input format and prompt.")

        except Exception as e:
            log_exception(e, "Error during LLM inference in LLM class.")
            raise APIError("Error during LLM inference. Check input data and model configuration.") from e
