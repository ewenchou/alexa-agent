from alexa_agent import AlexaAgent


def main():
    agent = AlexaAgent()
    agent.wakeup()
    agent.ask("What time is it?")


if __name__ == '__main__':
    main()
