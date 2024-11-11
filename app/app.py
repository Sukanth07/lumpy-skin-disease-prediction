import gradio as gr
import utils
from predict import prediction
import warnings
from logger import get_logger

logger = get_logger(__name__)
warnings.filterwarnings("ignore")

utils.copy_builder()


def show_processing_text():
    return gr.update(visible=True), gr.update(visible=False)

def prediction_with_loading(image, longitude, latitude, cloud_cover, evapotranspiration, precipitation, min_temp, mean_temp, max_temp, vapour_pressure, wet_day_freq):
    try:
        logger.info("Starting prediction process...")
        response = prediction(
            image, longitude, latitude, cloud_cover, evapotranspiration,
            precipitation, min_temp, mean_temp, max_temp, vapour_pressure, wet_day_freq
        )
        logger.info("Prediction completed successfully.")
        return gr.update(value=response, visible=True), gr.update(visible=False)
    except Exception as e:
        logger.error(f"Error in prediction: {str(e)}")
        return "An error occurred during prediction. Please try again.", gr.update(visible=False)

with gr.Blocks(css=utils.css, theme=gr.themes.Ocean(primary_hue=gr.themes.colors.red, secondary_hue=gr.themes.colors.pink)) as demo:
    gr.Markdown("<div class='title'>LUMPY SKIN DISEASE PREDICTION</div>")
    
    with gr.Row():
        with gr.Column(scale=5):
            # Image upload
            image_input = gr.Image(type="pil", label="Upload Image", height=177)
        
        with gr.Column(scale=5):
            longitude = gr.Number(label="Longitude")
            latitude = gr.Number(label="Latitude")

    with gr.Row():
        with gr.Column(scale=5):
            cloud_cover = gr.Number(label="Monthly Cloud Cover")
            evapotranspiration = gr.Number(label="Potential EvapoTranspiration")
        
        with gr.Column(scale=5):
            precipitation = gr.Number(label="Precipitation")
            min_temp = gr.Number(label="Minimum Temperature")

        with gr.Column(scale=5):
            mean_temp = gr.Number(label="Mean Temperature")
            max_temp = gr.Number(label="Maximum Temperature")
        
        with gr.Column(scale=5):
            vapour_pressure = gr.Number(label="Vapour Pressure")
            wet_day_freq = gr.Number(label="Wet Day Frequency")

    with gr.Row():
        predict_button = gr.Button("Predict", variant="primary")
    
    processing_text = gr.Markdown("", visible=False, height=100)
    output_text = gr.Markdown(label="LLM Generated Diagnostic Report", container=True, show_copy_button=True, visible=False)

    predict_button.click(
        fn=show_processing_text,
        inputs=[],
        outputs=[processing_text, output_text],
        queue=False
    )
    predict_button.click(
        fn=prediction_with_loading,
        inputs=[image_input, longitude, latitude, cloud_cover, evapotranspiration, precipitation, min_temp, mean_temp, max_temp, vapour_pressure, wet_day_freq],
        outputs=[output_text, processing_text],
        queue=True
    )

demo.launch(share=True)
