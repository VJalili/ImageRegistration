"""
TODO: a brief description of region
"""


class Region(object):
    def __init__(self, id=None):
        """
        TODO
        :param id:
        """
        self.id = id
        self.region = None
        self.bounding_region = None

    def set_region(self, region):
        """
        Sets the region for image registration.
        :param region:
        :type region: model.Rectangle

        :return:
        """
        self.region = region

    def set_bounding_region(self, region):
        """
        Sets the bounding region for image registration
        :param region:
        :type region:

        :return:
        """
        self.bounding_region = region
