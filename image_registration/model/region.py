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

    def set_region(self, vertices):
        """
        Sets the region for image registration.
        :param vertices:
        :type vertices: a list of model.Vertex

        :return:
        """
        self.region = vertices

    def set_bounding_region(self, vertices):
        """
        Sets the bounding region for image registration
        :param vertices:
        :type vertices:

        :return:
        """
        self.bounding_region = vertices
