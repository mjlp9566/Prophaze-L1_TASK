                                                           DECODING STEPS
                                                           
                                        0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38
                                                                 |
                                                                 |	(removing spaces and '0x' from given payload)
                                                                 |
                                                       3839293530203730203438
                                                                 |
                                                                 |      (Decoding the Hex)
                                                                 |
                                                            89 70 48 52 
                                                                 |
                                                                 |      (Mapping Equivalent characters for the ascii values)
                                                                 |
                                                               Y2F0
                                                                 |
                                                                 |	(Base64 decoding)
                                                                 |
                                                                cat
                                                                     
Server:
------
<ol>
<li>Import the required modules and packages such as BaseHTTPRequestHandler,HTTPServer,base64 and BytesIO</li>
<li>A class[handler] is created to handle the requests</li>
<li>Inside  the  handler  class  define  a  function <b>do_POST()</b>  to  handle  POST  request</li>
<li>Inside  the  do_POST()  function:</li>
	<ul>
	         <li>Entire http request body is dumped into a file using rfile.read()</li>
		<li>Send response code 200 to the client</li>
		<li>end_headers() adds a blank line (indicating the end of the http headers in the response)</li>
		<li>for conversion purpose , remove the '0x' using <b>remove_0x()</b> function , this function will remove '0x' and ' ' in the payload</li>
		<li>Now decode the payload from hex encoding using <b>hexToASCII()</b> , this will change the hex string to base 16 and typecast as character</li>
		<li>Then the decoded values is mapped with equivalent ascii characterset using <b>AsciiToChr()</b></li>
		<li>Finally the mapped string is decoded using base64 decryption</li>
	</ul>
  <li>The  message(decrypted payload)  is  sent  as  a  repsonse  to  the  server  using  response.write()</li>
<li>Initiate the server at the <b>PORT 7878</b> with the request handler</li>
</ol>

<h5>NOTE:</h5>
<p>If needed,we can use built functions like</p>
<pre><li>fromhex()</li><li>replace(),remove()</li></pre>
<p>for easy conversion and to make the code easier</p>

Client:
------
<ol>
	<li>Import the required module (requests)</li>
	<li>Define a url with server's adress and <b>port 7878</b></li>
	<li>Using requests.post() send a post request to the url with the payload</li>
<li>If the server is not responding or The URL is not correct and etc.. then an exception is raised and handled</li>
</ol>
<pre><b>NOTE:</b>We can make the code to get the hostname(or)IP from user and the payload also can be get as an input</pre>                                                                  

encrypt.py:
------
<h3>NOTE:THIS FILE IS NOT USED</h3>
<p>we can use this 'encrypt.py' file to encrypt the payload(cat--->0x38 0x39 0x20 0x35 0x30 0x20 0x37 0x30 0x20 0x34 0x38)</p>

<h1>Screenshots:</h1>

![Screenshot from 2022-08-05 19-25-45](https://user-images.githubusercontent.com/55002003/183114001-a5e466b2-d7f6-4a2d-8874-113e3e79ea8c.png)


![Screenshot from 2022-08-05 19-25-29](https://user-images.githubusercontent.com/55002003/183113957-b90aa887-882b-4af7-9655-f75e69bc977c.png)



