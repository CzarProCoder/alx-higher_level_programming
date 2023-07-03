<h1>0x11. Python - Network #1</h1>
<div>
    <div>PythonScriptingBack-endAPI</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume, CTO at Holberton School</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Jun 30, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jul 5, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <h4>In a nutshell&hellip;</h4>
    <ul>
        <li><strong>Auto QA review:</strong> 0.0/75 mandatory &amp; 0.0/8 optional</li>
        <li><strong>Altogether:</strong>&nbsp; <strong>0.0%</strong>
            <ul>
                <li>Mandatory: 0.0%</li>
                <li>Optional: 0.0%</li>
                <li>Calculation: &nbsp;0.0% + (0.0% * 0.0%) &nbsp;== <strong>0.0%</strong></li>
            </ul>
        </li>
    </ul>
</div>
<div>
    <div>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/KoRrs5dVWsb-B82e-M1TQQ" title="HOWTO Fetch Internet Resources Using urllib Package" target="_blank">HOWTO Fetch Internet Resources Using urllib Package</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/OGcRGPr7TSWtzypDd0ZibQ" title="Quickstart with Requests package" target="_blank">Quickstart with Requests package</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/dUNaNQrV2bMSstILitQbXQ" title="Requests package" target="_blank">Requests package</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/kn48lNAWMEoi1DysNqM6bg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>How to fetch internet resources with the Python package&nbsp;<code>urllib</code></li>
            <li>How to decode&nbsp;<code>urllib</code> body response</li>
            <li>How to use the Python package&nbsp;<code>requests</code> #requestsiswaysimplerthanurllib</li>
            <li>How to make HTTP&nbsp;<code>GET</code> request</li>
            <li>How to make HTTP&nbsp;<code>POST</code>/<code>PUT</code>/etc. request</li>
            <li>How to fetch JSON resources</li>
            <li>How to manipulate data from an external service</li>
        </ul>
        <h3>Copyright - Plagiarism</h3>
        <ul>
            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
            <li>You are not allowed to publish any content of this project.</li>
        </ul>
        <h2>- Any form of plagiarism is strictly forbidden and will result in removal from the program.</h2>
        <h2>Requirements</h2>
        <h3>General</h3>
        <ul>
            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
            <li>A&nbsp;<code>README.md</code> file at the root of the repo, containing a description of the repository</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of&nbsp;<em>this</em> project, is mandatory</li>
            <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>You must use&nbsp;<a href="https://intranet.alxswe.com/rltoken/ddDVKG3F084DP9byugbABw" title="get" target="_blank">get</a> to access to dictionary value by key (it won&rsquo;t throw an exception if the key doesn&rsquo;t exist in the dictionary)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
            <li>Your code should not be executed when imported (by using&nbsp;<code>if __name__ == &quot;__main__&quot;:</code>)</li>
        </ul>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. What&apos;s my status? #0</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that fetches&nbsp;<code>https://alx-intranet.hbtn.io/status</code></p>
            <ul>
                <li>You must use the package&nbsp;<code>urllib</code></li>
                <li>You are not allowed to import any packages other than&nbsp;<code>urllib</code></li>
                <li>The body of the response must be displayed like the following example (tabulation before&nbsp;<code>-</code>)</li>
                <li>You must use a&nbsp;<code>with</code> statement</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: &lt;class &apos;bytes&apos;&gt;$
    - content: b&apos;OK&apos;$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>0-hbtn_status.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Response header value #0</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the&nbsp;<code>X-Request-Id</code> variable found in the header of the response.</p>
            <ul>
                <li>You must use the packages&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>You are not allow to import packages other than&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>The value of this variable is different for each request</li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
                <li>You must use a&nbsp;<code>with</code> statement</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>1-hbtn_header.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. POST an email #0</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL and an email, sends a&nbsp;<code>POST</code> request to the passed URL with the email as a parameter, and displays the body of the response (decoded in&nbsp;<code>utf-8</code>)</p>
            <ul>
                <li>The email must be sent in the&nbsp;<code>email</code> variable</li>
                <li>You must use the packages&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
                <li>You must use the&nbsp;<code>with</code> statement</li>
            </ul>
            <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>2-post_email.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. Error code #0</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in&nbsp;<code>utf-8</code>).</p>
            <ul>
                <li>You have to manage&nbsp;<code>urllib.error.HTTPError</code> exceptions and print:&nbsp;<code>Error code:</code> followed by the HTTP status code</li>
                <li>You must use the packages&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import other packages than&nbsp;<code>urllib</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
                <li>You must use the&nbsp;<code>with</code> statement</li>
            </ul>
            <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>3-error_code.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. What&apos;s my status? #1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that fetches&nbsp;<code>https://alx-intranet.hbtn.io/status</code></p>
            <ul>
                <li>You must use the package&nbsp;<code>requests</code></li>
                <li>You are not allow to import packages other than&nbsp;<code>requests</code></li>
                <li>The body of the response must be display like the following example (tabulation before&nbsp;<code>-</code>)</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: &lt;class &apos;str&apos;&gt;$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>4-hbtn_status.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. Response header value #1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable&nbsp;<code>X-Request-Id</code> in the response header</p>
            <ul>
                <li>You must use the packages&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allow to import other packages than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>The value of this variable is different for each request</li>
                <li>You don&rsquo;t need to check script arguments (number and type)</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>5-hbtn_header.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. POST an email #1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL and an email address, sends a&nbsp;<code>POST</code> request to the passed URL with the email as a parameter, and finally displays the body of the response.</p>
            <ul>
                <li>The email must be sent in the variable&nbsp;<code>email</code></li>
                <li>You must use the packages&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to error check arguments passed to the script (number or type)</li>
            </ul>
            <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>6-post_email.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. Error code #1</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.</p>
            <ul>
                <li>If the HTTP status code is greater than or equal to 400, print:&nbsp;<code>Error code:</code> followed by the value of the HTTP status code</li>
                <li>You must use the packages&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
            </ul>
            <p>Please test your script in the sandbox provided, using the web server running on port 5000</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>7-error_code.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. Search API</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes in a letter and sends a&nbsp;<code>POST</code> request to&nbsp;<code>http://0.0.0.0:5000/search_user</code> with the letter as a parameter.</p>
            <ul>
                <li>The letter must be sent in the variable&nbsp;<code>q</code></li>
                <li>If no argument is given, set&nbsp;<code>q=&quot;&quot;</code></li>
                <li>If the response body is properly JSON formatted and not empty, display the&nbsp;<code>id</code> and&nbsp;<code>name</code> like this:&nbsp;<code>[&lt;id&gt;] &lt;name&gt;</code></li>
                <li>Otherwise:<ul>
                        <li>Display&nbsp;<code>Not a valid JSON</code> if the JSON is invalid</li>
                        <li>Display&nbsp;<code>No result</code> if the JSON is empty</li>
                    </ul>
                </li>
                <li>You must use the package&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
            </ul>
            <p>Please test your script in the sandbox provided, using the web server running on port 5000. All JSON generated by this server are random.</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>8-json_api.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. My GitHub!</h3>
            <div>mandatory</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>Write a Python script that takes your GitHub credentials (username and password) and uses the&nbsp;<a href="https://intranet.alxswe.com/rltoken/LjPfW9hW_55YwijGVofyTQ" title="GitHub API" target="_blank">GitHub API</a> to display your&nbsp;<code>id</code></p>
            <ul>
                <li>You must use&nbsp;<a href="https://intranet.alxswe.com/rltoken/_UgCj47xv8jzRRVcOG7V4w" title="Basic Authentication" target="_blank">Basic Authentication</a> with a&nbsp;<a href="https://intranet.alxswe.com/rltoken/Kz4UM-V_bcwrcWajaCAVtQ" title="personal access token as password" target="_blank">personal access token as password</a> to access to your information (only&nbsp;<code>read:user</code> permission is needed)</li>
                <li>The first argument will be your&nbsp;<code>username</code></li>
                <li>The second argument will be your&nbsp;<code>password</code> (in your case, a&nbsp;<a href="https://intranet.alxswe.com/rltoken/Kz4UM-V_bcwrcWajaCAVtQ" title="personal access token as password" target="_blank">personal access token as password</a>)</li>
                <li>You must use the package&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>10-my_github.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button> <button>QA Review</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. Time for an interview!</h3>
            <div>#advanced</div>
        </div>
        <div>
            <div>
                <div>
                    <div><br></div>
                </div>
                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
            </div>
            <p>The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:</p>
            <pre><code>Please list 10 commits (from the most recent to oldest) of the repository &ldquo;rails&rdquo; by the user &ldquo;rails&rdquo;
