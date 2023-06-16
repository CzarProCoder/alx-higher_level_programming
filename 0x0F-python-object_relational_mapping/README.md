<h1>0x0F. Python - Object-relational mapping</h1>
<div>
    <div>PythonOOPSQLMySQLORMSQLAlchemy</div>
</div>
<div>
    <ul>
        <li>&nbsp;By:&nbsp;Guillaume</li>
        <li>&nbsp;Weight:&nbsp;1</li>
        <li>&nbsp;Project will start&nbsp;<span title="">Jun 15, 2023 6:00 AM</span>, must end by&nbsp;<span title="">Jun 19, 2023 6:00 AM</span></li>
        <li>&nbsp;Checker&nbsp;was&nbsp;released at&nbsp;<span title="">Jun 16, 2023 6:00 AM</span></li>
        <li>&nbsp;An auto review will be launched at the deadline</li>
    </ul>
</div>
<div>
    <div>
        <h2>Before you start&hellip;</h2>
        <p><strong>Please make sure your MySQL server is in 8.0</strong> -&gt;&nbsp;<a href="https://intranet.alxswe.com/rltoken/paGukker_0KoG3D9FqymNQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>
        <h2>Background Context</h2>
        <p>In this project, you will link two amazing worlds: Databases and Python!</p>
        <p>In the first part, you will use the module&nbsp;<code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>
        <p>In the second part, you will use the module&nbsp;<code>SQLAlchemy</code> (don&rsquo;t ask me how to pronounce it&hellip;) an Object Relational Mapper (ORM).</p>
        <p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &ldquo;What can I do with my objects&rdquo; and not &ldquo;How this object is stored? where? when?&rdquo;. You won&rsquo;t write any SQL queries only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able to change your storage easily without re-writing your entire project.</p>
        <p>Without ORM:</p>
        <pre><code>conn = MySQLdb.connect(host=&quot;localhost&quot;, port=3306, user=&quot;root&quot;, passwd=&quot;root&quot;, db=&quot;my_db&quot;, charset=&quot;utf8&quot;)
