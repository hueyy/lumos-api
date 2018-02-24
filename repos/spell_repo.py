import uuid
from utils.firebase import dict_to_list


class SpellRepo:
    def __init__(self, database):
        self.database = database

    def get_spells(self):
        spells = self.database.child('spells').get().val()
        return dict_to_list(spells)

    def get_spell_by_id(self, spell_id):
        spell = self.database.child('spells').child(spell_id).get().val()
        return spell

    def create_spell(self, trigger, devices):
        spell_id = uuid.uuid4()
        spell = {
            "id": spell_id,
            "trigger": trigger,
            "devices": devices
        }
        self.database.child('spells').child(spell_id).set(spell)
        return spell

    def remove_trigger(self, spell_id): # there should be a more performant way to do this
        self.database.child('spells').child(spell_id).child('trigger').remove()
        spell = self.get_spell_by_id(spell_id)
        return spell

    def remove_action(self, spell_id, action_id):
        self.database.child('spells').child(spell_id).child('actions').child(action_id).remove()
        spell = self.get_spell_by_id(spell_id)
        return spell

    def update_spell(self, spell):
        spell_id = spell.get('id')
        spell = self.database.child('spells').child(spell_id).set(spell)
        return spell