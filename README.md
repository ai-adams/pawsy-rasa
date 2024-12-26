# pawsy-rasa

```
# Train a new model
rasa train

# Test model
rasa shell

# Test model in debug mode
rasa shell --debug

# Test model in debug model and save log file
script ./logs/log.log rasa shell --debug

# Clean up log file after exiting shell
sed -i.bak 's/\x1b\[[0-9;]*m//g' ./logs/log.log
```

### Testing the Widget Locally:
1. use the ngrok to expose the port: `ngrok http 5005`
2. update the `server-url=<YOUR-NGROK-URL>` **and** set `rest-enabled="true"`
3. train the bot
4. start the bot with: `rasa run --enable-api --cors="*"`
5. start the action server: `rasa run actions`
6. open `index.html` in your browser and test the bot

