from IPython.display import display
from IPython.display import Markdown

# Call the model and print the response.
gemini = genai.GenerativeModel(model_name=model)

response = gemini.generate_content(
    contents,
    generation_config=generation_config,
    safety_settings=safety_settings,
    stream=stream,
)

display(Markdown(response.text))
