# ---------------------------------------------------------------------------
#                           E m o D o n   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : emodon_main/services/reaction_service.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.core.exceptions import ObjectDoesNotExist,ValidationError
from django.utils.translation import gettext_lazy as _

from ..models import Reaction,Forum,Emoji

class ReactionService:
# CRUD methods for Forum models
    @staticmethod
    def get_emoji_choices():
        return Emoji.objects.all()
    
    # Retrieve all reactions objects for a same forum ordered by creation date.
    @staticmethod
    def get_reactions_by_forum_id(forum_pk):
        try:
            forum = Forum.objects.get(pk=forum_pk)
            reactions = Reaction.objects.filter(forum=forum).order_by('-created_at')
            return reactions, _("reactions list may be empty.")
        except Exception as e:
            return None, _("A problem occurred: %(errors)s") % {'errors': str(e)}
        
    @staticmethod
    def create_reaction(emoji_id,position_x,position_y,forum_pk):
        try:
            forum = Forum.objects.get(pk=forum_pk)
            emoji = Emoji.objects.get(pk=emoji_id)
            # Create a new reaction object
            new_reaction = Reaction(icon=emoji,position_x=position_x,position_y=position_y,forum=forum)
            print('okokokokokok')
            new_reaction.save()
    
            return True, new_reaction, _('Reaction successfully created')
        
        # Capture validation errors and return them
        except ValidationError as ve:
            validator_error_message = _("Validation error: %(errors)s") % {"errors" :' '.join(ve.messages)}
            return False, None, validator_error_message
        
        # Capture all possible errors
        except Exception as e:
            error_message =  _('A problem occured: %(errors)s') % {'errors' : str(e)}
            return False, None, error_message
        
    # Retrieve a single Forum object by its primary key (pk) before deleting it.
    @staticmethod
    def delete_reaction(pk):
        try:
            reaction = Reaction.objects.get(pk=pk)  
            reaction.delete()
            return True, _("Reaction has been successfully deleted.")
        
        except ObjectDoesNotExist:
            return False, _("No Reaction found.")
        
        except Exception as e:
            error_message = _("A problem occured: %(errors)s") % {"errors" : str(e)}
            return False, error_message
