from InquirerPy import inquirer

class menu:
    """ Simple menu using InquirerPy package. """

    @staticmethod
    def text(message):
        """ prompt text menu """
        return inquirer.text(message=f"{message}").execute()

    @staticmethod
    def select(message, choices):
        """ prompt select menu """
        return inquirer.select(
            message=f"{message}",
                choices = choices
        ).execute()

    @staticmethod
    def confirm(message):
        """ prompt confirmation menu """
        return inquirer.confirm(message=f"{message}").execute()