
Passwords should not be stored as-is; this is a **HUGE** security risk.

Passwords should be hashed when stored on a server. When someone enters their password again, the one-way hash will be applied
to the password they input, and it should match the hashed password stored on the server.

Their password is not stored plain-text in the database, and they can still verify their password and login.

