<div>
    <ul>
        <li title=""><a href="https://intranet.alxswe.com/planning/me">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/projects/current">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/corrections/to_review">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/my_current_evaluation_quizzes">
                <div><br></div>
            </a></li>
        <li>
            <hr title="My resources">
        </li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/my_curriculums">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/concepts">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/video_rooms">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/servers">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/user_containers/current">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/my_tools">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/videos">
                <div><br></div>
            </a></li>
        <li>
            <hr title="My campus">
        </li>
        <li title=""><a href="https://intranet.alxswe.com/users/peers">
                <div><br></div>
            </a></li>
        <li title=""><a href="https://intranet.alxswe.com/dashboards/my_captain_log">
                <div><br></div>
            </a></li>
        <li>
            <div title=""><a target="_blank" href="https://alx-students.slack.com/">
                    <div>
                        <div><br></div>
                    </div>
                </a></div>
            <div title=""><a href="https://intranet.alxswe.com/users/my_profile">
                    <div>
                        <div><br></div>
                    </div>
                </a></div>
        </li>
    </ul>
</div>
<main>
    <div><br></div>
    <article>
        <div>
            <div>
                <h1>0x0C. Web server</h1>
                <div>
                    <div>DevOpsSysAdmin</div>
                </div>
                <div>
                    <ul>
                        <li>&nbsp;By:&nbsp;Sylvain Kalache</li>
                        <li>&nbsp;Weight:&nbsp;1</li>
                        <li>&nbsp;Ongoing second chance project - started&nbsp;<span title="">Jun 26, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jun 29, 2023 6:00 AM</span></li>
                        <li>&nbsp;An auto review will be launched at the deadline</li>
                    </ul>
                </div>
                <div>
                    <h4>In a nutshell&hellip;</h4>
                    <ul>
                        <li><strong>Auto QA review:</strong> 0.0/13 mandatory &amp; 0.0/4 optional</li>
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
                        <h3>Concepts</h3>
                    </div>
                    <div>
                        <p><em>For this project, we expect you to look at this concept:</em></p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/concepts/110">What is a Child Process?</a></li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" alt=""></p>
                        <h2>Background Context</h2>
                        <p><a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&feature=youtu.be&hd=1" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" alt=""></a></p>
                        <p>In this project, some of the tasks will be graded on 2 aspects:</p>
                        <ol>
                            <li>Is your&nbsp;<code>web-01</code> server configured according to requirements</li>
                            <li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
                        </ol>
                        <p>For example, if I need to create a file&nbsp;<code>/tmp/test</code> containing the string&nbsp;<code>hello world</code> and modify the configuration of Nginx to listen on port&nbsp;<code>8080</code> instead of&nbsp;<code>80</code>, I can use&nbsp;<code>emacs</code> on my server to create the file and to modify the Nginx configuration file&nbsp;<code>/etc/nginx/sites-enabled/default</code>.</p>
                        <p>But my answer file would contain:</p>
                        <pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i &apos;s/80/8080/g&apos; /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>
                        <p>As you can tell, I am not using&nbsp;<code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an&nbsp;<a href="https://intranet.alxswe.com/rltoken/9I0WufjKdW3TZA2EVrGnlQ" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the&nbsp;<code>root</code> user, you do not need to use the&nbsp;<code>sudo</code> command.</p>
                        <p>A good Software Engineer is a&nbsp;<a href="https://intranet.alxswe.com/rltoken/sRY__axKNHhNW0SVmsUC_A" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.&nbsp;<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt=""></p>
                        <p>Tips: to test your answer Bash script, feel free to reproduce the checker environment:</p>
                        <ul>
                            <li>start a&nbsp;<code>Ubuntu 16.04</code> sandbox</li>
                            <li>run your script on it</li>
                            <li>see how it behaves</li>
                        </ul>
                        <h2>Resources</h2>
                        <p><strong>Read or watch</strong>:</p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/6TI3HiyFdwrbXWKVF24Gxw" title="How the web works" target="_blank">How the web works</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/vkVMGlaf39j2DWAQWzo6EA" title="Nginx" target="_blank">Nginx</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/zKrpVxWuUHVdW4URAjdFbw" title="How to Configure Nginx" target="_blank">How to Configure Nginx</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/Ar18u5sRis1fkvkVgzdcqg" title="Child process concept page" target="_blank">Child process concept page</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/xi3peVqYl02PfpHHHlCtxQ" title="Root and sub domain" target="_blank">Root and sub domain</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/sBrrP4EAmI3NoYjIgZrUhw" title="HTTP requests" target="_blank">HTTP requests</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/Eaa4ZuKvye941hTkP8VlBQ" title="HTTP redirection" target="_blank">HTTP redirection</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/eJSp2QFTY6jqqNtz8OVDEw" title="Not found HTTP response code" target="_blank">Not found HTTP response code</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/7WMNY5CWD-CBrxmQrdmfPg" title="Logs files on Linux" target="_blank">Logs files on Linux</a></li>
                        </ul>
                        <p><strong>For reference:</strong></p>
                        <ul>
                            <li><a href="https://intranet.alxswe.com/rltoken/BGa6RrS0dnM6EdBGS_ZDUw" title="RFC 7231 (HTTP/1.1)" target="_blank">RFC 7231 (HTTP/1.1)</a></li>
                            <li><a href="https://intranet.alxswe.com/rltoken/IZ2fyYn1qNZ9RXXsg5vG1g" title="RFC 7540 (HTTP/2)" target="_blank">RFC 7540 (HTTP/2)</a></li>
                        </ul>
                        <p><strong>man or help</strong>:</p>
                        <ul>
                            <li><code>scp</code></li>
                            <li><code>curl</code></li>
                        </ul>
                        <h2>Learning Objectives</h2>
                        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/EHyxcIwPtD2SzEGRKOnT3g" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
                        <h3>General</h3>
                        <ul>
                            <li>What is the main role of a web server</li>
                            <li>What is a child process</li>
                            <li>Why web servers usually have a parent process and child processes</li>
                            <li>What are the main HTTP requests</li>
                        </ul>
                        <h3>DNS</h3>
                        <ul>
                            <li>What DNS stands for</li>
                            <li>What is DNS main role</li>
                        </ul>
                        <h3>DNS Record Types</h3>
                        <ul>
                            <li><code>A</code></li>
                            <li><code>CNAME</code></li>
                            <li><code>TXT</code></li>
                            <li><code>MX</code></li>
                        </ul>
                        <h3>Copyright - Plagiarism</h3>
                        <ul>
                            <li>You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.</li>
                            <li>You will not be able to meet the objectives of this or any following project by copying and pasting someone else&rsquo;s work.</li>
                            <li>You are not allowed to publish any content of this project.</li>
                            <li>Any form of plagiarism is strictly forbidden and will result in removal from the program.</li>
                        </ul>
                        <h2>Requirements</h2>
                        <h3>General</h3>
                        <ul>
                            <li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
                            <li>All your files will be interpreted on Ubuntu 16.04 LTS</li>
                            <li>All your files should end with a new line</li>
                            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
                            <li>All your Bash script files must be executable</li>
                            <li>Your Bash script must pass&nbsp;<code>Shellcheck</code> (version&nbsp;<code>0.3.7</code>) without any error</li>
                            <li>The first line of all your Bash scripts should be exactly&nbsp;<code>#!/usr/bin/env bash</code></li>
                            <li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
                            <li>You can&rsquo;t use&nbsp;<code>systemctl</code> for restarting a process</li>
                        </ul>
                    </div>
                </div>
                <div>
                    <div>
                        <h3>Quiz questions</h3>
                    </div>
                    <div>
                        <div><strong>Great!</strong> You&apos;ve completed the quiz successfully! Keep going!&nbsp;(Show quiz)</div>
                    </div>
                </div>
                <h2>Your servers</h2>
                <div>
                    <div>
                        <table>
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Username</th>
                                    <th>IP</th>
                                    <th>State</th>
                                    <th><br></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>196617-web-01</td>
                                    <td><code>ubuntu</code></td>
                                    <td><code>100.25.130.189</code></td>
                                    <td>running</td>
                                    <td>
                                        <div><button type="button">Actions&nbsp;Toggle Dropdown</button></div>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <h2>Tasks</h2>
                <div>
                    <div>
                        <div>
                            <h3>0. Transfer a file to your server</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Write a Bash script that transfers a file from our client to a server:</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Accepts 4 parameters<ol>
                                        <li>The path to the file to be transferred</li>
                                        <li>The IP of the server we want to transfer the file to</li>
                                        <li>The username&nbsp;<code>scp</code> connects with</li>
                                        <li>The path to the SSH private key that&nbsp;<code>scp</code> uses</li>
                                    </ol>
                                </li>
                                <li>Display&nbsp;<code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
                                <li><code>scp</code> must transfer the file to the user home directory&nbsp;<code>~/</code></li>
                                <li>Strict host key checking must be disabled when using&nbsp;<code>scp</code></li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain &apos;ls ~/&apos;
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key &apos;ls ~/&apos;
afile
some_page.html
sylvain@ubuntu$
</code></pre>
                            <p>In this example, I:</p>
                            <ul>
                                <li>remotely execute the&nbsp;<code>ls ~/</code> command via&nbsp;<code>ssh</code> to see what&nbsp;<code>~/</code> contains</li>
                                <li>create a file named&nbsp;<code>some_page.html</code></li>
                                <li>execute my&nbsp;<code>0-transfer_file</code> script</li>
                                <li>remotely execute the&nbsp;<code>ls ~/</code> command via&nbsp;<code>ssh</code> to see that the file&nbsp;<code>some_page.html</code> has been successfully transferred</li>
                            </ul>
                            <p>That is one way of publishing your website pages to your server.</p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>0-transfer_file</code></li>
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
                            <h3>1. Install nginx web server</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/01cab59e881e31842b8d47a0974e8d3b6f0f2001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230628%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230628T084939Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ce152d06063802912462dd375f0436e4f9663c7d00036f4ca79a62d96392609" alt=""></p>
                            <p>Readme:</p>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/rltoken/KJiFZ4yJyTGp_cv3DYQLaQ" title="-y on apt-get command" target="_blank">-y on apt-get command</a></li>
                            </ul>
                            <p>Web servers are the piece of software generating and serving HTML pages, let&rsquo;s install one!</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Install&nbsp;<code>nginx</code> on your&nbsp;<code>web-01</code></li>
                                <li>server</li>
                                <li>Nginx should be listening on port 80</li>
                                <li>When querying Nginx at its root&nbsp;<code>/</code> with a GET request (requesting a page) using&nbsp;<code>curl</code>, it must return a page that contains the string&nbsp;<code>Hello World!</code></li>
                                <li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)</li>
                                <li>You can&rsquo;t use&nbsp;<code>systemctl</code> for restarting&nbsp;<code>nginx</code></li>
                            </ul>
                            <p>Server terminal:</p>
                            <pre><code>root@sy-web-01$ ./1-install_nginx_web_server &gt; /dev/null 2&gt;&amp;1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 