cur = conn.cursor()
cur.execute(&quot;SELECT * FROM states ORDER BY id ASC&quot;) # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
</code></pre>
        <p>With an ORM:</p>
        <pre><code>engine = create_engine(&apos;mysql+mysqldb://{}:{}@localhost/{}&apos;.format(&quot;root&quot;, &quot;root&quot;, &quot;my_db&quot;), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print(&quot;{}: {}&quot;.format(state.id, state.name))
session.close()
</code></pre>
        <p>Do you see the difference? Cool, right?</p>
        <p>The biggest difficulty with ORM is: The syntax!</p>
        <p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&rsquo;t read the entire documentation before starting, just jump on it if you don&rsquo;t get something.</p>
        <h2>Resources</h2>
        <p><strong>Read or watch</strong>:</p>
        <ul>
            <li><a href="https://intranet.alxswe.com/rltoken/a8DUOWhXpNX3TEwgyT-U8A" title="Object-relational mappers" target="_blank">Object-relational mappers</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/JtFaKjnqxudr6Hi05Us1Lw" title="mysqlclient/MySQLdb documentation" target="_blank">mysqlclient/MySQLdb documentation</a> (<em>please don&rsquo;t pay attention to&nbsp;<code>_mysql</code></em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/TdUSYFNGbXJG1WjCEoq5FA" title="MySQLdb tutorial" target="_blank">MySQLdb tutorial</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/YyL5hsscviNH04XGW-XpfA" title="SQLAlchemy tutorial" target="_blank">SQLAlchemy tutorial</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/j9azWF2Db_2rNolTxOF3SA" title="SQLAlchemy" target="_blank">SQLAlchemy</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/0zLhY9KqKjn-zmdb7X598Q" title="mysqlclient/MySQLdb" target="_blank">mysqlclient/MySQLdb</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/pw50Bl1Bj84wksxm018dwA" title="Introduction to SQLAlchemy" target="_blank">Introduction to SQLAlchemy</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/B-xIdMtGvpus8vHxAIRrPg" title="Flask SQLAlchemy" target="_blank">Flask SQLAlchemy</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/deIzPMrfK8Ixqm-AboFHWg" title="10 common stumbling blocks for SQLAlchemy newbies" target="_blank">10 common stumbling blocks for SQLAlchemy newbies</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/dZfUNK3lJicGMK5PU0bE7Q" title="Python SQLAlchemy Cheatsheet" target="_blank">Python SQLAlchemy Cheatsheet</a></li>
            <li><a href="https://intranet.alxswe.com/rltoken/hNxBKC8lHge5XjsRO8ksHQ" title="SQLAlchemy ORM Tutorial for Python Developers" target="_blank">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
            <li><a href="https://intranet.alxswe.com/rltoken/5G_R2NmQRFqiZb84qxYERQ" title="SQLAlchemy Tutorial" target="_blank">SQLAlchemy Tutorial</a></li>
        </ul>
        <h2>Learning Objectives</h2>
        <p>At the end of this project, you are expected to be able to&nbsp;<a href="https://intranet.alxswe.com/rltoken/vPPdh3HKg3t23YFxUqHpFg" title="explain to anyone" target="_blank">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
        <h3>General</h3>
        <ul>
            <li>Why Python programming is awesome</li>
            <li>How to connect to a MySQL database from a Python script</li>
            <li>How to&nbsp;<code>SELECT</code> rows in a MySQL table from a Python script</li>
            <li>How to&nbsp;<code>INSERT</code> rows in a MySQL table from a Python script</li>
            <li>What ORM means</li>
            <li>How to map a Python Class to a MySQL table</li>
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
            <li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using&nbsp;<code>python3</code> (version 3.8.5)</li>
            <li>Your files will be executed with&nbsp;<code>MySQLdb</code> version&nbsp;<code>2.0.x</code></li>
            <li>Your files will be executed with&nbsp;<code>SQLAlchemy</code> version&nbsp;<code>1.4.x</code></li>
            <li>All your files should end with a new line</li>
            <li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
            <li>A&nbsp;<code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
            <li>Your code should use the pycodestyle (version&nbsp;<code>2.8.*</code>)</li>
            <li>All your files must be executable</li>
            <li>The length of your files will be tested using&nbsp;<code>wc</code></li>
            <li>All your modules should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).__doc__)&apos;</code>)</li>
            <li>All your classes should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&apos;</code>)</li>
            <li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).my_function.__doc__)&apos;</code> and&nbsp;<code>python3 -c &apos;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&apos;</code>)</li>
            <li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
            <li>You are not allowed to use&nbsp;<code>execute</code> with sqlalchemy</li>
        </ul>
        <h2>More Info</h2>
        <h3>Install&nbsp;<code>MySQLdb</code> module version&nbsp;<code>2.0.x</code></h3>
        <p>For installing&nbsp;<code>MySQLdb</code>, you need to have&nbsp;<code>MySQL</code> installed:&nbsp;<a href="https://intranet.alxswe.com/rltoken/paGukker_0KoG3D9FqymNQ" title="How to install MySQL 8.0 in Ubuntu 20.04" target="_blank">How to install MySQL 8.0 in Ubuntu 20.04</a></p>
        <pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info 
(2, 0, 3, &apos;final&apos;, 0)
</code></pre>
        <h3>Install&nbsp;<code>SQLAlchemy</code> module version&nbsp;<code>1.4.x</code></h3>
        <pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__ 
&apos;1.4.22&apos;
</code></pre>
        <p>Also, you can have this warning message:</p>
        <pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, &quot;&apos;@@SESSION.GTID_EXECUTED&apos; is deprecated and will be re
moved in a future release.&quot;)                                                                                                                    
  cursor.execute(statement, parameters)  
</code></pre>
        <p>You can ignore it.</p>
    </div>
</div>
<h2>Tasks</h2>
<div>
    <div>
        <div>
            <h3>0. Get all states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>states</code> from the database&nbsp;<code>hbtn_0e_0_usa</code>:</p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code> (no argument validation needed)</li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, &apos;California&apos;)
