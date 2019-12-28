
##Here we will use the user defined templates for inserting it to the html pages with the {{ test| cut}}

from django import template

register=template.Library()


@register.filter(name='cut')
def cut(value,arg):

    """
    It will remove all the args from the values
    """

    return value.replace(arg,' ')
