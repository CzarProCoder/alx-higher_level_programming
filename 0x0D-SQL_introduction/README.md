<h1>0x0D. SQL - Introduction</h1>
<div>
    <div>SQLMySQL</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">May 16, 2023 6:00 AM</span>, must end by&nbsp;<span title="">May 17, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">May 16, 2023 12:00 PM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h3>Concepts</h3>
    </div>
    <div>
        <p><em>For this project, we expect you to look at these concepts:</em></p>
        <ul>
            <li><a href="https://intranet.alxswe.com/concepts/37">Databases</a></li>
            <li><a href="https://intranet.alxswe.com/concepts/556">Databases</a></li>
        </ul>
    </div>
</div>
<div>
    <div>
        <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg" alt=""></p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/yyRKTEdRkYEVlRgZPbasjw" title="What is Database & SQL?" target="_blank">What is Database &amp; SQL?</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/sV2PtK5YfQsXWW1malRZ5Q" title="A Basic MySQL Tutorial" target="_blank">A Basic MySQL Tutorial</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/IUKo4-UaRZSKPvXr5u9oBw" title="Basic SQL statements: DDL and DML" target="_blank">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/rXKvu2u7vg1Hj6bnX7UgMg" title="Basic queries: SQL and RA" target="_blank">Basic queries: SQL and RA</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/-Riv_dzSYsJyvy-LlaO6Mg" title="SQL technique: functions" target="_blank">SQL technique: functions</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/QpIXoR--8eBIaidgSWYsBQ" title="SQL technique: subqueries" target="_blank">SQL technique: subqueries</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/Gt0nFJPJRwW2Y0izzwbVrw" title="What makes the big difference between a backtick and an apostrophe?" target="_blank">What makes the big difference between a backtick and an apostrophe?</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/1oU1LwCksQLXjs6fZYezrw" title="MySQL Cheat Sheet" target="_blank">MySQL Cheat Sheet</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/HmdmLiYBM0Q34iCYPWd9XQ" title="MySQL 8.0 SQL Statement Syntax" target="_blank">MySQL 8.0 SQL Statement Syntax</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/IpYI9rgbwfjxOAQQgpHCmQ" title="installing MySQL in Ubuntu 20.04" target="_blank">installing MySQL in Ubuntu 20.04</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/-zY4kpQMjYkkbqlEb9W37A" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>What&rsquo;s a database</li>
            <li>What&rsquo;s a relational database</li>
            <li>What does SQL stand for</li>
            <li>What&rsquo;s MySQL</li>
            <li>How to create a database in MySQL</li>
            <li>What does&nbsp;<code>DDL</code> and&nbsp;<code>DML</code> stand for</li>
            <li>How to&nbsp;<code>CREATE</code> or&nbsp;<code>ALTER</code> a table</li>
            <li>How to&nbsp;<code>SELECT</code> data from a table</li>
            <li>How to&nbsp;<code>INSERT</code>,&nbsp;<code>UPDATE</code> or&nbsp;<code>DELETE</code> data</li>
            <li>What are&nbsp;<code>subqueries</code></li>
            <li>How to use MySQL functions</li>
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
            <li>All your files will be executed on Ubuntu 20.04 LTS using&nbsp;<code>MySQL 8.0</code> (version 8.0.25)</li>
            <li>All your files should end with a new line</li>
            <li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
            <li>All your files should start by a comment describing the task</li>
            <li>All SQL keywords should be in uppercase (<code>SELECT</code>,&nbsp;<code>WHERE</code>&hellip;)</li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
        </ul>
        <h2>More Info</h2>
        <h3>Comments for your SQL file:</h3>
        <pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
        <h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>
        <pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>
        <p>Connect to your MySQL server:</p>
        <pre><code>$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type &apos;help;&apos; or &apos;\h&apos; for help. Type &apos;\c&apos; to clear the current input statement.

mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>
        <h3>Use &ldquo;container-on-demand&rdquo; to run MySQL</h3>
        <p><strong>In the container, credentials are&nbsp;<code>root/root</code></strong></p>
        <ul>
            <li>Ask for container&nbsp;<code>Ubuntu 20.04</code></li>
            <li>Connect via SSH</li>
            <li>OR connect via the Web terminal</li>
            <li>In the container, you should start MySQL before playing with it:</li>
        </ul>
        <pre><code>$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -p                               
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$
</code></pre>
        <p><strong>In the container, credentials are&nbsp;<code>root/root</code></strong></p>
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
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. List databases</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all databases of your MySQL server.</p>
            <pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>0-list_databases.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>1. Create a database</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that creates the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>If the database&nbsp;<code>hbtn_0c_0</code> already exists, your script should not fail</li>
                <li>You are not allowed to use the&nbsp;<code>SELECT</code> or&nbsp;<code>SHOW</code> statements</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>1-create_database_if_missing.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>2. Delete a database</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that deletes the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>If the database&nbsp;<code>hbtn_0c_0</code> doesn&rsquo;t exist, your script should not fail</li>
                <li>You are not allowed to use the&nbsp;<code>SELECT</code> or&nbsp;<code>SHOW</code> statements</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database                                                                                                                                                                  
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>2-remove_database.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>3. List tables</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all the tables of a database in your MySQL server.</p>
            <ul>
                <li>The database name will be passed as argument of&nbsp;<code>mysql</code> command (in the following example:&nbsp;<code>mysql</code> is the name of the database)</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql                                                                              
columns_priv                                                                                 
component                                                                                    
db                                                                                           
default_roles                                                                                
engine_cost                                                                                  
func                                                                                         
general_log                                                                                  
global_grants                                                                                
gtid_executed                                                                                
help_category                                                                                
help_keyword                                                                                 
help_relation                                                                                
help_topic                                                                                   
innodb_index_stats                                                                           
innodb_table_stats                                                                           
password_history                                                                             
plugin                                                                                       
procs_priv                                                                                   
proxies_priv                                                                                 
replication_asynchronous_connection_failover                                                 
replication_asynchronous_connection_failover_managed                                         
role_edges                                                                                   
server_cost                                                                                  
servers                                                                                      
slave_master_info                                                                            
slave_relay_log_info                                                                         
slave_worker_info                                                                            
slow_log                                                                                     
tables_priv                                                                                  
time_zone                                                                                    
time_zone_leap_second                                                                        
time_zone_name                                                                               
time_zone_transition                                                                         
time_zone_transition_type                                                                    
user
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>3-list_tables.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>4. First table</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that creates a table called&nbsp;<code>first_table</code> in the current database in your MySQL server.</p>
            <ul>
                <li><code>first_table</code> description:<ul>
                        <li><code>id</code> INT</li>
                        <li><code>name</code> VARCHAR(256)</li>
                    </ul>
                </li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
                <li>If the table&nbsp;<code>first_table</code> already exists, your script should not fail</li>
                <li>You are not allowed to use the&nbsp;<code>SELECT</code> or&nbsp;<code>SHOW</code> statements</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>4-first_table.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>5. Full description</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that prints the full description of the table&nbsp;<code>first_table</code> from the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
                <li>You are not allowed to use the&nbsp;<code>DESCRIBE</code> or&nbsp;<code>EXPLAIN</code> statements</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table                                                                         
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci        
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>5-full_table.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>6. List all in table</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all rows of the table&nbsp;<code>first_table</code> from the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>All fields should be printed</li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>6-list_values.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>7. First add</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that inserts a new row in the table&nbsp;<code>first_table</code> (database&nbsp;<code>hbtn_0c_0</code>) in your MySQL server.</p>
            <ul>
                <li>New row:<ul>
                        <li><code>id</code> =&nbsp;<code>89</code></li>
                        <li><code>name</code> =&nbsp;<code>Best School</code></li>
                    </ul>
                </li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Best School
