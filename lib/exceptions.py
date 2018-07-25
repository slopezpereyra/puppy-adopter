class DownloadingError (Exception):
        """Baseclass for all exceptions related to the downloading process."""

        def __init__(self):
            pass


class ImageAlreadyDownloaded(DownloadingError):

    def __init__(self, url):
        self.url = url

    def __str__(self):
        error_string = ("""The found URL {} corresponds to an image already downloaded
                        to this environment. Seeking new image...""".format(self.url))

        return "\n" + error_string


class EnvironmentError(Exception):
    """Baseclass for all exceptions related to environments."""

    def __init__(self):
        pass


class NoEnvironmentFound(EnvironmentError):

    def __init__(self):
        pass

    def __str__(self):

        error_string = """No environments were found."""

        return "\n" + error_string
