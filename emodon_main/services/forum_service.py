# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/services/forum_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _

from ..models import Forum

class ForumService:
 # CRUD methods for Forum models
    @staticmethod
    def get_mood_choices():      
        return [({'key': label, 'value': value}) for label, value in Forum.MOOD_CHOICE]
    
    # Retrieve all Forum objects ordered by creation date.
    @staticmethod
    def read_forum_list():

        return Forum.objects.all().order_by('-created_at')


    """
    Create a new Forum object with the given mood_choice.

    Returns:
        tuple: (success: bool, data: dict, message: str)
    """
    @staticmethod
    def create_forum(mood_choice):
        try:
            if not mood_choice:
                return False, None, _("Mood choice is required.")

            # Create a new Forum object
            new_forum = Forum(title=mood_choice)
            new_forum.save()
            return True, new_forum, _("Your forum has been successfully created.")
        
        # Capture validation errors and return them
        except ValidationError as ve:
            validator_error_message = _("Validation error: %(errors)s") % {"errors" :' '.join(ve.messages)}
            return False, None, validator_error_message

        # Capture all possible errors
        except Exception as e:
            error_message = _("A problem occurred: %(errors)s") % {"errors" :str(e)}
            return False, None, error_message
        

    # Retrieve a single Forum object by its primary key (pk).
    @staticmethod
    def get_forum_by_id(pk):

        try:
            forum = Forum.objects.get(pk=pk) 
            return forum, _("Forum has been found.")
        
        except ObjectDoesNotExist:
            return None, _("No forum was found.")
    

    # Retrieve a single Forum object by its primary key (pk) before deleting it.
    @staticmethod
    def delete_forum(pk):
        try:
            forum = Forum.objects.get(pk=pk)  
            forum.delete()
            return True, _("Forum has been successfully deleted.")
        
        except ObjectDoesNotExist:
            return False, _("No forum was found.")
        
        except Exception as e:
            error_message = _("A problem occured: %(errors)s") % {"errors" : str(e)}
            return False, error_message