</code></pre>
                            <p>Local terminal:</p>
                            <pre><code>sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: &quot;58abea7c-1e&quot;
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>
                            <p>In this example&nbsp;<code>34.198.248.145</code> is the IP of my&nbsp;<code>web-01</code> server. If you want to query the Nginx that is locally installed on your server, you can use&nbsp;<code>curl 127.0.0.1</code>.</p>
                            <p>If things are not going as expected, make sure to check out Nginx logs, they can be found in&nbsp;<code>/var/log/</code>.</p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>1-install_nginx_web_server</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>QA Review</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>2. Setup a domain name</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p><a href="https://intranet.alxswe.com/rltoken/Hcb-pfK8UiDBfwsDJPyZZw" title=".TECH Domains" target="_blank">.TECH Domains</a> is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.</p>
                            <p>.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your&nbsp;<a href="https://intranet.alxswe.com/rltoken/CprZO4m1rUm5C6ZgvROpgg" title="tools space" target="_blank">tools space</a>. Feel free to drop a thank you tweet for&nbsp;<a href="https://intranet.alxswe.com/rltoken/y3_YCbJ5bGKgPYqP0LyVBA" title=".TECH Domains" target="_blank">.TECH Domains</a>.</p>
                            <p>Provide the domain name in your answer file.</p>
                            <p>Requirement:</p>
                            <ul>
                                <li>provide the domain name only (example:&nbsp;<code>foobar.tech</code>), no subdomain (example:&nbsp;<code>www.foobar.tech</code>)</li>
                                <li>configure your DNS records with an A entry so that your root domain points to your&nbsp;<code>web-01</code> IP address&nbsp;<strong>Warning: the propagation of your records can take time (~1-2 hours)</strong></li>
                                <li>go to&nbsp;<a href="https://intranet.alxswe.com/rltoken/hH2hPj0jwETzZL-AvFJkwQ" title="your profile" target="_blank">your profile</a> and enter your domain in the&nbsp;<code>Project website url</code> field</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; myschool.tech
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
</code></pre>
                            <p>When your domain name is setup, please verify the Registrar here:&nbsp;<a href="https://intranet.alxswe.com/rltoken/UVCb6LeF54ktxR6lZSUyTQ" title="https://whois.whoisxmlapi.com/" target="_blank">https://whois.whoisxmlapi.com/</a> and you must see in the JSON response:&nbsp;<code>&quot;registrarName&quot;: &quot;Dotserve Inc&quot;</code></p>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>2-setup_a_domain_name</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>QA Review</button></div>
                                <div><br></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <div>
                        <div>
                            <h3>3. Redirection</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Readme:</p>
                            <ul>
                                <li><a href="https://intranet.alxswe.com/rltoken/RRP9hX3MlQdABaKZD-Y_cA" title="Replace a line with multiple lines with sed" target="_blank">Replace a line with multiple lines with sed</a></li>
                            </ul>
                            <p>Configure your Nginx server so that&nbsp;<code>/redirect_me</code> is redirecting to another page.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>The redirection must be a &ldquo;301 Moved Permanently&rdquo;</li>
                                <li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
                                <li>Using what you did with&nbsp;<code>1-install_nginx_web_server</code>, write&nbsp;<code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>3-redirection</code></li>
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
                            <h3>4. Not found page 404</h3>
                            <div>mandatory</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Configure your Nginx server to have a custom 404 page that contains the string&nbsp;<code>Ceci n&apos;est pas une page</code>.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>The page must return an HTTP 404 error code</li>
                                <li>The page must contain the string&nbsp;<code>Ceci n&apos;est pas une page</code></li>
                                <li>Using what you did with&nbsp;<code>3-redirection</code>, write&nbsp;<code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
                            </ul>
                            <p>Example:</p>
                            <pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: &quot;58acb50e-1a&quot;

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n&apos;est pas une page

