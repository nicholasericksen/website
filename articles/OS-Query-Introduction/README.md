# OSQuery Introduction

A bit of fun over the holiday looking around my Macbook.
Finally got around to installing OSQuery since I have heard a lot about it in the infosec community.
Essentially it is a daemon and CLI tool that can be installed to query the OS.
These queries can range from pulling information about which binaries are unsigned on the machine
to determining what ports are currently open.
The queries can be scheduled using the daemon to pull the information on a reoccurring basis and 
determine when changes occur. 
This can be pretty handy from an investigation and monitoring perspective.
And for exploring of course.

## Initial Query for Auto Launch Daemons
After installation described [here](https://osquery.readthedocs.io/en/stable/installation/install-macos/)
I booted up the `osqueryi` CLI tool and started playing around.
As always running the help command `.help` is a nice way to get started without having to take up more 
bandwidth over Google search.

The tool itself using a Sqlite DB and queries are made with the same syntax.
`.tables` will list all the default tables which can be immediately be explored.
Personally I wanted to know all the programs set to auto launch which weren't created directly by Apple.

This can easily be accomplished with the following query

```
select name,process_type,username from launchd where name NOT LIKE '%com.apple%';
```

How did I get to this query you may ask yourself?

First off running a simple 

```
select * from launchd;
```

produced a large table of results. 
It was quite unmanageble so I looked into trimming it down.
Grab one column to make it more readable by replacing the `*` with a column name.

```
select name from launchd;
```

That makes it a little slimer so it can fit in my terminal window.

But how to know what columns are available?
SQLite can help here a bit.

```
pragma table_info(launchd);
```
will list all the columns available for the table.
I then hand picked a few.

Finally I wanted to look at anything that didn't appear to come from Apple.
Again some SQLite magic resulted in

```
select name,process_type,username from launchd where name NOT LIKE '%com.apple%';
```

Nice and easy huh?!

## Conclusion
It can be fast to get going with OSQuery especially if you have some SQLite knowledge
(if you don't, no time like the present to learn).

Here is my final list

```
osquery> select name,process_type,username from launchd where name NOT LIKE '%com.apple%';
+------------------------------------------------------+--------------+----------+
| name                                                 | process_type | username |
+------------------------------------------------------+--------------+----------+
| bootps.plist                                         |              |          |
| com.vix.cron.plist                                   |              |          |
| ntalk.plist                                          |              |          |
| org.apache.httpd.plist                               |              |          |
| org.cups.cups-lpd.plist                              | Adaptive     | _lp      |
| org.cups.cupsd.plist                                 | Interactive  |          |
| org.net-snmp.snmpd.plist                             | Background   |          |
| org.openldap.slapd.plist                             |              |          |
| ssh.plist                                            |              |          |
| tftp.plist                                           |              |          |
| com.cloudflare.1dot1dot1dot1.macos.warp.daemon.plist |              | root     |
| com.docker.vmnetd.plist                              |              |          |
| com.microsoft.teams.TeamsUpdaterDaemon.plist         |              |          |
| com.native-instruments.NativeAccess.Helper2.plist    |              |          |
| io.osquery.agent.plist                               |              |          |
| org.xquartz.privileged_startx.plist                  |              |          |
| us.zoom.ZoomDaemon.plist                             |              |          |
| com.openssh.ssh-agent.plist                          |              |          |
| org.xquartz.startx.plist                             |              |          |
| com.github.facebook.watchman.plist                   | Interactive  |          |
+------------------------------------------------------+--------------+----------+
```

Let me know if you see anything suspicious here.
Some of these things I don't like and will be removed so this was a useful afternoon.
