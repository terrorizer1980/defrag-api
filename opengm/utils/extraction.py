from pyrogram.types import Message
from pyrogram import Client
from opengm.utils.commands import get_args
from pyrogram.types import MessageEntity 
# Extract ID from reply
def id_from_reply(message: Message):
    if message.reply_to_message:
        return message.reply_to_message.from_user.id
    else:
        return None

def extract_user_and_text(msg: Message):
    prev_msg = msg.reply_to_message
    split_text = msg.text.split(None, 1)

    if len(split_text) < 2:
        return id_from_reply(msg)

    text_to_parse = split_text[1]
    text = ""
    # parse message entities
    entities = list(msg.entities)
    # Sort out everything not a mention from list
    print(entities)
    entity_list = []
    for entity in entities:
        if entity.type == "text_mention":
            entity_list.append(entity)
    if len(entities) > 0:
        ent = entities[0]
    else:
        ent = None

    if entities and ent != None and ent.offset == len(msg.text) - len(text_to_parse):
        print("Heyho!")
    return 0
