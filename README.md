# Pawsy Assistant for Pet Portal AI

Pawsy is a conversational AI chatbot designed to assist users on the Pet Portal AI platform. Built with Rasa Open Source, Pawsy helps potential pet owners find the perfect dog breeds based on their preferences, offers guidance on pet care, and answers common questions about pet parenting. This repository provides everything needed to develop, train, and test the Pawsy chatbot locally.



## Key Features

- **Personalized Dog Breed Recommendations**: Tailors breed suggestions to user preferences such as lifestyle, home type, and climate.
- **Pet Parenting Guidance**: Answers questions about pet care, behavior, and adoption processes.
- **Seamless Integration**: Includes a widget for local testing with options to connect the chatbot to the Pet Portal AI interface.



## Installation and Setup

### Install Rasa and Dependencies

```bash
pip install uv
uv pip install -r requirements.txt
```



### Train a New Model

```bash
rasa train
```



### Test the Model in Shell

```bash
rasa shell
```



### Debug the Model

Run the model in debug mode to view detailed logs:

```bash
rasa shell --debug
```



### Debug and Save Logs

To run the model in debug mode and save the output to a log file:

```bash
script ./logs/log.log rasa shell --debug
```

After exiting the shell, clean up log files to remove unwanted characters:

```bash
sed -i.bak 's/\x1b\[[0-9;]*m//g' ./logs/log.log
```



## Testing the Widget Locally

Follow these steps to test the chatbot widget in your browser:

1. **Expose the Port with Ngrok**: Use ngrok to expose the port:

   ```bash
   ngrok http 5005
   ```

2. **Update the Widget Settings**: Set the `server-url=<YOUR-NGROK-URL>` and ensure `rest-enabled="true"` is configured in your widget settings.

3. **Train the Bot**: Train the model:

   ```bash
   rasa train
   ```

4. **Start the Rasa API Server**: Run the Rasa server with CORS enabled:

   ```bash
   rasa run --enable-api --cors="*"
   ```

5. **Start the Action Server**: Run the custom action server:

   ```bash
   rasa run actions
   ```

6. **Test the Widget**: Open `index.html` in your browser to test the chatbot widget.

