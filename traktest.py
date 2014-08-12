#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2013  <pi@mattypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import bigtrak
import time
import os

#os.system("mpg123 love.mp3")

print("Testing Big Trak")
seconds = int(input("Forwards for how long?"))
bigtrak.setupPins()
bigtrak.goforwards(seconds)
bigtrak.resetpins()
#backwards
seconds = int(input("Backwards for how long?"))
bigtrak.setupPins()
bigtrak.gobackwards(seconds)
bigtrak.resetpins()
#right
seconds = int(input("Right for how long?"))
bigtrak.setupPins()
bigtrak.goright(seconds)
bigtrak.resetpins()
#ledt
seconds = int(input("Left for how long?"))
bigtrak.setupPins()
bigtrak.goleft(seconds)
bigtrak.resetpins()

print("End")


