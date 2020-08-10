from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        hostA = self.addHost( 'A' ,  mac='00:00:00:00:00:01')
        hostB = self.addHost( 'B' ,  mac='00:00:00:00:00:02')
        hostC = self.addHost( 'C' ,  mac='00:00:00:00:00:03')
        hostD = self.addHost( 'D' ,  mac='00:00:00:00:00:04')
        hostE = self.addHost( 'E' ,  mac='00:00:00:00:00:05')
        hostF = self.addHost( 'F' ,  mac='00:00:00:00:00:06')
        hostG = self.addHost( 'G' ,  mac='00:00:00:00:00:07')
        
        # Add switches
        switchX = self.addSwitch( 's1' )
        switchY = self.addSwitch( 's2' )
        switchZ = self.addSwitch( 's3' )
        switchU = self.addSwitch( 's4' )
        switchV = self.addSwitch( 's5' )
        switchW = self.addSwitch( 's6' )
        switchT = self.addSwitch( 's7' )
        

        # Add links in V
        self.addLink(hostA, switchV, 1, 2)
        self.addLink(hostB, switchV, 3, 4)
        
        # Add links in X
        self.addLink(hostC, switchX, 5 ,6)
        self.addLink(hostD, switchX, 7, 8)
        
        # Add links in Z
        self.addLink(hostE, switchZ, 9  , 10)
        self.addLink(hostF, switchZ, 11 , 12)
       
        # Add Server
        self.addLink(hostG, switchT, 13 , 14)

        # Add links between switch red
        self.addLink(switchT, switchV, 15 , 16)
        self.addLink(switchV, switchX, 17 , 18)
        self.addLink(switchX, switchZ, 19 , 20)
        
        # Add links between switch blue
        self.addLink(switchV, switchU, 21 , 22)
        self.addLink(switchX, switchW, 23 , 24)
        self.addLink(switchZ, switchY, 25 , 26)

        self.addLink(switchY, switchW, 27 , 28)
        self.addLink(switchW, switchU, 29 , 30)
        self.addLink(switchU, switchT, 31 , 32)

topos = { 'mytopo': ( lambda: MyTopo() ) }
