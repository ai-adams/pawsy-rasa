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

