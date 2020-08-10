from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        hostA = self.addHost( 'A' )
        hostB = self.addHost( 'B' )
        hostC = self.addHost( 'C' )
        hostD = self.addHost( 'D' )
        hostE = self.addHost( 'E' )
        hostF = self.addHost( 'F' )
        hostG = self.addHost( 'G' )
        
        # Add switches
        switchX = self.addSwitch( 's1' )
        switchY = self.addSwitch( 's2' )
        switchZ = self.addSwitch( 's3' )
        switchU = self.addSwitch( 's4' )
        switchV = self.addSwitch( 's5' )
        switchW = self.addSwitch( 's6' )
        switchT = self.addSwitch( 's7' )
        
        # Add Server
        self.addLink(hostG, switchT)

        # Add links in V
        self.addLink(hostA, switchV)
        self.addLink(hostB, switchV)
        # Add links in X
        self.addLink(hostC, switchX)
        self.addLink(hostD, switchX)
        # Add links in Z
        self.addLink(hostE, switchZ)
        self.addLink(hostF, switchZ)
        # Add links between switch red
        self.addLink(switchT, switchV)
        self.addLink(switchV, switchX)
        self.addLink(switchX, switchZ)
        
        # Add links between switch blue
        self.addLink(switchV, switchU)
        self.addLink(switchX, switchW)
        self.addLink(switchZ, switchY)

        self.addLink(switchY, switchW)
        self.addLink(switchW, switchU)
        self.addLink(switchU, switchT)

topos = { 'mytopo': ( lambda: MyTopo() ) }
