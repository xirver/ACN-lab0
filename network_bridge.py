# Copyright 2020 Lin Wang
#
# This code is part of the Advanced Computer Networks (ACN) course at VU 
# Amsterdam.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

#!/usr/bin/python

from mininet.topo import Topo
from mininet.link import TCLink
from mininet.node import OVSKernelSwitch


class BridgeTopo(Topo):
    "Creat a bridge-like customized network topology."

    def __init__(self):

        Topo.__init__(self)

        # TODO: add nodes and links to construct the topology
        #add host and switches
    	host1 = self.addHost('h1', ip = '10.0.0.1/8')
    	host2 = self.addHost('h2', ip = '10.0.0.2/8')
    	host3 = self.addHost('h3', ip = '10.0.0.3/8')
    	host4 = self.addHost('h4', ip = '10.0.0.4/8')
    	leftSwitch = self.addSwitch('s1')
    	rightSwitch = self.addSwitch('s2')

    	#add links
    	self.addLink(host1,leftSwitch, bw = 15, delay = '10ms')
    	self.addLink(host2,leftSwitch, bw = 15, delay = '10ms')
    	self.addLink(leftSwitch, rightSwitch, bw = 20, delay = '45ms')
    	self.addLink(host3,rightSwitch, bw = 15, delay = '10ms')
	self.addLink(host4,rightSwitch, bw = 15, delay = '10ms')
topos = {'bridge': (lambda: BridgeTopo())}
