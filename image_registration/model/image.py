"""
some brief description about this class.
"""


class Image(object):

    def __init__(self, marker, regions, width, height, level):
        """

        :param marker:
        :type marker:

        :param regions:
        :type regions: a list of model.Region

        :param width:
        :type width:

        :param height:
        :type height:

        :param level:
        :type level:
        """
        self.marker = marker
        self.regions = regions
        self.width = width
        self.height = height
        self.level = level
