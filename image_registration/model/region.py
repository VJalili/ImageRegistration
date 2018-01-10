"""
TODO: a brief description of region
"""
import sys
from pixel import *
from vertex import *


class Region(object):
    def __init__(self, id=None):
        """
        TODO
        :param id:
        """
        self.id = id
        self.region = None
        self.bounding_region = None
        self.pixels = None

    def _get_width_and_height(self, vertices):
        # Determine the upper-level corner of the rectangle from the list of vertices.
        ul = Vertex(x=sys.maxint, y=sys.maxint, z=sys.maxint)
        for vertex in vertices:
            if vertex.x < ul.x and vertex.y < ul.y:
                ul.x = vertex.x
                ul.y = vertex.y

        # Determine the upper-right corner of the rectangle from the list of vertices.
        ur = Vertex(x=0, y=sys.maxint, z=sys.maxint)
        for vertex in vertices:
            if vertex.x > ur.x and vertex.y < ur.y:
                ur.x = vertex.x
                ur.y = vertex.y

        # Determine the lower-left corner of the rectangle from a the list of vertices.
        ll = Vertex(x=sys.maxint, y=0, z=sys.maxint)
        for vertex in vertices:
            if vertex.x < ll.x and vertex.y > ll.y:
                ll.x = vertex.x
                ll.y = vertex.y

        # Determine the lower-right corner of the rectangle from a the list of vertices.
        lr = Vertex(x=0, y=0, z=sys.maxint)
        for vertex in vertices:
            if vertex.x > lr.x and vertex.y > lr.y:
                lr.x = vertex.x
                lr.y = vertex.y

        return ur.x - ul.x, ll.y-ul.y

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
        w, h = self._get_width_and_height(vertices)
        self.pixels = [[Pixel(0, 0, 0) for x in range(w)] for y in range(h)]

    def set_pixel(self, x, y, pixel):
        """
        Sets the pixel of this region at x and y to pixel.
        :param x: x position on the image (should be within the boundary of bounding region.
        :type x: integer

        :param y: y position on the image (should be within the boundary of bounding region.
        :type y: integer

        :param pixel: the new pixel value.
        :type pixel: model.Pixel

        :return: void
        """
        self.pixels[x][y] = pixel


