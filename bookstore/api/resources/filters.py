

def search_normalize(title = None,
                    author = None,
                    category = None,
                    limit = 30,
                    offset = 0, **data):
    if title and author:
        return {
            "title": title,
            "author": author,
            "limit": limit,
            "offset": offset
        }
    
    
    elif title:
        return {
            "title": title,
            "limit": limit,
            "offset": offset
            }
    
    elif author:
        return {
            "author": author,
            "limit": limit,
            "offset": offset
            }

    else:
        return {
            "category": category,
            "limit": limit,
            "offset": offset
            }


catg_consult = "SELECT * FROM books WHERE (category = ?) \
                    LIMIT ?  OFFSET ?"



title_consult = "SELECT * FROM books WHERE (title LIKE ?)\
                    LIMIT ?  OFFSET ?"



author_consult = "SELECT * FROM books WHERE (author LIKE ?) \
                    LIMIT ?  OFFSET ?"

author_title_consult = "SELECT * FROM books WHERE (title LIKE ?)\
                           AND (author LIKE ?) LIMIT ? OFFSET ?"