# arduino2graph
Python code to output arduino temperature output from DHT22 to a graph

To use simply upload the .ino script to an arduino, the file is configure for an arduino uno with temperature sensor plugged into data pin 2
then run ```pip3 install matplotlib```  
and ```pip3 install pyserial```  
then in one terminal ```python -m SimpleHTTPServer```  
and in another ```python3 arduino2pi.py```  

For this to work you must **not** use ssh instead use VNC or any other remote desktop viewer that will allow the desktop to be seen.
