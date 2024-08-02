import sqlite3
import os
import win32crypt

def get_chrome_passwords():
    """
    Get saved passwords from Google Chrome's database.
    """
    # Path to the Google Chrome login data file
    chrome_login_db = os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Login Data')
    conn = sqlite3.connect(chrome_login_db)
    cursor = conn.cursor()
    cursor.execute('SELECT origin_url, action_url, username_value, password_value FROM logins')

    passwords = []
    for row in cursor.fetchall():
        url, action_url, username, password = row
        password = win32crypt.CryptUnprotectData(password, None, None, None, 0)[1].decode()
        passwords.append((url, username, password))

    conn.close()
    return passwords

def main():
    passwords = get_chrome_passwords()
    if passwords:
        print("Saved passwords:")
        for url, username, password in passwords:
            print(f"URL: {url}")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print("-" * 40)
    else:
        print("No passwords found.")

if __name__ == '__main__':
    main()