89  Best School
89  Best School
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>7-insert_value.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>8. Count 89</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that displays the number of records with&nbsp;<code>id = 89</code> in the table&nbsp;<code>first_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>8-count_89.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>9. Full creation</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that creates a table&nbsp;<code>second_table</code> in the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server and add multiples rows.</p>
            <ul>
                <li><code>second_table</code> description:<ul>
                        <li><code>id</code> INT</li>
                        <li><code>name</code> VARCHAR(256)</li>
                        <li><code>score</code> INT</li>
                    </ul>
                </li>
                <li>The database name will be passed as an argument to the&nbsp;<code>mysql</code> command</li>
                <li>If the table&nbsp;<code>second_table</code> already exists, your script should not fail</li>
                <li>You are not allowed to use the&nbsp;<code>SELECT</code> and&nbsp;<code>SHOW</code> statements</li>
                <li>Your script should create these records:<ul>
                        <li><code>id</code> = 1,&nbsp;<code>name</code> = &ldquo;John&rdquo;,&nbsp;<code>score</code> = 10</li>
                        <li><code>id</code> = 2,&nbsp;<code>name</code> = &ldquo;Alex&rdquo;,&nbsp;<code>score</code> = 3</li>
                        <li><code>id</code> = 3,&nbsp;<code>name</code> = &ldquo;Bob&rdquo;,&nbsp;<code>score</code> = 14</li>
                        <li><code>id</code> = 4,&nbsp;<code>name</code> = &ldquo;George&rdquo;,&nbsp;<code>score</code> = 8</li>
                    </ul>
                </li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>9-full_creation.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>10. List by best</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all records of the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>Results should display both the score and the name (in this order)</li>
                <li>Records should be ordered by score (top first)</li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>10-top_score.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>11. Select the best</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all records with a&nbsp;<code>score &gt;= 10</code> in the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>Results should display both the score and the name (in this order)</li>
                <li>Records should be ordered by score (top first)</li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>11-best_score.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>12. Cheating is bad</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that updates the score of Bob to&nbsp;<code>10</code> in the table&nbsp;<code>second_table</code>.</p>
            <ul>
                <li>You are not allowed to use Bob&rsquo;s id value, only the&nbsp;<code>name</code> field</li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>12-no_cheating.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>13. Score too low</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that removes all records with a&nbsp;<code>score &lt;= 5</code> in the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>13-change_class.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>14. Average</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that computes the score average of all records in the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>The result column name should be&nbsp;<code>average</code></li>
                <li>The database name will be passed as an argument of the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>14-average.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>15. Number by score</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists the number of records with the same score in the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>The result should display:<ul>
                        <li>the&nbsp;<code>score</code></li>
                        <li>the number of records for this&nbsp;<code>score</code> with the label&nbsp;<code>number</code></li>
                    </ul>
                </li>
                <li>The list should be sorted by the number of records (descending)</li>
                <li>The database name will be passed as an argument to the&nbsp;<code>mysql</code> command</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>15-groups.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>16. Say my name</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all records of the table&nbsp;<code>second_table</code> of the database&nbsp;<code>hbtn_0c_0</code> in your MySQL server.</p>
            <ul>
                <li>Don&rsquo;t list rows without a&nbsp;<code>name</code> value</li>
                <li>Results should display the score and the name (in this order)</li>
                <li>Records should be listed by descending score</li>
                <li>The database name will be passed as an argument to the&nbsp;<code>mysql</code> command</li>
            </ul>
            <p>In this example, new data have been added to the table&nbsp;<code>second_table</code>.</p>
            <pre><code>guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>16-no_link.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>17. Go to UTF8</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write a script that converts&nbsp;<code>hbtn_0c_0</code> database to UTF8 (<code>utf8mb4</code>, collate&nbsp;<code>utf8mb4_unicode_ci</code>) in your MySQL server.</p>
            <p>You need to convert all of the following to&nbsp;<code>UTF8</code>:</p>
            <ul>
                <li>Database&nbsp;<code>hbtn_0c_0</code></li>
                <li>Table&nbsp;<code>first_table</code></li>
                <li>Field&nbsp;<code>name</code> in&nbsp;<code>first_table</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>100-move_to_utf8.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>18. Temperatures #0</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Import in&nbsp;<code>hbtn_0c_0</code> database this table dump:&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a></p>
            <p>Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).</p>
            <pre><code>guillaume@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>101-avg_temperatures.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>19. Temperatures #1</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Import in&nbsp;<code>hbtn_0c_0</code> database this table dump:&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a> (same as&nbsp;<code>Temperatures #0</code>)</p>
            <p>Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)</p>
            <pre><code>guillaume@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>102-top_city.sql</code></li>
                </ul>
            </div>
        </div>
        <div>
            <div>
                <div><button>&nbsp;Done?</button> <button>Help</button> <button>Check your code</button> <button>Get a sandbox</button></div>
                <div><br></div>
            </div>
        </div>
    </div>
</div>
<div>
    <div>
        <div>
            <h3>20. Temperatures #2</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Import in&nbsp;<code>hbtn_0c_0</code> database this table dump:&nbsp;<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql" title="download" target="_blank">download</a> (same as&nbsp;<code>Temperatures #0</code>)</p>
            <p>Write a script that displays the max temperature of each state (ordered by State name).</p>
            <pre><code>guillaume@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
guillaume@ubuntu:~/$ 
</code></pre>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0D-SQL_introduction</code></li>
                    <li>File:&nbsp;<code>103-max_state.sql</code></li>
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