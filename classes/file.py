import os

class file_management:
    """ File Management Class. """
    @staticmethod
    def save(d = 'start_application'):
        # try to create storage directory
        try:
            os.mkdir('storage')
        # if file exists
        except FileExistsError: 
            # save state into file 
            with open('storage/user.log', 'w', encoding='utf-8') as state:
                state.write(d) # write user state into file
        
