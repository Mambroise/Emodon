# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/services/forum_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.core.exceptions import ValidationError,ObjectDoesNotExist

from ..models import Forum

class ForumService:
 # CRUD methods for Forum models
    @staticmethod
    def get_mood_choices():      
        return [({'key': label, 'value': value}) for label, value in Forum.MOOD_CHOICE]
    
    @staticmethod
    def read_forum_list():

        # Retrieve all Forum objects ordered by creation date.
        return Forum.objects.all().order_by('-created_at')


    @staticmethod
    def create_forum(mood_choice):
        """
        Create a new Forum object with the given mood_choice.

        Returns:
            tuple: (success: bool, data: dict, message: str)
        """
        try:
            if not mood_choice:
                return False, None, "Mood choice is required."

            # Create a new Forum object
            new_forum = Forum(title=mood_choice)
            new_forum.save()
            return True, new_forum, "Your forum has been successfully created."
        
        except ValidationError as ve:
            # Capture validation errors and return them
            return False, None, f"Validation error: {', '.join(ve.messages)}"
            # Capture all possible errors
        except Exception as e:
            return False, None, f"A problem occurred: {str(e)}"
        

    @staticmethod
    def get_forum_by_id(pk):

        # Retrieve a single Forum object by its primary key (pk).
        try:
            forum = Forum.objects.get(pk=pk) 
            return forum, "Forum has been found."
        
        except ObjectDoesNotExist:
            return None, "No forum was found."
    

    @staticmethod
    def delete_forum(pk):
        # Retrieve a single Forum object by its primary key (pk) before deleting it.
        try:
            forum = Forum.objects.get(pk=pk)  
            forum.delete()
            return True, "Forum has been successfully deleted."
        
        except ObjectDoesNotExist:
            return False, "No forum was found."
        
        except Exception as e:
            return False, f"A problem occured: {str(e)}"
