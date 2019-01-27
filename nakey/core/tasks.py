from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from django.conf import settings

logger = get_task_logger(__name__)


@shared_task(default_retry_delay=2 * 60, max_retries=2)
def email(to, subject, message, pdf=None):
    """
    Sends email to user/users. 'to' parameter must be a string or list.
    """
    from nakey.utils.string_utils import valid_email
    try:
        if not isinstance(to, list):
            to = [to]
        email_list = list(filter(lambda email: valid_email(email), to))
        msg = EmailMessage(subject, message, from_email=settings.FROM_EMAIL, to=email_list)
        msg.content_subtype = "html"
        msg.send()
    except Exception as exc:
        logger.error((u'''Failed to send email,
            to={0}, subject={1}, message={2}, with exception={3}''').format(
            to, subject, message, str(exc)))
        raise email.retry(exc=exc)