(2, &apos;Arizona&apos;)
(3, &apos;Texas&apos;)
(4, &apos;New York&apos;)
(5, &apos;Nevada&apos;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>0-select_states.py</code></li>
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
            <h3>1. Filter states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>states</code> with a&nbsp;<code>name</code> starting with&nbsp;<code>N</code> (upper N) from the database&nbsp;<code>hbtn_0e_0_usa</code>:</p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code> (no argument validation needed)</li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, &apos;New York&apos;)
(5, &apos;Nevada&apos;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>1-filter_states.py</code></li>
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
            <h3>2. Filter states by user input</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that takes in an argument and displays all values in the&nbsp;<code>states</code> table of&nbsp;<code>hbtn_0e_0_usa</code> where&nbsp;<code>name</code> matches the argument.</p>
            <ul>
                <li>Your script should take 4 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code>,&nbsp;<code>database name</code> and&nbsp;<code>state name searched</code> (no argument validation needed)</li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>You must use&nbsp;<code>format</code> to create the SQL query with the user input</li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &apos;Arizona&apos;
(2, &apos;Arizona&apos;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>2-my_filter_states.py</code></li>
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
            <h3>3. SQL Injection...</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Wait, do you remember the previous task? Did you test&nbsp;<code>&quot;Arizona&apos;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &apos;&quot;</code> as an input?</p>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa &quot;Arizona&apos;; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = &apos;&quot;
(2, &apos;Arizona&apos;)
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p>What? Empty?</p>
            <p>Yes, it&rsquo;s an&nbsp;<a href="https://intranet.alxswe.com/rltoken/qzLjdkHPTue2U1isMj5fJA" title="SQL injection" target="_blank">SQL injection</a> to delete all records of a table&hellip;</p>
            <p>Once again, write a script that takes in arguments and displays all values in the&nbsp;<code>states</code> table of&nbsp;<code>hbtn_0e_0_usa</code> where&nbsp;<code>name</code> matches the argument. But this time, write one that is safe from MySQL injections!</p>
            <ul>
                <li>Your script should take 4 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code>,&nbsp;<code>database name</code> and&nbsp;<code>state name searched</code> (safe from MySQL injection)</li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa &apos;Arizona&apos;
(2, &apos;Arizona&apos;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>3-my_safe_filter_states.py</code></li>
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
            <h3>4. Cities by states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>cities</code> from the database&nbsp;<code>hbtn_0e_4_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>cities.id</code></li>
                <li>You can use only&nbsp;<code>execute()</code> once</li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, &apos;San Francisco&apos;, &apos;California&apos;)
(2, &apos;San Jose&apos;, &apos;California&apos;)
(3, &apos;Los Angeles&apos;, &apos;California&apos;)
(4, &apos;Fremont&apos;, &apos;California&apos;)
(5, &apos;Livermore&apos;, &apos;California&apos;)
(6, &apos;Page&apos;, &apos;Arizona&apos;)
(7, &apos;Phoenix&apos;, &apos;Arizona&apos;)
(8, &apos;Dallas&apos;, &apos;Texas&apos;)
(9, &apos;Houston&apos;, &apos;Texas&apos;)
(10, &apos;Austin&apos;, &apos;Texas&apos;)
(11, &apos;New York&apos;, &apos;New York&apos;)
(12, &apos;Las Vegas&apos;, &apos;Nevada&apos;)
(13, &apos;Reno&apos;, &apos;Nevada&apos;)
(14, &apos;Henderson&apos;, &apos;Nevada&apos;)
(15, &apos;Carson City&apos;, &apos;Nevada&apos;)
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>4-cities_by_state.py</code></li>
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
            <h3>5. All cities by state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that takes in the name of a state as an argument and lists all&nbsp;<code>cities</code> of that state, using the database&nbsp;<code>hbtn_0e_4_usa</code></p>
            <ul>
                <li>Your script should take 4 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code>,&nbsp;<code>database name</code> and&nbsp;<code>state name</code> (SQL injection free!)</li>
                <li>You must use the module&nbsp;<code>MySQLdb</code> (<code>import MySQLdb</code>)</li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>cities.id</code></li>
                <li>You can use only&nbsp;<code>execute()</code> once</li>
                <li>The results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

guillaume@ubuntu:~/0x0F$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
guillaume@ubuntu:~/0x0F$ ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

guillaume@ubuntu:~/0x0F$  
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>5-filter_cities.py</code></li>
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
            <h3>6. First state model</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/f84fe6edb9436c8560996c6d72e17ea51dab28e1.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230616%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230616T184955Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d4006d12e7d538258c6fa65f107e14fa803a78a9b9ff165bb76bfea5ffc638da" alt=""></p>
            <p>Write a python file that contains the class definition of a&nbsp;<code>State</code> and an instance&nbsp;<code>Base = declarative_base()</code>:</p>
            <ul>
                <li><code>State</code> class:<ul>
                        <li>inherits from&nbsp;<code>Base</code> <a href="https://intranet.alxswe.com/rltoken/SFKIwNZ3IG6_4TL6dEsIuA" title="Tips" target="_blank">Tips</a></li>
                        <li>links to the MySQL table&nbsp;<code>states</code></li>
                        <li>class attribute&nbsp;<code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
                        <li>class attribute&nbsp;<code>name</code> that represents a column of a string with maximum 128 characters and can&rsquo;t be null</li>
                    </ul>
                </li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li><strong>WARNING:</strong> all classes who inherit from&nbsp;<code>Base</code> <strong>must</strong> be imported before calling&nbsp;<code>Base.metadata.create_all(engine)</code></li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;

guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table &apos;hbtn_0e_6_usa.states&apos; doesn&apos;t exist
guillaume@ubuntu:~/0x0F$ cat 6-model_state.py
#!/usr/bin/python3
&quot;&quot;&quot;Start link class to table in database 
&quot;&quot;&quot;
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == &quot;__main__&quot;:
    engine = create_engine(&apos;mysql+mysqldb://{}:{}@localhost/{}&apos;.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

guillaume@ubuntu:~/0x0F$ ./6-model_state.py root root hbtn_0e_6_usa
guillaume@ubuntu:~/0x0F$ cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table   Create Table
states  CREATE TABLE `states` (\n  `id` int(11) NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>model_state.py</code></li>
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
            <h3>7. All states via SQLAlchemy</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>State</code> objects from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>The results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

guillaume@ubuntu:~/0x0F$ cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>7-model_state_fetch_all.py</code></li>
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
            <h3>8. First state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that prints the first&nbsp;<code>State</code> object from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>The state you display must be the first in&nbsp;<code>states.id</code></li>
                <li>You are not allowed to fetch all states from the database before displaying the result</li>
                <li>The results must be displayed as they are in the example below</li>
                <li>If the table&nbsp;<code>states</code> is empty, print&nbsp;<code>Nothing</code> followed by a new line</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>8-model_state_fetch_first.py</code></li>
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
            <h3>9. Contains `a`</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>State</code> objects that contain the letter&nbsp;<code>a</code> from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code></li>
                <li>The results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>9-model_state_filter_a.py</code></li>
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
            <h3>10. Get a state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that prints the&nbsp;<code>State</code> object with the&nbsp;<code>name</code> passed as argument from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 4 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code>,&nbsp;<code>database name</code> and&nbsp;<code>state name to search</code> (SQL injection free)</li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>You can assume you have one record with the state name to search</li>
                <li>Results must display the&nbsp;<code>states.id</code></li>
                <li>If no state has the name you searched for, display&nbsp;<code>Not found</code></li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
guillaume@ubuntu:~/0x0F$ ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>10-model_state_my_get.py</code></li>
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
            <h3>11. Add a new state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that adds the&nbsp;<code>State</code> object &ldquo;Louisiana&rdquo; to the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Print the new&nbsp;<code>states.id</code> after creation</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>11-model_state_insert.py</code></li>
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
            <h3>12. Update a state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that changes the name of a&nbsp;<code>State</code> object from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Change the name of the&nbsp;<code>State</code> where&nbsp;<code>id = 2</code> to&nbsp;<code>New Mexico</code></li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>12-model_state_update_id_2.py</code></li>
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
            <h3>13. Delete states</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a script that deletes all&nbsp;<code>State</code> objects with a name containing the letter&nbsp;<code>a</code> from the database&nbsp;<code>hbtn_0e_6_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>13-model_state_delete_a.py</code></li>
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
            <h3>14. Cities in state</h3>
            <div>mandatory</div>
        </div>
        <div>
            <p>Write a Python file similar to&nbsp;<code>model_state.py</code> named&nbsp;<code>model_city.py</code> that contains the class definition of a&nbsp;<code>City</code>.</p>
            <ul>
                <li><code>City</code> class:<ul>
                        <li>inherits from&nbsp;<code>Base</code> (imported from&nbsp;<code>model_state</code>)</li>
                        <li>links to the MySQL table&nbsp;<code>cities</code></li>
                        <li>class attribute&nbsp;<code>id</code> that represents a column of an auto-generated, unique integer, can&rsquo;t be null and is a primary key</li>
                        <li>class attribute&nbsp;<code>name</code> that represents a column of a string of 128 characters and can&rsquo;t be null</li>
                        <li>class attribute&nbsp;<code>state_id</code> that represents a column of an integer, can&rsquo;t be null and is a foreign key to&nbsp;<code>states.id</code></li>
                    </ul>
                </li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
            </ul>
            <p>Next, write a script&nbsp;<code>14-model_city_fetch_by_state.py</code> that prints all&nbsp;<code>City</code> objects from the database&nbsp;<code>hbtn_0e_14_usa</code>:</p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>You must import&nbsp;<code>State</code> and&nbsp;<code>Base</code> from&nbsp;<code>model_state</code> -&nbsp;<code>from model_state import Base, State</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>Results must be sorted in ascending order by&nbsp;<code>cities.id</code></li>
                <li>Results must be display as they are in the example below (<code>&lt;state name&gt;: (&lt;city id&gt;) &lt;city name&gt;</code>)</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>model_city.py, 14-model_city_fetch_by_state.py</code></li>
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
            <h3>15. City relationship</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Improve the files&nbsp;<code>model_city.py</code> and&nbsp;<code>model_state.py</code>, and save them as&nbsp;<code>relationship_city.py</code> and&nbsp;<code>relationship_state.py</code>:</p>
            <ul>
                <li><code>City</code> class:<ul>
                        <li>No change</li>
                    </ul>
                </li>
                <li><code>State</code> class:<ul>
                        <li>In addition to previous requirements, the class attribute&nbsp;<code>cities</code> must represent a relationship with the class&nbsp;<code>City</code>. If the&nbsp;<code>State</code> object is deleted, all linked&nbsp;<code>City</code> objects must be automatically deleted. Also, the reference from a&nbsp;<code>City</code> object to his&nbsp;<code>State</code> should be named&nbsp;<code>state</code></li>
                    </ul>
                </li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
            </ul>
            <p>Write a script that creates the&nbsp;<code>State</code> &ldquo;California&rdquo; with the&nbsp;<code>City</code> &ldquo;San Francisco&rdquo; from the database&nbsp;<code>hbtn_0e_100_usa</code>: (<code>100-relationship_states_cities.py</code>)</p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>You must use the&nbsp;<code>cities</code> relationship for all&nbsp;<code>State</code> objects</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql
-- Create the database hbtn_0e_100_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_100_usa;
USE hbtn_0e_100_usa;

SELECT * FROM states;
SELECT * FROM cities;

guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 5: Table &apos;hbtn_0e_100_usa.states&apos; doesn&apos;t exist
guillaume@ubuntu:~/0x0F$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
guillaume@ubuntu:~/0x0F$ cat 100-relationship_states_cities.sql | mysql -uroot -p
Enter password: 
id  name
1   California
id  name    state_id
1   San Francisco   1
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>relationship_city.py, relationship_state.py, 100-relationship_states_cities.py</code></li>
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
            <h3>16. List relationship</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>State</code> objects, and corresponding&nbsp;<code>City</code> objects, contained in the database&nbsp;<code>hbtn_0e_101_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>The connection to your MySQL server must be to&nbsp;<code>localhost</code> on port&nbsp;<code>3306</code></li>
                <li>You must only use one query to the database</li>
                <li>You must use the&nbsp;<code>cities</code> relationship for all&nbsp;<code>State</code> objects</li>
                <li>Results must be sorted in ascending order by&nbsp;<code>states.id</code> and&nbsp;<code>cities.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>&lt;state id&gt;: &lt;state name&gt;
&lt;tabulation&gt;&lt;city id&gt;: &lt;city name&gt;
</code></pre>
            <pre><code>guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql
-- Create states table in hbtn_0e_101_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_101_usa;
USE hbtn_0e_101_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES (&quot;California&quot;), (&quot;Arizona&quot;), (&quot;Texas&quot;), (&quot;New York&quot;), (&quot;Nevada&quot;);

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, &quot;San Francisco&quot;), (1, &quot;San Jose&quot;), (1, &quot;Los Angeles&quot;), (1, &quot;Fremont&quot;), (1, &quot;Livermore&quot;);
INSERT INTO cities (state_id, name) VALUES (2, &quot;Page&quot;), (2, &quot;Phoenix&quot;);
INSERT INTO cities (state_id, name) VALUES (3, &quot;Dallas&quot;), (3, &quot;Houston&quot;), (3, &quot;Austin&quot;);
INSERT INTO cities (state_id, name) VALUES (4, &quot;New York&quot;);
INSERT INTO cities (state_id, name) VALUES (5, &quot;Las Vegas&quot;), (5, &quot;Reno&quot;), (5, &quot;Henderson&quot;), (5, &quot;Carson City&quot;);

guillaume@ubuntu:~/0x0F$ cat 101-relationship_states_cities_list.sql | mysql -uroot -p
guillaume@ubuntu:~/0x0F$ ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
1: California
    1: San Francisco
    2: San Jose
    3: Los Angeles
    4: Fremont
    5: Livermore
2: Arizona
    6: Page
    7: Phoenix
3: Texas
    8: Dallas
    9: Houston
    10: Austin
4: New York
    11: New York
5: Nevada
    12: Las Vegas
    13: Reno
    14: Henderson
    15: Carson City
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>101-relationship_states_cities_list.py</code></li>
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
            <h3>17. From city</h3>
            <div>#advanced</div>
        </div>
        <div>
            <p>Write a script that lists all&nbsp;<code>City</code> objects from the database&nbsp;<code>hbtn_0e_101_usa</code></p>
            <ul>
                <li>Your script should take 3 arguments:&nbsp;<code>mysql username</code>,&nbsp;<code>mysql password</code> and&nbsp;<code>database name</code></li>
                <li>You must use the module&nbsp;<code>SQLAlchemy</code></li>
                <li>Your script should connect to a MySQL server running on&nbsp;<code>localhost</code> at port&nbsp;<code>3306</code></li>
                <li>You must use only one query to the database</li>
                <li>You must use the&nbsp;<code>state</code> relationship to access to the&nbsp;<code>State</code> object linked to the&nbsp;<code>City</code> object</li>
                <li>Results must be sorted in ascending order by&nbsp;<code>cities.id</code></li>
                <li>Results must be displayed as they are in the example below</li>
                <li>Your code should not be executed when imported</li>
            </ul>
            <pre><code>&lt;city id&gt;: &lt;city name&gt; -&gt; &lt;state name&gt;
</code></pre>
            <pre><code>guillaume@ubuntu:~/0x0F$ ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
1: San Francisco -&gt; California
2: San Jose -&gt; California
3: Los Angeles -&gt; California
4: Fremont -&gt; California
5: Livermore -&gt; California
6: Page -&gt; Arizona
7: Phoenix -&gt; Arizona
8: Dallas -&gt; Texas
9: Houston -&gt; Texas
10: Austin -&gt; Texas
11: New York -&gt; New York
12: Las Vegas -&gt; Nevada
13: Reno -&gt; Nevada
14: Henderson -&gt; Nevada
15: Carson City -&gt; Nevada
guillaume@ubuntu:~/0x0F$ 
</code></pre>
            <p><strong>No test cases needed</strong></p>
        </div>
        <div>
            <div>
                <p><strong>Repo:</strong></p>
                <ul>
                    <li>GitHub repository:&nbsp;<code>alx-higher_level_programming</code></li>
                    <li>Directory:&nbsp;<code>0x0F-python-object_relational_mapping</code></li>
                    <li>File:&nbsp;<code>102-relationship_cities_states_list.py</code></li>
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