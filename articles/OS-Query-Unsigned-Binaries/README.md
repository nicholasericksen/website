# Detecting Unsigned Binaries with OSQuery

Some malware may like to try and hide itself by looking like an Apple program.
Based on the last query of checking launchd for `com.apple` may not be enough.
So it seems reasonable to try and check the binaries signature for more assurance.
Unsigned binaries can be a big hint that something is wrong on your machine.
Leveraging OS Query should make our lives easier to try and find unsigned binaries.

```
select * FROM signature s JOIN launchd d ON d.program_arguments = s.path WHERE signed=0 AND d.run_at_load=1;
```

Thankfully there are no results returned from this query on my machine!

### REF
I needed a little help on this one...Thank you [Guillaume Ross!](https://www.uptycs.com/blog/hunting-for-evil-launch-daemons-identifying-suspicious-behavior-with-osquery)
