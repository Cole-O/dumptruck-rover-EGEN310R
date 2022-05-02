# dumptruck-rover-EGEN310R


## Overview
This is the code repository for Group A6's dump truck rover controller.  The rover is primary controlled via bluetooth connection through a python controller. This controller dynamically takes keyboard inputs from the user and sends them to an arduino for processing.  In turn, the arduino has logic statements to determine what should be done with the inputs given.  

## Control Scheme

Controls are implemented in way that makes sense for most game controls.  

**Example:**
Pressing W results in the rover moving forward until the user presses the space bar, at which the rover promptly stops moving.

* W - Move Forward
* A - Move Left
* S - Move Backwards
* D - Move Right
* Space - Stop all movement
* L - Move dump bed up
* l - Move dump bed down

*For movement commands, lower case characters work the same way as upper case.  This is not the case with the dump bed, as it is case specific.*

