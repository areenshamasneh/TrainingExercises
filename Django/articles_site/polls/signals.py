from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import logging
from .models import Article

logger = logging.getLogger("polls.audit_log")


@receiver(post_save, sender=Article)
def audit_article_change(sender, instance, created, **kwargs):
    if created:
        logger.info(f"New article created: {instance.title}")
    else:
        logger.info(f"Article updated: {instance.title}")


@receiver(post_delete, sender=Article)
def audit_article_delete(sender, instance, **kwargs):
    logger.info(f"Article deleted: {instance.title}")
