"""
some description of what this package does.
"""
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

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
        self.regions = {}
        try:
            tree = ET.parse(config)
            root = tree.getroot()
            if root.tag != "Annotations":
                raise ParseError("Invalid root element `{}`!".format(root.tag))
            for annotation in root:
                if annotation.tag != "Annotation":
                    raise ParseError("Invalid child tag `{}`!".format(annotation.tag))
                regions = annotation.findall("Regions")
                if len(regions) != 1:
                    raise ParseError("Expect exactly one `Regions` element per `Annotation` element, found `{}` "
                                     "elements.".format(len(regions)))
                for region in regions[0].findall("Region"):
                    vertices = region.findall("Vertices")
                    if len(vertices) != 1:
                        raise ParseError("Expect exactly one `Vertices` element per `Region` element, found `{}` "
                                         "elements.".format(len(vertices)))
                    region_vertices = []
                    for vertex in vertices[0]:
                        for item in vertex.items():
                            if item[0].lower() == "x":
                                x = item[1]
                            if item[0].lower() == "y":
                                y = item[1]
                            if item[0].lower() == "z":
                                z = item[1]
                        try:
                            region_vertices.append(Vertex(x ,y, z))
                        except NameError:
                            raise ParseError("The vertex `{}` does not have X and/or Y coordinate(s)".format(vertex.items()))

        except ImportError:
            raise
        except ParseError as e:
            raise ParseError("Invalid configuration at `{}`: {} -- unable to continue.".format(config, e.message))

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