sylvain@ubuntu$
</code></pre>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>4-not_found_page_404</code></li>
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
                            <h3>5. Install Nginx web server (w/ Puppet)</h3>
                            <div>#advanced</div>
                        </div>
                        <div>
                            <div>
                                <div>
                                    <div><br></div>
                                </div>
                                <div>Score:&nbsp;0.0%&nbsp;(Checks completed: 0.0%)</div>
                            </div>
                            <p>Time to practice configuring your server with Puppet! Just as you did before, we&rsquo;d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.</p>
                            <p>Requirements:</p>
                            <ul>
                                <li>Nginx should be listening on port 80</li>
                                <li>When querying Nginx at its root&nbsp;<code>/</code> with a GET request (requesting a page) using&nbsp;<code>curl</code>, it must return a page that contains the string&nbsp;<code>Hello World!</code></li>
                                <li>The redirection must be a &ldquo;301 Moved Permanently&rdquo;</li>
                                <li>Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements</li>
                            </ul>
                        </div>
                        <div>
                            <div>
                                <p><strong>Repo:</strong></p>
                                <ul>
                                    <li>GitHub repository:&nbsp;<code>alx-system_engineering-devops</code></li>
                                    <li>Directory:&nbsp;<code>0x0C-web_server</code></li>
                                    <li>File:&nbsp;<code>7-puppet_install_nginx_web_server.pp</code></li>
                                </ul>
                            </div>
                        </div>
                        <div>
                            <div>
                                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button>&nbsp;</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </article>
</main>
