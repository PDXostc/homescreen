Copyright (c) 2014, Intel Corporation, Jaguar Land Rover

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Name: HomeScreen
Version: XW_TizenIVI3_0_01FEB_AGL_05MAR2015
Maintainer: Steve Mattison <smattiso@jaguarlandrover.com>
Mailing list: dev@lists.tizen.org


Build Instructions: 

	make apps - To build the wgt files for all release apps

Set the TIZEN_IP enviroment varable to the ip of target. or set TizenVTC host name to that ip.

	make deploy - To build and copy the wgt files to the platform

	make install.feb1 - To build and install wigits on the platform

	make run.feb1 - To build, install and run on the platform

	-- Applications

	All applications make use of the "common" repository for artifacts 
	common across every POC.


KnownIssues:

	The preloader causes a series of flashes when the system starts. Trac #186

	The Volume Level setting does not persist between apps while multitasking. Trac #187

	Occasionally animation is jittery. Trac #164