SESSION_HISTORY_KEY = 'last_viewed_notes'
SESSION_HISTORY_LIMIT = 20


def add_note_to_history(request, note_id):
    history = request.session.get(SESSION_HISTORY_KEY, [])
    note_id = int(note_id)

    if note_id in history:
        history.remove(note_id)

    history.insert(0, note_id)
    request.session[SESSION_HISTORY_KEY] = history[:SESSION_HISTORY_LIMIT]
    request.session.modified = True
