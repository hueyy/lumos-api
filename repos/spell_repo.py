import uuid
from utils.utils import dict_to_list, object_to_dict
from models.triggers.trigger import create_trigger


class SpellRepo:
    def __init__(self, database):
        self.database = database

    def get_spells(self):
        spells = self.database.child('spells').get().val()
        return dict_to_list(spells)

    def get_spell_by_id(self, spell_id):
        spell = self.database.child('spells').child(spell_id).get().val()
        return spell

    def create_spell(self):
        spell_id = str(uuid.uuid4())
        spell = {
            "id": spell_id
        }
        self.database.child('spells').child(spell_id).set(spell)
        return spell

    def set_trigger(self, spell_id, trigger):
        trigger = object_to_dict(create_trigger(trigger))
        self.database.child('spells').child(spell_id).child('trigger').set(trigger)
        spell = self.get_spell_by_id(spell_id)
        return spell

    def set_action(self, spell_id, device_id, action):
        action_id = str(uuid.uuid4())
        action = {
            "id": action_id,
            "device_id": device_id,
            "action": action
        }
        self.database.child('spells').child(spell_id).child('actions').child(action_id).set(action)
        spell = self.get_spell_by_id(spell_id)
        return spell

    def remove_trigger(self, spell_id):  # there should be a more performant way to do this
        self.database.child('spells').child(spell_id).child('trigger').remove()
        spell = self.get_spell_by_id(spell_id)
        return spell

    def remove_action(self, spell_id, action_id):
        self.database.child('spells').child(spell_id).child('actions').child(action_id).remove()
        spell = self.get_spell_by_id(spell_id)
        return spell
