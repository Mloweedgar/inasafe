"""
InaSAFE Disaster risk assessment tool developed by AusAid - **Table**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.
"""

__author__ = 'marco@opengis.ch'
__revision__ = '$Format:%H$'
__date__ = '04/06/2013'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

from message_element import MessageElement
from exceptions import InvalidMessageItemError
from row import Row


class Table(MessageElement):
    """A class to model tables in the messaging system """

    def __init__(self, *args, **kwargs):
        """Creates a table object

        :param args: args can be list or Row
        :type args: list, row


        We pass the kwargs on to the base class so an exception is raised
        if invalid keywords were passed. See:

        http://stackoverflow.com/questions/13124961/
        how-to-pass-arguments-efficiently-kwargs-in-python
        """
        super(Table, self).__init__(**kwargs)
        self.caption = None
        self.rows = []

        for arg in args:
            self.add(arg)

    def add(self, item):
        """Add a row to the table.

        List can be passed and are automatically converted to Rows

        :param item: Item an element to add to the rows can be list or Row
            object
        :type item: row, list

        """
        if isinstance(item, list):
            self.rows.append(Row(item))
        elif isinstance(item, Row):
            self.rows.append(item)
        else:
            raise InvalidMessageItemError(item, item.__class__)

    def to_html(self):
        """Render a Table MessageElement as html

        :returns: The html representation of the Table MessageElement
        :rtype: basestring
        """
        table = '<table%s>\n' % self.html_attributes()
        if self.caption is not None:
            table += '<caption>%s</caption>\n' % self.caption
        table += '<tbody>\n'
        for row in self.rows:
            table += row.to_html()
        table += '</tbody>\n</table>\n'

        return table

    def to_text(self):
        """Render a Table MessageElement as plain text

        :returns: The text representation of the Table MessageElement
        :rtype: basestring
        """

        table = ''
        if self.caption is not None:
            table += '%s</caption>\n' % self.caption
        table += '\n'
        for row in self.rows:
            table += row.to_text()
        return table

    def to_markdown(self):
        """Render a Table queue as markdown

        :returns: Markdown representation of the Text Table.
        :rtype: str
        """
        raise NotImplementedError('Please Implement this method')

    def to_json(self):
        """Render a Table queue as JSON

        :returns: Json representation of the Text Table.
        :rtype: str
        """
        raise NotImplementedError('Please Implement this method')
