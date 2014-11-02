# coding=utf-8
"""This module contains the abstract class of the MinimumNeeds. The storage
logic is omitted here."""

__author__ = 'Christian Christelis <christian@kartoza.com>'
__date__ = '05/10/2014'
__copyright__ = ('Copyright 2014, Australia Indonesia Facility for '
                 'Disaster Reduction')

from collections import OrderedDict
import json
from safe.common.utilities import ugettext as tr


class MinimumNeeds(object):
    """A abstract class for handling the minimum needs.

    The persistence logic is excluded from this class.
    """

    def get_need(self, resource):
        """Get a resource from the minimum_needs.

        :param resource: The resource name
        :type resource: basestring

        :returns: resource needed.
        :rtype: dict, None
        """
        for need in self.minimum_needs:
            if need['name'] == resource:
                return need
        return None

    def get_minimum_needs(self):
        """Get the minimum needed information about the minimum needs.

        That is the resource and the amount.

        :returns: minimum needs
        :rtype: OrderedDict
        """
        minimum_needs = OrderedDict()
        for resource in self.minimum_needs['resources']:
            if resource['Unit abbreviation']:
                name = '%s [%s]' % (
                    tr(resource['Resource name']),
                    resource['Unit abbreviation']
                )
            else:
                name = tr(resource['Resource name'])
            amount = resource['Default']
            minimum_needs[name] = amount
        return OrderedDict(minimum_needs)

    def get_full_needs(self):
        """The full list of minimum needs with all fields.


        :returns: minimum needs
        :rtype: dict
        """
        return self.minimum_needs

    def set_need(
            self, resource, amount, units,
            frequency='weekly', provenance=''):
        """Append a single new minimum need entry to the list.

        :param resource: Minimum need resource name.
        :type resource: basestring

        :param amount: Amount per person per time interval
        :type amount: int, float

        :param units: The unit that the resource is measured in.
        :type: basestring

        :param frequency: How regularly the unit needs to be dispatched
        :type: basestring  # maybe at some point fix this to a selection.

        :param provenance: Additional information about where this
        information is obtained and what it relates to.
        :type: basestring
        """
        self.minimum_needs['resources'].append({
            'resource': resource,
            'amount': amount,
            'unit': units,
            'frequency': frequency,
            'provenance': provenance,
        })

    def update_minimum_needs(self, minimum_needs):
        """Overwrite the internal minimum needs with new needs.

         Validate the new minimum needs. If ok, set these as the internal
         minimum needs.

        :param minimum_needs: The new minimum
        :type minimum_needs: dict

        :return: Returns success code, -1 for failure, 0 for success.
        :rtype: int
        """
        if type(minimum_needs) != dict:
            return -1

        # noinspection PyAttributeOutsideInit
        self.minimum_needs = minimum_needs
        return 0

    @staticmethod
    def _defaults():
        """Helper to get the default minimum needs.

        .. note:: Key names will be translated.
        """
        rice = 'Rice'
        drinking_water = 'Drinking Water'
        water = 'Water'
        family_kits = 'Family Kits'
        toilets = 'Toilets'
        minimum_needs = {
            'resources': [
                {'resource': rice, 'amount': 2.8, 'unit': 'kg',
                    'frequency': 'weekly'},
                {'resource': drinking_water, 'amount': 17.5, 'unit': 'l',
                    'frequency': 'weekly'},
                {'resource': water, 'amount': 67, 'unit': 'l',
                    'frequency': 'weekly'},
                {'resource': family_kits, 'amount': 0.2, 'unit': 'unit',
                    'frequency': 'weekly'},
                {'resource': toilets, 'amount': 0.05, 'unit': 'unit',
                    'frequency': 'single'},
            ],
            'provenance': 'Perka',
            'profile': [
                'BNPB'
            ]
        }
        return minimum_needs

    def read_from_file(self, filename):
        """Read from an existing json file.

        :param filename: The file to be written to.
        :type filename: basestring, str

        :returns: Success status. -1 for unsuccessful 0 for success
        :rtype: int
        """
        with open(filename) as fd:
            needs_json = fd.read()
            try:
                minimum_needs = json.loads(needs_json)
            except (TypeError, ValueError):
                minimum_needs = None

        if not minimum_needs:
            return -1

        return self.update_minimum_needs(minimum_needs)

    def write_to_file(self, filename):
        """Write minimum needs as json to a file.

        :param filename: The file to be written to.
        :type filename: basestring, str
        """
        with open(filename, 'w') as fd:
            needs_json = json.dumps(self.minimum_needs)
            fd.write(needs_json)
