# Alexa Agent

An agent for interacting with Amazon Alexa using text instead of voice. 

## Examples

The agent class has two main methods for interacting with Alexa Voice Service.

1. Tell Alexa to Say Something

```
from alexa_agent import AlexaAgent

alexa = AlexaAgent()
alexa.say("Hello World")
```

2. Tell Alexa to Do Something

```
from alexa_agent import AlexaAgent

alexa = AlexaAgent()

# Single command
alexa.ask("What time is it")

# Multiple commands, sent concurrently to Alexa
alexa.ask(["What is today's date", "How is the weather in San Francisco"])
```

For more ideas on how to use it, please read my [blog post](https://ewenchou.github.io/blog/2016/10/16/putting-it-all-together/).

## Requirements

Alexa Agent uses the modules below. Please follow the instructions in the README file for each one to install and configure.

* [alexa-client](https://github.com/ewenchou/alexa-client)
* [simple-tts](https://github.com/ewenchou/simple-tts)

## Installation

```
git clone https://github.com/ewenchou/alexa-agent.git
cd alexa-agent
sudo python setup.py install
```