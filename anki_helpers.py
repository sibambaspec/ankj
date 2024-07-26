import os
from anki.storage import Collection

# Path to Anki's collection
ANKI_COLLECTION_PATH = os.path.expanduser("~/Anki2/User 1/collection.anki2")

def open_collection():
    return Collection(ANKI_COLLECTION_PATH)

def add_card(deck_name, front, back):
    col = open_collection()
    
    # Get the deck ID
    did = col.decks.id(deck_name)
    
    # Get the model
    model = col.models.byName("Basic")
    
    # Create a new note
    note = col.newNote()
    note.model()['did'] = did
    note.model()['mid'] = model['id']
    
    # Add fields to the note
    note.fields[0] = front
    note.fields[1] = back
    
    # Add the note to the collection
    col.addNote(note)
    
    # Save changes and close collection
    col.save()
    col.close()

    return note.id
