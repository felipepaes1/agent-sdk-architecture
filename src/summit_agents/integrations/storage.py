from agents import SQLiteSession


def build_session(session_id: str | None) -> SQLiteSession | None:
    if not session_id:
        return None

    return SQLiteSession(session_id)
