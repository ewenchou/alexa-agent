from alexa_agent import AlexaAgent


def main():
    agent = AlexaAgent()
    agent.wakeup()
    agent.ask(["What is today's date", "How's the weather"])


if __name__ == '__main__':
    main()
