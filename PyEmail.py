"""
PyEmail is a fast, powerful, and easy-to-use open-source Email tool.
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP_SSL, SMTPServerDisconnected
from ssl import create_default_context
from typing import List, Optional


class Email:
    """Email

    The class saves basic Email information, including the title/subject
    and the Email body. Two types of Email bodies are allowed: plain
    text and HTML.

    This Email class also provides a property to convert all saved
    information to MIMEText and can be used to send out using Server
    instance.

    Attributes:
        subject: The subject is the introduction that identifies the
            intent of the Email.
        is_html: Whether or not the message is plain text or HTML.
        content: Representing an Email body.
    """

    def __init__(
        self,
        subject: str = "",
        *,
        text: Optional[str] = None,
        html: Optional[str] = None,
    ) -> None:
        """
        Either text or HTML must be passing in. If giving in both, then
        it will use HTML and drop text. If none, raise value error.

        Args:
            subject: The subject is the introduction that identifies the
                intent of the Email.
            text: Email body in plain text format.
            html: Email body in HTML format.
        """
        if (text is None and html is None) or (
            text is not None and html is not None
        ):
            raise ValueError(
                f"{self.__class__.__name__} takes one of 'text' or 'html'."
            )

        self.subject = subject
        self.is_html = html is not None
        self.content: str = html if self.is_html else text  # type: ignore

    @property
    def message(self) -> MIMEText:
        if self.is_html:
            return MIMEText(self.content, "html")
        return MIMEText(self.content, "plain")


class Server:
    """Server

    An SMTP server is used to send mail to any Internet machine with an
    SMTP or ESMTP listener daemon.

    Attributes:
        address: User's Email account.
        smtp: SMTP server's connection.
    """

    def __init__(
        self,
        email: str,
        password: str,
        server: str,
        port: Optional[int] = None,
        ttls: bool = True,
    ) -> None:
        """
        A computer system that sends and receives the Email.

        Args:
            email: User's Email account.
            password: Email account password.
            server: A computer with mail transfer agent (MTA) functions.
            port: The Simple Mail Transfer Protocol. Defaults to None.
            ttls: Tunneled Transport Layer Security. Defaults to True.
        """
        # save email address
        self.address = email

        # auto fill port number
        if port is None:
            port = 587 if ttls else 465

        # init smtp server
        self.smtp = SMTP_SSL(server, port, context=create_default_context())
        if ttls:
            self.smtp.starttls()

        # login into smtp server
        self.smtp.login(self.address, password)

    def __del__(self) -> None:
        self.quit()

    def __enter__(self) -> "Server":
        return self

    def __exit__(self, type, value, traceback) -> None:
        self.quit()

    def is_connected(self) -> bool:
        """Check connection status.

        Check if the server instance is still connected with the SMTP server.

        Returns:
            True if it is connected, otherwise false.
        """
        try:
            status = self.smtp.noop()[0]
        except SMTPServerDisconnected:
            return False
        return status == 250

    def quit(self) -> None:
        """Quit connection.

        Safely disconnected. Only when a connection exists.
        """
        if self.is_connected():
            self.smtp.quit()

    def send(
        self,
        email: Email,
        *,
        to: Optional[List[str]] = None,
        cc: Optional[List[str]] = None,
    ) -> None:
        """Send out Email.

        Messages are distributed by electronic means from one computer
        user to one or more recipients via a network.

        Args:
            email: The messages.
            to: Main recipients of the given Email. Defaults to None.
            cc: Carbon copy. Defaults to None.
        """
        if to is None:
            to = []
        if cc is None:
            cc = []

        # init email
        message = MIMEMultipart()

        # set email address
        message["From"] = self.address
        message["To"] = ", ".join(to)
        message["Cc"] = ", ".join(cc)

        # set email content
        message["Subject"] = email.subject
        message.attach(email.message)

        # send email
        self.smtp.sendmail(
            from_addr=self.address, to_addrs=to + cc, msg=message.as_string()
        )
