from django.dispatch import Signal

user_logged_in = Signal()

# Typically followed by `user_logged_in` (unless, e-mail verification kicks in)
user_signed_up = Signal()

password_set = Signal()
password_changed = Signal()
password_reset = Signal()

email_confirmed = Signal()
email_confirmation_sent = Signal()

email_changed = Signal()
email_added = Signal()
email_removed = Signal()