You must use the GitHub API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `&lt;sha&gt;: &lt;author name&gt;` (one by line)
</code></pre>
            <p>Write a Python script that takes 2 arguments in order to solve this challenge.</p>
            <ul>
                <li>The first argument will be the&nbsp;<code>repository name</code></li>
                <li>The second argument will be the&nbsp;<code>owner name</code></li>
                <li>You must use the packages&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You are not allowed to import packages other than&nbsp;<code>requests</code> and&nbsp;<code>sys</code></li>
                <li>You don&rsquo;t need to check arguments passed to the script (number or type)</li>
            </ul>
            <p>Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.</p>
            <pre><code>guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael Fran&ccedil;a
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael Fran&ccedil;a
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael Fran&ccedil;a
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendon&ccedil;a Fran&ccedil;a
guillaume@ubuntu:~/0x11$ 
</code></pre>
            <p><strong>Be careful: only 60 requests by hour by IP for unauthenticated requests&nbsp;<a href="https://intranet.alxswe.com/rltoken/S2DhgB0xP5IPy_93vBcRhw" title="Rate limit" target="_blank">Rate limit</a></strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x11-python-network_1</code></li>
                    <li>File:&nbsp;<code>100-github_commits.py</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button>&nbsp;</div>
            </div>
        </div>
    </div>
</div>