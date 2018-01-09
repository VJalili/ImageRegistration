"""
some description of what this package does.
"""


class ImageRegistration(object):
    def __init__(self, config, nuclei_file):
        """
        a brief description goes here ...
        :param config:
        :type config:

        :param nuclei_file:
        :type nuclei_file:
        """
        self._parse_config_xml(config)
        self._nuclei_file = nuclei_file

    def _parse_config_xml(self, config):
        """

        :param config:
        :type config:

        :return: void
        """
        print "in xml parse"

    def analyze(self, image_file, channel):
        """
        function description goes here ...
        :param image_file: what is an image file ?
        :type image_file: what is the type, e.g., string ? File?

        :param channel: what is a channel ?
        :type channel:

        :return: what does this function return ?
        """
        print "another thing"