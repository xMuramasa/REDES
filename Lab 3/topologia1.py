from mininet.topo import Topo


class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        hostA = self.addHost( 'A' , mac='00:00:00:00:00:01')
        hostB = self.addHost( 'B' , mac='00:00:00:00:00:02')
        hostC = self.addHost( 'C' , mac='00:00:00:00:00:03')
        hostD = self.addHost( 'D' , mac='00:00:00:00:00:04')
        hostE = self.addHost( 'E' , mac='00:00:00:00:00:05')
        hostF = self.addHost( 'F' , mac='00:00:00:00:00:06')
        
        # Add switches
        switchX = self.addSwitch( 's1' )
        switchY = self.addSwitch( 's2' )
        switchZ = self.addSwitch( 's3' )

        # Add links in X
        self.addLink(hostA, switchX, 1, 2)
        self.addLink(hostB, switchX, 3, 4)

        # Add links in Y
        self.addLink(hostC, switchY, 5, 6)     
        self.addLink(hostD, switchY, 7, 8)        
        
        # Add links in Z
        self.addLink(hostE, switchZ, 9, 10)
        self.addLink(hostF, switchZ, 11, 12)
        
        # Add links between switch
        self.addLink(switchX, switchY, 13, 14)
        self.addLink(switchY, switchZ, 15, 16)
        self.addLink(switchZ, switchX, 17, 18)
        

topos = { 'mytopo': ( lambda: MyTopo() ) }
