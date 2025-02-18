# Start the API
uvicorn api.main:app --host localhost --port 8000 --reload





You can set the temperature for Llama 3.2 when running it locally with Ollama. Here's how you can do it:   

1. Create a Modelfile:

Create a text file named Modelfile (no extension).
Add the following lines to the file:
FROM llama3.2
PARAMETER temperature 0.7 
Replace 0.7 with your desired temperature value. A lower value (e.g., 0.2) makes the model more deterministic and focused, while a higher value (e.g., 0.9) makes it more creative and unpredictable.   
2. Create a Model:

Open your terminal and navigate to the directory where you saved the Modelfile.
Run the following command to create a new model with your custom temperature:
Bash

ollama create my-llama3.2 -f Modelfile
Replace my-llama3.2 with any name you want to give to your custom model.
3. Run the Model:

Now you can run your custom model with the specified temperature:
Bash

ollama run my-llama3.2