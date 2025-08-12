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

    def get_ndp(self):
        """Get NDP table for router."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/interface/getNdp")
        else: 
            return self._get("diagnostics/interface/get_ndp")

    def get_arp(self):
        """Get ARP table for router."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/interface/getArp")
        else: 
            return self._get("diagnostics/interface/get_arp")


class NetworkInsightClient(client.OPNClient):
    """A client for interacting with the diagnostics/networkinsight endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """

    def get_interfaces(self):
        """Return the available interfaces."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/networkinsight/getinterfaces")
        else:
            return self._get("diagnostics/networkinsight/get_interfaces")

    def get_services(self):
        """Return the available services."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/networkinsight/getservices")
        else:        
            return self._get("diagnostics/networkinsight/get_services")

    def get_protocols(self):
        """Return the protocols."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/networkinsight/getprotocols")
        else:
            return self._get("diagnostics/networkinsight/get_protocols")

    def get_timeserie(self):
        """Return the time serie."""
        return self._get("diagnostics/networkinsight/timeserie")


class SystemHealthClient(client.OPNClient):
    """A client for interacting with the diagnostics/systemhealth endpoint.

    :param str api_key: The API key to use for requests
    :param str api_secret: The API secret to use for requests
    :param str base_url: The base API endpoint for the OPNsense deployment
    :param int timeout: The timeout in seconds for API requests
    """

    def get_health_list(self):
        """Return the health list."""
        if (self.api_version_pre_25_7):
            return self._get("diagnostics/systemhealth/getRRDlist")
        else:
            return self._get("diagnostics/systemhealth/get_rrd_list")

    def get_health_data(
        self, metric, start=0, stop=0, maxitems=1024, inverse=False, details=False
    ):
        """Return the health data."""
        url = ["diagnostics/systemhealth/getSystemHealth"] if self.api_version_pre_25_7 else ["diagnostics/systemhealth/get_system_health"]
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
