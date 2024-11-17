import joblib
import numpy as np
import tensorflow as tf
from src.llm import LLM
from src.config import *
from src.exception import log_exception, ModelLoadingError, PreprocessingError, PredictionError
from src.logger import get_logger

logger = get_logger(__name__)

class DataPreprocessor:
    def __init__(self):
        try:
            self.scaler = joblib.load(f"{MODELS_DIR}/scaler_object.joblib")
            logger.info("DataPreprocessor initialized with scaler.")
        except Exception as e:
            log_exception(e, "Error loading scaler in DataPreprocessor.")
            raise ModelLoadingError("Could not load the scaler for data preprocessing.") from e

    def preprocess(self, input_data):
        try:
            scaled_data = self.scaler.transform(np.array(input_data).reshape(1, -1))
            logger.info("Data preprocessing completed successfully.")
            return scaled_data
        except Exception as e:
            log_exception(e, "Error in preprocessing data in DataPreprocessor.")
            raise PreprocessingError("Preprocessing failed. Ensure input data format is correct.") from e


class ML_Model_Predictor:
    def __init__(self):
        try:
            self.model = joblib.load(f"{MODELS_DIR}/randomforest_best_model.pkl")
            logger.info("ML model loaded successfully.")
        except Exception as e:
            log_exception(e, "Failed to load ML model in ML_Model_Predictor.")
            raise ModelLoadingError("Could not load ML model. Please check model path and format.") from e

    def predict(self, preprocessed_data):
        try:
            prediction = self.model.predict(preprocessed_data)
            logger.info("ML model prediction completed successfully.")
            return prediction[0]
        except Exception as e:
            log_exception(e, "Error during ML model prediction in ML_Model_Predictor.")
            raise PredictionError("Prediction failed. Ensure input data format is correct.") from e


class CNN_Model_Predictor:
    def __init__(self):
        try:
            self.model = tf.keras.models.load_model(f"{MODELS_DIR}/mobilenet_lumpy_skin_model.h5")
            logger.info("CNN model loaded successfully.")
        except Exception as e:
            log_exception(e, "Failed to load CNN model in CNN_Model_Predictor.")
            raise ModelLoadingError("Could not load CNN model. Please check model path and format.") from e

    def predict(self, image):
        try:
            image = image.resize((224, 224))
            image_array = np.array(image) / 255.0
            image_array = np.expand_dims(image_array, axis=0)
            image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
            prediction = self.model.predict(image_array)
            logger.info("CNN model prediction completed successfully.")
            return np.argmax(prediction, axis=1)[0]
        except Exception as e:
            log_exception(e, "Error during CNN model prediction in CNN_Model_Predictor.")
            raise PredictionError("CNN prediction failed. Check image input format.") from e


def prediction(image, longitude, latitude, cloud_cover, evapotranspiration, precipitation, min_temp, mean_temp, max_temp, vapour_pressure, wet_day_freq):
    try:
        # Initialize classes
        preprocessor = DataPreprocessor()
        ml_predictor = ML_Model_Predictor()
        cnn_predictor = CNN_Model_Predictor()
        llm = LLM()
        
        # Prepare structured data input for ML model
        structured_data = [longitude, latitude, cloud_cover, evapotranspiration, precipitation, min_temp, mean_temp, max_temp, vapour_pressure, wet_day_freq]
        preprocessed_data = preprocessor.preprocess(structured_data)
        
        # Get predictions from ML and CNN models
        ml_prediction = ml_predictor.predict(preprocessed_data)
        cnn_prediction = cnn_predictor.predict(image)
    
        result = f"""
        Lumpy Skin Disease Diagnostic Report:
        
        **ML Model Prediction:** {'Lumpy' if ml_prediction == 1 else 'Not Lumpy'}
        **CNN Model Prediction:** {'Lumpy' if cnn_prediction == 1 else 'Not Lumpy'}
        
        **Input Data:**
        - Longitude: {longitude}
        - Latitude: {latitude}
        - Monthly Cloud Cover: {cloud_cover}
        - Potential EvapoTranspiration: {evapotranspiration}
        - Precipitation: {precipitation}
        - Minimum Temperature: {min_temp}
        - Mean Temperature: {mean_temp}
        - Maximum Temperature: {max_temp}
        - Vapour Pressure: {vapour_pressure}
        - Wet Day Frequency: {wet_day_freq}
        """

        # Generate LLM report
        report = llm.inference(image=image, result=result)
        logger.info("LLM report generated successfully.")
        return report
    
    except Exception as e:
        log_exception(e, "Error in prediction function.")
        raise PredictionError("Prediction function encountered an error. Check inputs and model paths.") from e
