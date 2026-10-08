from fastapi import HTTPException


def get_book(id: int) -> dict:
    conn = None
    row = conn.execute("SELECT * FROM books WHERE id=?", (id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return dict(row)
