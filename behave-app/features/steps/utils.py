# -*- coding: utf-8 -*-

"""
Utils
"""

from page_objects import page_objects_dict


def get_page_object(element):
    """Checks has 'element' been defined in page_objects.

    :param str element: element to be checked
    """
    if element in page_objects_dict:
        return page_objects_dict[element]
    else:
        message = "Element '{}' not defined in page_objects"
        assert False, message.format(element)
