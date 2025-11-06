! NavierStokes1D.f90
!
! Analytical Solution of the Navier-Stokes Equations for Fully Developed Laminar Flow in a Straight Channel (Flow between Parallel Flat Plates).
!
! Written by Dr. Laszlo Konozsy ' 10. 10. 2012
!  
! Department of Engineering Physics,
! Cranfield University, Cranfield, Bedfordshire,
! MK43 OAL, United Kingdom
!
! Introduction to Fluid Mechanics and Heat Transfer Module for MSc-CFD Students. Example FORTRAN code for Studying Purpose. 

program NavierStokes1DAnalyicalSolution

	implicit none

	integer J

	integer, parameter :: YMAX = 20 ! NUMBER OF GRID POINTS

	real RHO, MU, NU, ua, dp, Q, Re
	real length, height, width, l, h, w

	real Y0, delY

	real, dimension(1:YMAX) :: Y, U

	! MATERIAL PROPERTIES OF THE WATER
	RHO = 1000.0  	       ! DENSITY OF THE FLUID
	MU = 0.00102 	       ! DYNAMIC VISCOSITY OF THE FLUID  
	NU = MU/RHO  	       ! KINEMATIC VISCOSITY OF THE FLUID

	print *, 'Fluid density, RHO [kg/m3] = ', RHO
	print *, 'Dynamic viscosity MU [Pas] = ', MU
	print *, 'Kinematic viscosity NU [m2/s] = ', NU

	! DIMENSIONS OF THE COMPUTATIONAL DOMAIN
	length = 2.0 	       ! LENGTH OF THE DOMAIN [meter]
	height = 0.3  	       ! HEIGHT OF THE DOMAIN [meter]
	width = 1.0            ! WIDTH OF THE DOMAIN  [meter]

	l = length	       ! LENGTH OF THE CHANNEL
	h = height	       ! HEIGHT OF THE CHANNEL
	w = width	       ! WIDTH OF THE CHANNEL

	print *, 'Length of the channel [m] = ', l
	print *, 'Height of the channel [m] = ', h
	print *, 'Width of the channel [m] = ', w

	! INPUT REYNOLDS NUMBER
	Re = 1.0 		
	print *, 'Reynolds number = ', Re

	! COMPUTE THE AVERAGE VELOCITY OF THE FLOW
	ua = (Re*NU)/(2.0*h)
	print *, 'Average velocity of the flow = ', ua

	! COMPUTE THE PRESSURE-DROP
	dp = (12.0*MU*l*ua)/(h*h)
	print *, 'Pressure drop in the channel = ', dp

	! COMPUTE THE VOLUME FLOW RATE
	Q = (w*dp*h*h*h)/(12.0*MU*l)
	print *, 'Volume flow rate = ', Q

	! ONE-DIMENSIONAL GRID GENERATION

	delY = h/(YMAX-1) ! DOMAIN DISCRETIZATION IN DIRECTION-Y (GRID SPACING)
	print *, 'Grid spacing (dy) = ', delY
	
	Y0 = 0.0
	do J=1,YMAX
	  Y(J) = Y0
          Y0 = Y0+delY
	end do
    
	! ANALYTICAL SOLUTION FOR THE VELOCITY PROFILE TO VALIDATE THE NUMERICAL SOLUTION AT THE OUTLET SECTION OF THE CHANNEL
	do J=1,YMAX
          if(J.eq.1.or.J.eq.YMAX) then
	     U(J) = 0.0
	  else
	     U(J) = (dp/(2.0*MU*l))*Y(J)*(h-Y(J))
	  end if
	end do

	! WRITE THE COMPUTED ANALYTICAL VELOCITY PROFILE IN A FILE
	open(1,file = 'OutputProfileNS1D.dat')

	do J=1,YMAX
	  write (1,*) Y(J), U(J)
 	end do

	close (1)

	print *, 'OUTPUT FILE IS READY!'

end program NavierStokes1DAnalyicalSolution

! END
