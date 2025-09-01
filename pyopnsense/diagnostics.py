# Copyright 2018 Matthew Treinish
#
# This file is part of pyopnsense
#
# pyopnsense is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyopnsense is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyopnsense. If not, see <http://www.gnu.org/licenses/>.

import urllib

from pyopnsense import client


class NetFlowClient(client.OPNClient):
    """A client for interacting with the diagnostics/netflow endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    """

    def status(self):
        """Return the current netflow status.

        :returns: A dict representing the current status of netflow
        :rtype: dict
        """
        return self._get("diagnostics/netflow/status")


class InterfaceClient(client.OPNClient):
    """A client for interacting with the diagnostics/interface endpoint

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """
    
    def __get_ndp_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/interface/getNdp"
        else:
            return "diagnostics/interface/get_ndp"

    def __get_arp_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/interface/getArp"
        else:
            return "diagnostics/interface/get_arp"
 
    def get_ndp(self):
        """Get NDP table for router."""
        return self._get(self.__get_ndp_uri)

    def get_arp(self):
        """Get ARP table for router."""
        return self._get(self.__get_arp_uri())


class NetworkInsightClient(client.OPNClient):
    """A client for interacting with the diagnostics/networkinsight endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """
        
    def __get_interfaces_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/networkinsight/getinterfaces"
        else:
            return "diagnostics/networkinsight/get_interfaces"
    
    def __get_services_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/networkinsight/getservices"
        else:
            return "diagnostics/networkinsight/get_services"
    
    def __get_protocols_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/networkinsight/getprotocols"
        else:
            return "diagnostics/networkinsight/get_protocols"

    def __get_timeserie_uri(self):
        return "diagnostics/networkinsight/timeserie"

    def get_interfaces(self):
        """Return the available interfaces."""
        return self._get(self.__get_interfaces_uri)

    def get_services(self):
        """Return the available services."""
        return self._get(self.__get_services_uri)

    def get_protocols(self):
        """Return the protocols."""
        return self._get(self.__get_protocols_uri)

    def get_timeserie(self):
        """Return the time serie."""
        return self._get(self.__get_timeserie_uri)


class SystemHealthClient(client.OPNClient):
    """A client for interacting with the diagnostics/systemhealth endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """

    def __get_health_list_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/systemhealth/getRRDlist"
        else:
            return "diagnostics/systemhealth/get_rrd_list"

    def __get_health_data_uri(self):
        if (self.api_version_pre_25_7):
            return "diagnostics/systemhealth/getSystemHealth"
        else:
            return "diagnostics/systemhealth/get_system_health"

    def get_health_list(self):
        """Return the health list."""
        return self._get(self.__get_health_list_uri)

    def get_health_data(
        self, metric, start=0, stop=0, maxitems=1024, inverse=False, details=False
    ):
        """Return the health data."""
        url = self.__get_health_data_uri()
        url.append(urllib.parse.quote(metric))
        url.append(start)
        url.append(stop)
        url.append(maxitems)
        if inverse:
            url.append("true")
        else:
            url.append("false")
        if details:
            url.append("true")
        else:
            url.append("false")

        return self._get("/".join(url))
