# LittleDarwin

Java Mutation Analysis Framework
Copyright (C) 2014-2020 Ali Parsai

## How to Use:
On your selected python platform use:

    pip3 install littledarwin

You can use the program by executing it as a module:

    python3 -m littledarwin [options]

For a maven project, all you need to do is to pass the required arguments to LittleDarwin:

    python3 -m littledarwin -m -b \
			    -p [path to production code (usually in src/main)] \
			    -t [path to build directory (usually the one containing pom.xml)] \
			    --timeout=[in seconds, the duration of a normal test execution] \
			    -c [build command separated by commas (usually mvn,clean,test)]


------------------------------------------------------------------------------------
## License
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

------------------------------------------------------------------------------------
Find me at:

www.parsai.net
ali@parsai.net
ali.parsai@live.com

------------------------------------------------------------------------------------
