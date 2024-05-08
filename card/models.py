from django.db import models
from fernet_fields import EncryptedCharField
import hashlib
import uuid

class Card(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    hash_id = models.CharField(max_length=36, primary_key=True, editable=False, unique=True)
    card_number = EncryptedCharField(max_length=16)

    def save(self, *args, **kwargs):
        self.id = hashlib.sha256(self.card_number.encode()).hexdigest()
        super(Card, self).save(*args, **kwargs)