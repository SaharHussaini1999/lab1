from db_connect import connect


# 2 - user should enter his/her username
def get_or_create_user(username):
    conn = connect()
    cur = conn.cursor()

    # Check if user exists
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        # Create new user
        cur.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

# 3 - get user's last level


def get_latest_level(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT level FROM user_score
        WHERE user_id = %s
        ORDER BY saved_at DESC
        LIMIT 1
    """, (user_id,))

    result = cur.fetchone()
    cur.close()
    conn.close()

    return result[0] if result else 1  # Default to level 1

# save game state


def save_score(user_id, level, score):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO user_score (user_id, level, score)
        VALUES (%s, %s, %s)
    """, (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()
